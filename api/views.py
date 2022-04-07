from django.shortcuts import render
from api.models import Question, Answer, User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from .serializers import AnswerSerializer, QuestionSerializer, QuestionAnswerSerializer, UserSerializer
from api import serializers


class QuestionListView(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserQuestionsListView(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.filter()
    serializer_class = QuestionSerializer

class QuestionDetailsView(ListCreateAPIView):
    serializer_class = QuestionAnswerSerializer

    def get_queryset(self):
        return Answer.objects.filter(question_id=self.kwargs["question_pk"])

class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
