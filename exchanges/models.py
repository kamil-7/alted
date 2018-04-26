from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.text import slugify


class Exchange(models.Model):
    name = models.CharField(max_length=32)
    code = models.CharField(max_length=8)
    slug = models.SlugField(max_length=8, blank=True, unique=True)

    volume_usd = models.DecimalField(max_digits=32, decimal_places=8, null=True, blank=True)
    volume_btc = models.DecimalField(max_digits=32, decimal_places=8, null=True, blank=True)

    ticker_url = models.URLField(max_length=2000, default='', blank=True)

    code_substitutes = JSONField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.code)
        super(Exchange, self).save(*args, **kwargs)
