from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from ..models import Question

def index(request):
    question_list = Question.objects.order_by('-create_date')
    page = request.GET.get('page', '1')
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}

    return render(request, 'question/question_list.html', context)

def detail(requset, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(requset, 'question/question_detail.html', context)