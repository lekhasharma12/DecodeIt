from django.contrib import admin
from .models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ('pub_date',)


class AnswerAdmin(admin.ModelAdmin):
    readonly_fields = ('pub_date',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
