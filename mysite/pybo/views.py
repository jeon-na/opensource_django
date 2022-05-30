from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question


# Create your views here.
def index(request):
    question_list = Question.objects.all().order_by('-id')
    context = {'question_list': question_list}
    return render(request, 'pybo/index.html', context)


#응시하기
def test(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'pybo/test.html', {'question': question})
