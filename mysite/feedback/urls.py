from django.urls import path

from . import views

app_name = 'feedback'

urlpatterns = [
    #path('', views.FeedbackView.as_view(), name='index'),
    path('', views.feedback, name='index'),
    path('thanks/', views.thanks, name='thanks')
]