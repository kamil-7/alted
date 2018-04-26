import json
import sys

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.views.generic import ListView, DetailView
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from alted.utils import MessagesMixin, CustomEncoder
from signals.models import Signal, OPERATOR_CHOICES
from signals.serializers import SignalSerializer

if 'makemigrations' not in sys.argv and 'migrate' not in sys.argv:
    target_choices = (
        (ContentType.objects.get(app_label='coins', model='coin').id, "Coin"),
        (ContentType.objects.get(app_label='markets', model='market').id, "Market"),
    )
    target_choices = [dict(value=target[0], label=target[1]) for target in target_choices]

oparator_choices = [dict(value=operator[0], label=operator[1]) for operator in OPERATOR_CHOICES]

import itertools
from datetime import timedelta


def group_dates(iterable):
    iterable = sorted(set(iterable))
    keyfunc = lambda t: t[1] - timedelta(days=t[0])
    for key, group in itertools.groupby(enumerate(iterable), keyfunc):
        group = list(group)
        if len(group) == 1:
            yield group[0][1]
        else:
            yield group[0][1], group[-1][1]


class SignalListView(MessagesMixin, LoginRequiredMixin, ListView):
    template_name = 'pages/signals/signal_list/signal_list.html'
    messages = dict(
        created="Signal Created"
    )

    def get_queryset(self):
        return Signal.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(SignalListView, self).get_context_data(**kwargs)
        context['data'] = json.dumps(dict(
            operatorChoices=oparator_choices,
            targetChoices=target_choices,
        ), cls=CustomEncoder)

        signal_list = self.request.user.signal_set.all()
        grouped_events = list()

        for signal in signal_list:
            event_list = signal.event_set.order_by('date')
            if event_list:

                # initializing from first event
                event_list = iter(event_list)
                last = next(event_list)
                first = last
                reset = False

                for event in event_list:
                    # starting streak over
                    if reset:
                        last = event
                        first = event
                        reset = False

                    # streak continues
                    if event.date < last.date + timedelta(seconds=90):
                        last = event
                    else:
                        # save signle occurence
                        if first == last:
                            grouped_events.append(first)

                        # save grouped
                        else:
                            grouped_events.append(dict(
                                date_start=first.date,
                                date_end=last.date,
                                signal=first.signal
                            ))

                        reset = True
                else:
                    # todo: super messy, needs a refactor
                    if reset:
                        last = event
                        first = event
                        reset = False

                    if first == last:
                        grouped_events.append(first)

                    # save grouped
                    else:
                        grouped_events.append(dict(
                            date_start=first.date,
                            date_end=last.date,
                            signal=first.signal
                        ))

        context['event_list'] = grouped_events
        print(grouped_events)
        return context


class SignalDetailView(LoginRequiredMixin, DetailView):
    template_name = 'pages/signals/signal_detail/signal_detail.html'
    model = Signal

    def get_context_data(self, **kwargs):
        context = super(SignalDetailView, self).get_context_data(**kwargs)
        signal = SignalSerializer(context['object']).data
        context['data'] = json.dumps(dict(
            signal=signal,
            operatorChoices=oparator_choices,
            targetChoices=target_choices,
        ), cls=CustomEncoder)
        return context


class SignalCreateAPI(CreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = SignalSerializer


class SignalUpdateAPI(UpdateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = SignalSerializer

    def get_queryset(self):
        return Signal.objects.filter(user=self.request.user)


class ConditionCreateAPI(CreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
