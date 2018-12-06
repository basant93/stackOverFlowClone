from django.contrib import admin

# Register your models here.
from .models import Question, QuestionTag, Answer

admin.site.register(QuestionTag)
admin.site.register(Question)
admin.site.register(Answer)

