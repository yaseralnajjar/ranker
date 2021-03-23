from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'role')


class MyUserAdmin(UserAdmin):
    add_form = UserCreateForm

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'role', 'first_name', 'last_name',),
        }),
    )

    fieldsets = (
        (None, {'fields': ('password',)}),
        (_('Personal info'), {
         'fields': ('email', 'first_name', 'last_name', 'role')}),
    )

    list_display = ('email', 'first_name', 'last_name', 'role')
    list_filter = ('role',)
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('role', 'email')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.exclude(is_superuser=True)


admin.site.register(User, MyUserAdmin)
