from django.urls import path

from .views import (
    create_quiz,
    get_active_quiz,
    get_quiz_result,
    get_all_quizzes,
)

app_name = 'quizzes'

urlpatterns = [
    path('', create_quiz, name='create_quiz'),
    path('active/', get_active_quiz, name='get_active_quiz'),
    path('result/<int:id>/', get_quiz_result, name='get_quiz_result'),
    path('all/', get_all_quizzes, name='get_all_quizzes'),
]
