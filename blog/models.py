from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):  # means the Post is a Django model.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # link to another model
    title = models.CharField(max_length=200)  # limited number
    text = models.TextField()  # unlimited number
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
