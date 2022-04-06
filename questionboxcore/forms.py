from django import forms
from api.models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = (
            'title',
            'description',
        )

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = (
            'response',
            
        )