from django.db import models


class PreCoin(models.Model):
    code = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return self.code
