from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from django.utils import timezone
from .models import Quiz

@api_view(['GET', 'POST'])
def create_quiz(request):
    if request.method == 'POST':
        # Handle the POST request to create a quiz
        question = request.data.get('question')
        options = request.data.get('options')
        right_answer = request.data.get('rightAnswer')
        start_date = request.data.get('startDate')
        end_date = request.data.get('endDate')

        # Your code for creating a quiz here

        return Response({'message': 'Quiz created successfully'})
    elif request.method == 'GET':
        # Handle the GET request to retrieve all quizzes

        # Your code for retrieving all quizzes here

        return Response({'message': 'Retrieve all quizzes'})


@api_view(['GET'])
def get_active_quiz(request):
    # Your code for retrieving the active quiz here

    return Response({'message': 'Retrieve active quiz'})


@api_view(['GET'])
def get_quiz_result(request, id):
    # Your code for retrieving the result of a quiz by its ID here

    return Response({'message': f'Retrieve quiz result for ID: {id}'})


@api_view(['GET'])
def get_all_quizzes(request):
    # Your code for retrieving all quizzes here

    return Response({'message': 'Retrieve all quizzes'})