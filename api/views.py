from django.shortcuts import get_object_or_404, render
from api.models import Question, Answer, User
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from .serializers import AnswerSerializer, QuestionSerializer, QuestionAnswerSerializer, UserSerializer
from api import serializers
from rest_framework.decorators import action


class QuestionListView(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class QuestionFavoriteView(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 
    @action(detail=False, methods=['get'])
    def favorited(self, request):
        question = self.get_queryset().filter(favorited=True).filter(user_id=self.request.user)
        serializer = self.get_serializer(question, many=True)
        return Response(serializer.data)


class AnswerListView(ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    @action(detail=False, methods= ["get"])
    def correct(self, request):
        accepted_answers = self.get_queryset().filter(accepted=True)
        serializer = self.get_serializer(accepted_answers, many=True)
        return Response(serializer.data)



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


class AnswerDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

def accepted(self, request):
    accepted_answers = Question.objects.filter(correct=True)
    serializer = self.get_serializer(accepted_answers, many=True)
    return Response(serializer.data)

class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class QuestionSearchView(ListAPIView):
    serializer_class=QuestionSerializer
    queryset=Question.objects.all()

    def get_queryset(self):
        search_term=self.request.query_params.get("description")
        if search_term is not None:
            return Question.objects.filter(description__icontains=search_term)


