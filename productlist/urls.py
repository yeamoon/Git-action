from django.urls import path
from .views import ListingsView

urlpatterns = [
    path('', ListingsView.as_view()),
]