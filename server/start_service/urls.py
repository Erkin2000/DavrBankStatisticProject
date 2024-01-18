from django.urls import path
from . import views


urlpatterns = [
    path('', views.InformationOverdueListView.as_view()),
    path('upload_excel/', views.GetExcel, name='push_excel'),
    # path('upload_excel2/', views.GetExcel2, name='push_excel')
]


