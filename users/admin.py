from django.contrib import admin
from main.models import Course
from .models import *

# Register your models here.


class IMUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'user_type', 'is_active', 'date_created')
    list_filter = ('user_type', 'is_active')
    search_fields = ('first_name', 'last_name')

class CohortAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'is_active', 'author', 'start_date', 'end_date')
    list_filter = ('year', 'is_active')
    search_fields = ('name', 'description')
    raw_id_fields = ('author',)

class CohortMemberAdmin(admin.ModelAdmin):
    list_display = ('member', 'cohort', 'is_active', 'author', 'date_created')
    list_filter = ('is_active',)
    search_fields = ('member__first_name', 'member__last_name', 'cohort__name')
    raw_id_fields = ('member', 'cohort', 'author')

# Register the models with the admin and specify the custom ModelAdmin classes
admin.site.register(IMUser, IMUserAdmin)
admin.site.register(Cohort, CohortAdmin)
admin.site.register(CohortMember, CohortMemberAdmin)





