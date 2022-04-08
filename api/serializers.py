from api.models import Question, Answer, User
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Question
        fields = (
            "pk",
            "title",
            "description",
            "user",
        )

class AnswerSerializer(serializers.ModelSerializer):
    answers_list = QuestionSerializer(many=True, required=False)
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Answer
        fields = (
            'pk',
            'user',
            'answers_list',
            'response',
            'answered',
            'favorited',
        )

class QuestionAnswerSerializer(serializers.ModelSerializer):
    answers_list = AnswerSerializer(many=True, required=False)
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Question
        fields = (
            "title",
            "description",
            "answers_list",
            "pk",
            "favorited",
            "user"
        )

class UserSerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all())
    answer_user = serializers.PrimaryKeyRelatedField(many=True, queryset=Answer.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'questions', 'answer_user')