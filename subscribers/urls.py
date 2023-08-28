from django.urls import path
from .views import SubscribeView, SubscribedView

urlpatterns = [
    path("subscribe/", SubscribeView.as_view(), name="subscribe"),
    path("subscribed/", SubscribedView.as_view(), name="subscribed"),
]