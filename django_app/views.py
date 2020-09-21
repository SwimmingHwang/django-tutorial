# Todo: https://docs.djangoproject.com/ko/3.1/intro/tutorial03/
#         하드코딩 url 제거해주기


from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.http import Http404

from django.template import loader
from .models import Question
from django.core import serializers

def questions(request):
    questions = Question.objects.filter().all()
    question_list = serializers.serialize('json', questions)
    return HttpResponse(question_list, content_type="text/json-comment-filtered")

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('django_app/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'django_app/index.html', context)
    # return HttpResponse(template.render(context, request))