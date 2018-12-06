from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView, CreateView
from quiz.models import Question, Answer
from django.db.models import Count
from django.shortcuts import get_object_or_404
from quiz.forms import QuestionCreateForm, AnswerCreateForm
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect, Http404

class QuestionListView(ListView):
    context_object_name = 'question_list'
    model = Question
    paginate_by = 3

    def get_queryset(self):
        
        return Question.objects.all().order_by('-created_at')

    def get_template_names(self):
        template_name = 'quiz/question_list.html'
        return template_name

    def get_context_data(self, **kwargs):
        context = super(QuestionListView, self).get_context_data(**kwargs)
        unanswered_questions = Question.objects.filter(
            answer__isnull=True).order_by('-created_at')
        
        context['unanswered_questions'] = unanswered_questions
    
        return context


class QuestionDetailView(DetailView):
    model = Question
    context_object_name = 'question_detail'
    template_name = 'quiz/question_detail.html'

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        current_question = get_object_or_404(Question,
                                             slug=self.kwargs['slug'])
        favorite_questions = Question.objects.all().order_by("title").annotate(
            savedquestion_count=Count('savedquestion'))
        related_questions = Question.objects.filter(
            question_tag__id__in=current_question.question_tag.distinct())
        related_questions = set(related_questions)
        context['related_questions'] = related_questions
        context['favorite_questions'] = favorite_questions
        context['current_question'] = current_question
        
        return context

    def get_object(self, **kwargs):
        """ Increase view count when user views details of question. """

        question = super(QuestionDetailView, self).get_object()
        question.view_count += 1
        question.save()
        return question


@login_required
def rate_question(request, object_id, score):

    question = get_object_or_404(Question, id=object_id)
    if request.user == question.author:
        if(score =='up'):
            question.rating +=1
        else:
            question.rating -=1
        question.save() 
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def rate_answer(request, object_id, score):

    answer = get_object_or_404(Answer, id=object_id)
    
    if(score =='up'):
        answer.rating +=1
    else:
        answer.rating -=1
    answer.save() 
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
