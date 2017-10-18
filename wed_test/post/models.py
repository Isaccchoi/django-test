from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='post')
    content = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
