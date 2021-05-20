from django.db import models

PRIORITY = (("secondary", "low"), ("info", "normal"), ("danger", "high"))


class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(max_length=50, choices=PRIORITY)
    duedate = models.DateField()
