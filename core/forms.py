from django import forms
from .models import Assignment, Course, Tag


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date', 'status', 'course', 'tags']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'tags': forms.CheckboxSelectMultiple(),
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_code', 'course_name', 'instructor']


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']