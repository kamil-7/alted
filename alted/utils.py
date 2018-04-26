import datetime
import json
from decimal import Decimal

from django.contrib import messages
from django.core.exceptions import ImproperlyConfigured
from django.utils.text import slugify


class SlugifyMixin(object):
    def get_unique_slug(self):
        stopwords = ['best', 'resources', 'resource']
        querywords = self.name.split()

        resultwords = [word for word in querywords if word.lower() not in stopwords]
        name = ' '.join(resultwords)

        slug = slugify(name)
        unique_slug = slug
        num = 1
        while type(self).objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):

        if isinstance(obj, set):
            return list(obj)

        if isinstance(obj, Decimal):
            return float(obj)

        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')

        return json.JSONEncoder.default(self, obj)


class MessagesMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if self.messages is None:
            raise ImproperlyConfigured(
                "MessagesMixin requires messages.")
        else:
            key = request.GET.get('m')
            if key in self.messages:
                messages.add_message(request, messages.INFO, self.messages[key])
            return super(MessagesMixin, self).dispatch(request, *args, **kwargs)
