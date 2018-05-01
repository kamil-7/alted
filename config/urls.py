from allauth.account.views import LoginView, LogoutView, PasswordResetView, confirm_email, password_reset, \
    password_reset_from_key, password_reset_done, password_reset_from_key_done
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views import defaults as default_views
from rest_framework.routers import DefaultRouter

from alted.views import TargetListAPI
from arbitrage.views import PriceDiffDetailView, PriceDiffListView
from coins.views import CoinListView, CoinDetailView, CoinMarketsView, CoinDetailAPI
from exchanges.views import ExchangeListView, ExchangeDetailView
from markets.views import MarketListView, MarketDetailView
from signals.views import SignalListView, SignalDetailView, ConditionCreateAPI, SignalUpdateAPI, SignalCreateAPI
from users.views import SignupView

router = DefaultRouter()

urlpatterns = [
                  # path('', RedirectView.as_view(pattern_name='coin-list'), name='home'),

                  path('', CoinListView.as_view(), name='home'),
                  path('coin/<slug:slug>/', CoinDetailView.as_view(), name='coin-detail'),
                  path('price-diff/', PriceDiffListView.as_view(), name='price-diff-list'),
                  path('price-diff/<slug:slug>/', PriceDiffDetailView.as_view(), name='price-diff-detail'),

                  path('signals/', SignalListView.as_view(), name='signal-list'),
                  path('signal/<int:pk>/', SignalDetailView.as_view(), name='signal-detail'),

                  # path('coins/(<slug:slug>/price-differences', CoinPriceDifferencesView.as_view(),
                  #      name='coin-price-differences'),
                  path('coin/<slug:slug>/markets', CoinMarketsView.as_view(), name='coin-markets'),

                  path('exchanges/', ExchangeListView.as_view(), name='exchange-list'),
                  path('exchanges/<slug:slug>/', ExchangeDetailView.as_view(), name='exchange-detail'),

                  path('markets/', MarketListView.as_view(), name='market-list'),
                  path('market/<slug:slug>/', MarketDetailView.as_view(), name='market-detail'),

                  path('api/target-list', TargetListAPI.as_view(), name='target-list-api'),
                  path('api/signal-create/', SignalCreateAPI.as_view(), name='signal-create-api'),
                  path('api/signal-update/<int:pk>/', SignalUpdateAPI.as_view(), name='signal-update-api'),
                  path('api/condition-create/', ConditionCreateAPI.as_view(), name='condition-create-api'),
                  path('api/coin-detail/<slug:slug>/', CoinDetailAPI.as_view(), name='coin-detial-api'),

                  path('login/', LoginView.as_view(), name='account_login'),
                  path('logout/', LogoutView.as_view(), name='account_logout'),
                  path('signup/', SignupView.as_view(), name='account_signup'),
                  path('reset-password/', PasswordResetView.as_view(), name='account_reset_password'),

                  path('confirm-email/(?P<key>[-:\w]+)/', confirm_email, name='account_confirm_email'),

                  # password reset
                  path('password/reset/', password_reset, name='account_reset_password'),
                  path('password/reset/done/', password_reset_done, name='account_reset_password_done'),
                  path('password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/', password_reset_from_key,
                       name='account_reset_password_from_key'),
                  path('password/reset/key/done/', password_reset_from_key_done,
                       name='account_reset_password_from_key_done'),

                  # Django Admin, use {% url 'admin:index' %}
                  path(settings.ADMIN_URL, admin.site.urls),

                  # url('settings/', SettingsView.as_view(), name='settings'),
                  # path('alerts/', AlertListView.as_view(), name='alert-list'),

              ] + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path('400/', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        path('403/', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        path('404/', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        path('500/', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
