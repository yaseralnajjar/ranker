from django.contrib import admin
from django.contrib.admin import StackedInline, ModelAdmin

from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin

from .models import (Test, Question, Answer, Tag)
from .custom_filters import QuestionsByTestListFilter


class AnswersInline(SortableInlineAdminMixin, StackedInline):
    model = Answer


class QuestionAdmin(SortableAdminMixin, ModelAdmin):
    inlines = (AnswersInline,)
    list_filter = [
        QuestionsByTestListFilter,
    ]
    ordering = ['order']

    def get_queryset(self, request):
        self.filtered_test_id = request.GET.get('by_test', None)
        return super().get_queryset(request)

    def _move_item(self, request, startorder, endorder):
        """
        Allow to use SortableAdminMixin but first get the filtered questions from list_filter 
        """
        if self.filtered_test_id:
            self.model.objects = self.model.objects.filter(
                test=self.filtered_test_id)

        return super()._move_item(request, startorder, endorder)


class QuestionsInline(StackedInline):
    model = Question


class TestAdmin(ModelAdmin):
    inlines = (QuestionsInline,)


admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Tag)
