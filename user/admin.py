from django.contrib import admin
from .models import CustomUser
# Register your models here.
from .forms import CustomUserChangeForm,CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin


class CUstomUserAdmin(UserAdmin):
   add_form = CustomUserCreationForm
   form = CustomUserChangeForm
   model = CustomUser
   list_display = ['email', 'username', 'name']


admin.site.register(CustomUser,CUstomUserAdmin)


