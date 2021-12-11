from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline

from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

from .custom_filters import QuestionsByTestListFilter
from .models import AnswerChoice, Invitation, Question, Submission, Tag, Test, TestQuestion


class AnswerChoiceInline(SortableInlineAdminMixin, StackedInline):
    model = AnswerChoice


class TestQuestionAdmin(SortableAdminMixin, ModelAdmin):
    inlines = (AnswerChoiceInline,)
    list_filter = [QuestionsByTestListFilter]
    ordering = ['order']
    list_display = ['order', 'question']

    def get_queryset(self, request):
        self.filtered_test_id = request.GET.get('by_test', None)
        return super().get_queryset(request)

    def _move_item(self, request, startorder, endorder):
        """Allow to use SortableAdminMixin but first get the filtered questions from list_filter"""
        print(self.filtered_test_id)
        if self.filtered_test_id:
            self.model.objects = self.model.objects.filter(test=self.filtered_test_id)

        return super()._move_item(request, startorder, endorder)


class TestQuestionInline(StackedInline):
    model = TestQuestion


class TestAdmin(ModelAdmin):
    inlines = (TestQuestionInline,)


admin.site.register(Test, TestAdmin)
admin.site.register(TestQuestion, TestQuestionAdmin)
admin.site.register(AnswerChoice)
admin.site.register(Tag)
admin.site.register(Invitation)
admin.site.register(Submission)
admin.site.register(Question)
