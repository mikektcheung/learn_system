from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(user_profile)
admin.site.register(redeem)
admin.site.register(redeem_type)
admin.site.register(eng_quiz_result)
admin.site.register(eng_question_result)
