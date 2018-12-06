from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.http import require_GET, require_http_methods
from django.core.paginator import Paginator, EmptyPage
import uuid
from .models import Question, Answer
from .forms import AskForm, AnswerForm, LoginForm, RegisterForm


@require_GET
def test(request):
    return HttpResponse('OK')


@require_GET
def index(request):
    try:
        page = int(request.GET.get("page", 1))
    except ValueError:
        raise Http404

    paginator = Paginator(Question.objects.new(), 10)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return render(request, "new.html", {
        "questions": page.object_list,
        "paginator": paginator,
        "page": page,
        "page_base_url": "/?page=",
        "question_base_url": "/question/"
    })


@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                request.session["sessionid"] = str(uuid.uuid4())
                return HttpResponseRedirect("/")
    else:
        form = LoginForm()
    return render(request, "login.html", {
        "form": form
    })


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            request.session["sessionid"] = str(uuid.uuid4())
            return HttpResponseRedirect("/")
    else:
        form = RegisterForm()
    return render(request, "signup.html", {
        "form": form
    })


@require_http_methods(["GET", "POST"])
def question(request, *args, **kwargs):
    try:
        id = int(kwargs["id"])
    except ValueError:
        raise Http404

    quest = get_object_or_404(Question, pk=id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        form.user = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(quest.get_absolute_url())
    else:
        form = AnswerForm()
    return render(request, "question.html", {
        "form": form,
        "question": quest,
        "answers": Answer.objects.filter(question=quest.pk)
    })


@require_http_methods(["GET", "POST"])
def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        form.user = request.user
        if form.is_valid():
            quest = form.save()
            return HttpResponseRedirect(quest.get_absolute_url())
    else:
        form = AskForm()
    return render(request, "ask.html", {"form": form})


@require_GET
def popular(request):
    try:
        page = int(request.GET.get("page", 1))
    except ValueError:
        raise Http404

    paginator = Paginator(Question.objects.popular(), 10)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return render(request, "popular.html", {
        "questions": page.object_list,
        "paginator": paginator,
        "page": page,
        "page_base_url": "/popular/?page=",
        "question_base_url": "/question/"
    })


@require_GET
def new(request):
    return HttpResponse('new')
