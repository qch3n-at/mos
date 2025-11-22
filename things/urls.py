from django.urls import path

from . import views

urlpatterns = [
    path('keys/<slug:thing>', views.thingtoucher_list),
    path('usage/<slug:thing>', views.thingtoucher_usage),
    path('stats/<slug:thing>', views.thing_usage_stats),
]
