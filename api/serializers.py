from api.models import Question, Answer, User
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            "title",
            "description",
            "user",
        )

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = (
            'pk',
            'user',
            'question',
            'response',
            'answered',
            'favorited',
        )

class QuestionAnswerSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, required=False)
    class Meta:
        model = Question
        fields = (
            "title",
            "description",
            "answers",
            "answered",
            "pk",
            "favorited"
        )