from api.models import Question, Answer, User
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            "pk",
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
    answers_list = AnswerSerializer(many=True, required=False)
    class Meta:
        model = Question
        fields = (
            "title",
            "description",
            "answers_list",
            "pk",
            "favorited"
        )

class UserSerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all())
    answer_user = serializers.PrimaryKeyRelatedField(many=True, queryset=Answer.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'questions', 'answer_user')