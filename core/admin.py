from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest
from .models import HeaderNews, Admin, News, Feedback, Employee, Sponsor
from rest_framework.authtoken.admin import TokenProxy
from django.contrib.auth.models import Group 
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.admin.options import ModelAdmin
from django.utils.translation import gettext_lazy as lazy
from django import forms


class MyAdminSite(admin.AdminSite):
    site_title = "SIYF"
    site_header = "SIYF менеджер"
    site_url = "https://siyf.uz/"
    index_title = "SIYF"



my_site = MyAdminSite()

def makeAdminModelWithout(*args):
    class CustomAdminModel(ModelAdmin):
        if not 'view' in args:
            def has_view_permission(self, request: HttpRequest, *args, **kwargs):
                return not request.user.is_superuser
        if not 'add' in args:
            def has_add_permission(self, request: HttpRequest) -> bool:
                return not request.user.is_superuser
        if not 'change' in args:
            def has_change_permission(self, request: HttpRequest, *args, **kwargs) :
                return not request.user.is_superuser
        if not "module" in args:
            def has_module_permission(self, request: HttpRequest, *args, **kwargs) -> bool:
                return not request.user.is_superuser
        if not 'delete' in args:
            def has_delete_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
                return not request.user.is_superuser
    return CustomAdminModel
        

class AdminChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Admin

class AdminCreationForm(UserCreationForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        if "is_developer" in self.initial:
            self.initial['is_developer'] = False
 
    class Meta(UserCreationForm.Meta):
        model = Admin
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            Admin.objects.get(username=username)
        except Admin.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

class CustomUserAdmin(UserAdmin):
    form = AdminChangeForm
    add_form = AdminCreationForm

    def has_view_permission(self, request: HttpRequest, *args, **kwargs):
        return request.user.is_superuser
    
    def has_change_permission(self, request: HttpRequest, *args, **kwargs) :
        return request.user.is_superuser
    
    def has_module_permission(self, request: HttpRequest, *args, **kwargs) -> bool:
        return request.user.is_superuser
    
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        # (lazy("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            lazy("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )


class FeedbackAdminModel(ModelAdmin):
    def has_view_permission(self, request: HttpRequest, *args, **kwargs):
        return not request.user.is_superuser

    def has_module_permission(self, request: HttpRequest, *args, **kwargs) -> bool:
        return not request.user.is_superuser
    
    def has_delete_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        return not request.user.is_superuser
    
    list_display = ['email', 'title', 'created_at', 'phone']

my_site.register(HeaderNews, makeAdminModelWithout())
my_site.register(News,makeAdminModelWithout())
my_site.register(Feedback,FeedbackAdminModel)
my_site.register(Employee,makeAdminModelWithout())
my_site.register(Sponsor,makeAdminModelWithout())
my_site.register(Admin, CustomUserAdmin)
