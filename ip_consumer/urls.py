from django.urls import path

from ip_consumer.views import IPAddressListView

urlpatterns = [
    path("ip-consumer", IPAddressListView.as_view()),
]
