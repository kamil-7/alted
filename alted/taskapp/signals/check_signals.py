from signals.models import Signal, Event


def apply_operator(value, target, operator):
    if operator == 0:
        return value == target
    elif operator == 1:
        return value > target
    elif operator == 2:
        return value < target
    elif operator == 3:
        return value >= target
    elif operator == 4:
        return value <= target


def check_signals():
    for signal in Signal.objects.all():
        for condition in signal.condition_set.all():
            value = condition.target.price_usd
            if not apply_operator(value, condition.value, condition.operator):
                break
        else:
            Event.objects.create(signal=signal, user=signal.user)
