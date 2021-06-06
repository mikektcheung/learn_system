from django.contrib import admin
from .models import *

class AnswerInline(admin.TabularInline):
    model = eng_answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(eng_quiz_topic)
admin.site.register(eng_quiz)
admin.site.register(eng_question, QuestionAdmin)
admin.site.register(eng_answer)
admin.site.register(eng_vocab_topic)
admin.site.register(eng_vocab)
