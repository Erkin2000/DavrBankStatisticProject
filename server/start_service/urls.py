from django.urls import path
from . import views


urlpatterns = [
    path('', views.InformationOverdueListView.as_view()),
]


