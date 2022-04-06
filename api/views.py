from django.shortcuts import render
from api.models import Question, Answer, User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetriveUpdateDestroyAPIView
from .serializers import AnswerSerializer, QuestionSerializer, QuestionAnswerSerializer
from api import serializers





class QuestionListView(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AnswerListView(ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class UserQuestionsListView(RetriveUpdateDestroyAPIView):
    queryset = Question.objects.filter(user=User)
    serializer_class = QuestionSerializer

class QuestionDetailsView(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionAnswerSerializer

