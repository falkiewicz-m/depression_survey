from django.contrib import admin
from .models import QuestionM, ChoiceM, Current_answer

admin.site.register(QuestionM)
admin.site.register(ChoiceM)
admin.site.register(Current_answer)