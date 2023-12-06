from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

__project_by__ = "RajeshKumar"


class Todo(models.Model):
    STATUS = (("Pending", "Pending"), ("Completed", "Completed"))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, choices=STATUS, default="Pending")

    @property
    def formatted_created_at(self):
        return self.created_at.strftime("%d-%b-%y %I:%M%p")

    @property
    def formatted_updated_at(self):
        return self.updated_at.strftime("%d-%b-%y %I:%M%p")

    @property
    def time_ago_created_at(self):
        delta = timezone.now() - self.created_at
        if delta < timezone.timedelta(minutes=1):
            return "Just Now"
        elif delta < timezone.timedelta(hours=1):
            return f"{int(delta.seconds/60)} mins ago"
        elif self.created_at.date() == timezone.now().date():
            return "Today"
        elif (
            self.created_at.date()
            == (timezone.now() - timezone.timedelta(days=1)).date()
        ):
            return "Yesterday"
        elif self.created_at.year == timezone.now().year:
            return self.created_at.strftime("%d-%b")
        else:
            return self.created_at.strftime("%d-%b-%Y")

    @property
    def time_ago_updated_at(self):
        delta = timezone.now() - self.updated_at
        if delta < timezone.timedelta(minutes=1):
            return "Just Now"
        elif delta < timezone.timedelta(hours=1):
            return f"{int(delta.seconds/60)} mins ago"
        elif self.updated_at.date() == timezone.now().date():
            return "Today"
        elif (
            self.updated_at.date()
            == (timezone.now() - timezone.timedelta(days=1)).date()
        ):
            return "Yesterday"
        elif self.updated_at.year == timezone.now().year:
            return self.updated_at.strftime("%d-%b")
        else:
            return self.updated_at.strftime("%d-%b-%Y")

    def __str__(self):
        return self.title
