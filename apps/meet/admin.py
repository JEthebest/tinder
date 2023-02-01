from django.contrib import admin


from .models import Questionnaire, Like, Photo

# Register your models here.

admin.site.register(Questionnaire)
admin.site.register(Like)
admin.site.register(Photo)