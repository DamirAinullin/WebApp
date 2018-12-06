from django import forms
from _datetime import datetime
from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def clean_text(self):
        text = self.cleaned_data["text"]
        if text == "" or text is None:
            raise forms.ValidationError("empty text is not allowed")
        return text

    def clean_title(self):
        title = self.cleaned_data["title"]
        if title == "" or title is None:
            raise forms.ValidationError("empty title is not allowed")
        return title

    def save(self):
        question = Question(**self.cleaned_data)
        question.date_added = datetime.now()
        question.rating = 1
        question.author_id = 2
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField()

    def clean_text(self):
        text = self.cleaned_data["text"]
        if text == "" or text is None:
            raise forms.ValidationError("empty text is not allowed")
        return text

    def clean_question(self):
        try:
            question = int(self.cleaned_data["question"])
        except ValueError:
            raise forms.ValidationError("no such question " + str(question))

        if Question.objects.filter(pk=question).count() == 0:
            raise forms.ValidationError("no such question " + str(question))
        return question

    def save(self):
        answer = Answer()
        answer.date_added = datetime.now()
        answer.text = self.cleaned_data["text"]
        answer.question_id = self.cleaned_data["question"]
        answer.author_id = 2
        answer.save()
        return answer
