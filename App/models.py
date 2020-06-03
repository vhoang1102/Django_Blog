from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    publish_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.publish_date.save()

    def approve_comments(self):
        return self.comments.filter(approve_comments=True)

    def get_absolute_url(self):
        return reverse('post_details', kwargs={'pk': self.pk})

    def __str_(self):
        return self.title


class Comments(models.Model):
    post = models.ForeignKey('App.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve_comments(self):
        self.approved_comment = True
        self.approved_comment.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str_(self):
        return self.text
