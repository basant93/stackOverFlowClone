from django import forms
from django.forms import Textarea

from quiz.models import Question, Answer


class QuestionCreateForm(forms.ModelForm):

    tag = forms.CharField(max_length=100, required = False, label="Tags", help_text="Add tags for a question.")

    class Meta:
        model = Question
        exclude = ['author', 'slug', 'created_at', 'view_count',
                   'question_tag']
        labels = {
            'title': 'title', 'question_text': 'Question text : '
        }

class AnswerCreateForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['answer_text']

        labels = {
            'answer_text': '',
        }

        widgets = {
            'answer_text': Textarea(
                attrs={'class': 'myredactor', 'rows': 3, }),

        }

        def __init__(self, author, current_question, *args, **kwargs):
            super(AnswerCreateForm, self).__init__(*args, **kwargs)
            self.author = author
            self.question = current_question
        
        def clean(self):

            if(Answer.objects.filter(question=self.question, author=self.author)):
                raise forms.ValidationError("Enter valid author name and question details")
            raise  self.cleaned_data
