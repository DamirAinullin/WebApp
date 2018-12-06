from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from _datetime import datetime
import re
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
        question.author = self.user
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
        answer.author = self.user
        answer.save()
        return answer


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=254)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data["username"]
        if username == "" or username is None or len(username) < 4:
            raise forms.ValidationError("username %s is not allowed" % username)
        return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        if email == "" or email is None or \
                re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email) is None:
            raise forms.ValidationError("email %s is not allowed" % email)
        return email

    def clean_password(self):
        password = self.cleaned_data["password"]
        if password == "" or password is None or len(password) < 4:
            raise forms.ValidationError("such password is not allowed")
        return password

    def save(self):
        User.objects.create_user(self.cleaned_data["username"],
                                 self.cleaned_data["email"],
                                 self.cleaned_data["password"])

        return authenticate(username=self.cleaned_data["username"], password=self.cleaned_data["password"])


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data["username"]
        if username == "" or username is None or len(username) < 4:
            raise forms.ValidationError("username or password is not correct")
        return username

    def clean_password(self):
        password = self.cleaned_data["password"]
        if password == "" or password is None or len(password) < 4:
            raise forms.ValidationError("username or password is not correct")
        return password

    def save(self):
        return authenticate(username=self.cleaned_data["username"], password=self.cleaned_data["password"])
