from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage
from .models import Question, Answer


@require_GET
def test(request, *args, **kwargs):
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


@require_GET
def login(request, *args, **kwargs):
    return HttpResponse('login')


@require_GET
def signup(request, *args, **kwargs):
    return HttpResponse('signup')


@require_GET
def question(request, *args, **kwargs):
    try:
        id = int(kwargs["id"])
    except ValueError:
        raise Http404

    quest = get_object_or_404(Question, pk=id)

    return render(request, "question.html", {
        "question": quest,
        "answers": Answer.objects.filter(question=quest.pk)
    })


@require_GET
def ask(request, *args, **kwargs):
    return HttpResponse('ask')


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
def new(request, *args, **kwargs):
    return HttpResponse('new')

