from django.contrib.sitemaps import Sitemap

from users.models import User


class UserSitemap(Sitemap):
    protocol = 'https'

    def items(self):
        return User.objects.all()
