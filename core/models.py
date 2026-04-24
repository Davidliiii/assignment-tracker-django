from django.db import models


class Course(models.Model):
    course_code = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.course_code} - {self.course_name}"


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Assignment(models.Model):
    STATUS_CHOICES = [
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Not Started')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
    tags = models.ManyToManyField(Tag, blank=True, related_name='assignments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title