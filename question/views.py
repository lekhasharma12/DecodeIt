from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from .forms import QuestionForm, AnswerForm
from .models import Question, Answer


@login_required
def addquestion_view(request):
    form = QuestionForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.added_by = request.user
        instance.save()
        return redirect('home')
    else:
        form = QuestionForm(request.POST)
        context = {
            'form': form
        }
        return render(request, 'question/add_question.html', context)


def home_view(request):
    things = Question.objects.all().order_by('-pub_date')
    context = {
        'things': things
    }
    return render(request, 'home.html', context)

@login_required
def addanswer_view(request, question_id):
    form = AnswerForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.added_by = request.user
        instance.question = Question.objects.get(pk=question_id)
        instance.save()
        return redirect('home')
    else:
        question = Question.objects.get(pk=question_id)
        if question.added_by == request.user:
            return redirect('home')
        else:
            form = AnswerForm(request.POST)
            context = {
                'form': form,
                'question': question
            }
        return render(request, 'question/add_answer.html', context)


def viewanswer_view(request, question_id):
    ques = Question.objects.get(pk=question_id)
    answers = Answer.objects.filter(question=ques)
    context = {
        'ques': ques,
        'answers': answers
    }
    return render(request, 'question/view_answer.html', context)
