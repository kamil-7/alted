from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from signals.models import Signal, Condition, TelegramToken


class TelegramTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramToken
        fields = ('name', 'token')


class ConditionSerializer(serializers.ModelSerializer):
    targetType = serializers.PrimaryKeyRelatedField(source='target_type', queryset=ContentType.objects.all())
    targetId = serializers.IntegerField(source='target_id')
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Condition
        fields = ('id', 'targetType', 'targetId', 'operator', 'value')


class SignalSerializer(serializers.ModelSerializer):
    conditionSet = ConditionSerializer(source='condition_set', many=True)

    class Meta:
        model = Signal
        fields = ('id', 'name', 'conditionSet')
        depth = 2

    @staticmethod
    def get_conditionSet(obj):
        return ConditionSerializer(obj.condition_set, many=True).data

    def create(self, validated_data):
        condition_set = validated_data.pop('condition_set')
        user = self.context['request'].user
        signal = Signal.objects.create(**validated_data, user=user)

        for condition in condition_set:
            target_type = condition['target_type']
            target = target_type.get_object_for_this_type(id=condition['target_id'])
            Condition.objects.create(
                user=user,
                operator=condition['operator'],
                target=target,
                value=condition['value'],
                signal=signal
            )
        return signal

    def update(self, signal, validated_data):
        condition_set = validated_data.pop('condition_set')
        condition_set_ids = [condition['id'] for condition in condition_set]
        user = self.context['request'].user

        # check if objects ids belong to the user
        if Condition.objects.exclude(user=user).filter(id__in=condition_set_ids).exists():
            raise Exception()

        signal.name = validated_data['name']
        signal.save()

        # todo: pycharm doesn't like tuple comprehension
        old_conditions = signal.condition_set.exclude(id__in=condition_set_ids)
        old_conditions.delete()

        for condition in condition_set:
            target = condition.pop('target_type').get_object_for_this_type(id=condition.pop('target_id'))
            condition.target = target
            condition.user = user

            instance = Condition.objects.update_or_create(
                id=condition['id'],
                defaults=condition
            )

        return signal
