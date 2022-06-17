from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

# Creating Post
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    text = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title

