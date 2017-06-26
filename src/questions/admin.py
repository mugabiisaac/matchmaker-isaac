from django.contrib import admin

from .models import Question, Answer, MatchAnswer

class QuestionAdmin(admin.ModelAdmin):
    class Meta:
        model = Question

admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    class Meta:
        model = Answer

admin.site.register(Answer, AnswerAdmin)


class MatchAnswerAdmin(admin.ModelAdmin):
    class Meta:
        model = MatchAnswer

admin.site.register(MatchAnswer, MatchAnswerAdmin)
