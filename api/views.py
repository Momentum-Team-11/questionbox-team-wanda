from django.shortcuts import render
from api.models import Question, Answer, User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateDestroyAPIView
from .serializers import AnswerSerializer, QuestionSerializer, QuestionAnswerSerializer, UserSerializer
from api import serializers
from django.contrib.postgres.search import SearchVector



class QuestionListView(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AnswerListView(ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class UserAnswersListView(ListCreateAPIView):
    serializer_class=AnswerSerializer

    def get_queryset(self):
     return self.request.user.answer_user.all()

class UserQuestionsListView(ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return self.request.user.questions.all()

class QuestionDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionAnswerSerializer


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SearchResultsList(ListAPIView):
    model = Question
    context_object_name = "description" #not sure what this is
    template_name = "search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Question.objects.annotate(search=SearchVector("title", "description")).filter(search=query)
