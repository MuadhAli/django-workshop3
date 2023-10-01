from django.contrib import admin
from polls.models import Question,Choice

class QuestionAdmin(admin.ModelAdmin):
    pass
list_filter = (('pub_date',),)
search_fields = ['question_text']
list_display = ('pub_date',)


admin.site.register(Question, QuestionAdmin)

class ChoiceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Choice, ChoiceAdmin)





