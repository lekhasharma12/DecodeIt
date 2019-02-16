from django import forms
from .models import Question, Answer


class QuestionForm(forms.ModelForm):
    question_text = forms.CharField(label="Write your question here...", widget=forms.Textarea)
    category = forms.CharField(label="Category :")

    class Meta:
        model = Question
        fields = ['question_text', 'category']
        #labels = {"question": "", "category": "Category"}


class AnswerForm(forms.ModelForm):
    answer = forms.TextInput()

    class Meta:
        model = Answer
        fields = ['answer']
