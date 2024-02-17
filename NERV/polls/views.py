from django.http import HttpResponse
from .models import Question
from django.shortcuts import render


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("просмотр %s" % question_id)

def results(request, question_id):
    resource = "результат вопроса номер %s"
    return HttpResponse(resource % question_id)


def vote(request, question_id):
    return HttpResponse("голосование %s" % question_id)
