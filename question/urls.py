from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addquestion_view, name='add'),
    path('view/', views.home_view, name='view'),
    path('add_answer/<int:question_id>/', views.addanswer_view, name='add_answer'),
    path('answers/<int:question_id>/', views.viewanswer_view, name='view_answer'),

]
