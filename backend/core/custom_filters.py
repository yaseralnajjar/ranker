from django.contrib import admin

from .models import (Test)


class BaseListFilter(admin.SimpleListFilter):
    template = 'django_admin_listfilter_dropdown/dropdown_filter.html'
    action_lookup = None

    def lookups(self, request, model_admin):
        tupleObj = ()
        for obj in self.dropdown_objects.all():
            tupleData = None
            tupleData = (obj.id, str(obj))
            tupleObj = tupleObj + (tupleData,)

        return tupleObj


class QuestionsByTestListFilter(BaseListFilter):
    title = 'Test'
    parameter_name = 'by_test'
    dropdown_objects = Test.objects

    def queryset(self, request, queryset):
        obj_id = self.value()
        if obj_id is None:
            return queryset

        return queryset.filter(test=obj_id)
