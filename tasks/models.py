from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator


class Task(models.Model):
    title = models.CharField(max_length=150,
                             validators=[MinLengthValidator(3, 'Title must be greater than 3 characters')])
    description = models.TextField(max_length=450)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks:task_detail', kwargs={'pk': self.pk})
