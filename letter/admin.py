from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Letter


# Register your models here.
@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = ('user','title', 'email_address', 'delivered')
    list_filter = ('audience',)


