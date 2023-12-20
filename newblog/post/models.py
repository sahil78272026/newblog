from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        db_table = "Post"

class NewsLetter(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(null=True, blank=True)
    email_sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

