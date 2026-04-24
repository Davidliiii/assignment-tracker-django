from django.contrib import admin
from .models import Course, Tag, Assignment


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'course_name', 'instructor')
    search_fields = ('course_code', 'course_name', 'instructor')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'due_date', 'status', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('status', 'due_date', 'course', 'tags')