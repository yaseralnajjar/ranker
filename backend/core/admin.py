from django.contrib import admin
from django.contrib.admin import StackedInline, ModelAdmin
from .models import (Test, Question)


class QuestionsInline(StackedInline):
    model = Question
    extra = 1


class TestAdmin(ModelAdmin):
    inlines = (QuestionsInline,)
