from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content=models.TextField()
    thumbnail=models.URLField()
    post_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
