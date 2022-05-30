from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('test/<int:question_id>/', views.test),
    #path('result/<int:question_id>', views.result, name='result'),
]
