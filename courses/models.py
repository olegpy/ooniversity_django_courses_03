from django.db import models
from django.core.urlresolvers import reverse_lazy

from coaches.models import Coach


class Course(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    coach = models.ForeignKey(
        Coach, null=True, blank=True, related_name='coach_courses')
    assistant = models.ForeignKey(
        Coach, null=True, blank=True, related_name='assistant_courses')

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    subject = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()

    # def get_url(self):
    #     return reverse_lazy('courses:detail', args=(self.course.id))

    def get_url(self):
        return reverse_lazy('courses:detail', args=[self.course.id])

    def __unicode__(self):
        return self.subject
