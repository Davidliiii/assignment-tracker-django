from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Assignment, Course, Tag
from .forms import AssignmentForm, CourseForm, TagForm


def assignment_list(request):
    assignments = Assignment.objects.all().order_by('due_date')
    courses = Course.objects.all().order_by('course_code')
    tags = Tag.objects.all().order_by('name')

    query = request.GET.get('q')
    status = request.GET.get('status')
    course_id = request.GET.get('course')
    tag_id = request.GET.get('tag')

    if query:
        assignments = assignments.filter(title__icontains=query)

    if status:
        assignments = assignments.filter(status=status)

    if course_id:
        assignments = assignments.filter(course_id=course_id)

    if tag_id:
        assignments = assignments.filter(tags__id=tag_id)

    today = timezone.now().date()

    total_assignments = Assignment.objects.count()
    completed_assignments = Assignment.objects.filter(status='Completed').count()
    in_progress_assignments = Assignment.objects.filter(status='In Progress').count()
    not_started_assignments = Assignment.objects.filter(status='Not Started').count()
    overdue_assignments = Assignment.objects.filter(due_date__lt=today).exclude(status='Completed')
    upcoming_assignments = Assignment.objects.filter(due_date__gte=today).exclude(status='Completed').order_by('due_date')[:5]

    context = {
        'assignments': assignments,
        'courses': courses,
        'tags': tags,
        'selected_query': query or '',
        'selected_status': status or '',
        'selected_course': course_id or '',
        'selected_tag': tag_id or '',
        'total_assignments': total_assignments,
        'completed_assignments': completed_assignments,
        'in_progress_assignments': in_progress_assignments,
        'not_started_assignments': not_started_assignments,
        'overdue_assignments': overdue_assignments,
        'upcoming_assignments': upcoming_assignments,
    }
    return render(request, 'core/assignment_list.html', context)


def assignment_create(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assignment_list')
    else:
        form = AssignmentForm()

    return render(request, 'core/assignment_form.html', {'form': form})


def assignment_update(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)

    if request.method == 'POST':
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('assignment_list')
    else:
        form = AssignmentForm(instance=assignment)

    return render(request, 'core/assignment_form.html', {'form': form})


def assignment_delete(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)

    if request.method == 'POST':
        assignment.delete()
        return redirect('assignment_list')

    return render(request, 'core/assignment_confirm_delete.html', {'assignment': assignment})


def course_list(request):
    courses = Course.objects.all().order_by('course_code')
    return render(request, 'core/course_list.html', {'courses': courses})


def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()

    return render(request, 'core/course_form.html', {'form': form})


def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)

    return render(request, 'core/course_form.html', {'form': form})


def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if request.method == 'POST':
        course.delete()
        return redirect('course_list')

    return render(request, 'core/course_confirm_delete.html', {'course': course})


def tag_list(request):
    tags = Tag.objects.all().order_by('name')
    return render(request, 'core/tag_list.html', {'tags': tags})


def tag_create(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tag_list')
    else:
        form = TagForm()

    return render(request, 'core/tag_form.html', {'form': form})


def tag_update(request, pk):
    tag = get_object_or_404(Tag, pk=pk)

    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('tag_list')
    else:
        form = TagForm(instance=tag)

    return render(request, 'core/tag_form.html', {'form': form})


def tag_delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk)

    if request.method == 'POST':
        tag.delete()
        return redirect('tag_list')

    return render(request, 'core/tag_confirm_delete.html', {'tag': tag})