from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Question
from .forms import QuestionForm, AnswerForm

# Create your views here.

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

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('question:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'question/question_detail.html', context)

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('question:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'question/question_form.html', context)