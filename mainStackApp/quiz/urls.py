from django.urls import path, include
from django.views.generic import TemplateView
from quiz.views import QuestionListView, QuestionDetailView, rate_question, rate_answer

urlpatterns = [
                path('all/', QuestionListView.as_view(),name='question_list'),
                path('question/<slug>/',QuestionDetailView.as_view(),
                           name='question_detail'),
                path('rate_question/<object_id>/<score>/',
                           rate_question, name='question_rate'),
                path('rate_answer/<object_id>/<score>/',
                           rate_answer, name='answer_rate'),

]