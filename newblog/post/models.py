from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        db_table = "Post"
