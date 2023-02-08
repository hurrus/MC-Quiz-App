from django.urls import path
from quiz import views

urlpatterns = [
    path('question/<int:question_id>/', views.question_view, name='question_view'),
    path('result/<int:question_id>/', views.result_view, name='question_result'),
]