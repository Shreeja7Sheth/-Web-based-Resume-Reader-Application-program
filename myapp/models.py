from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(('email address'), unique=True)
    resume = models.FileField(upload_to='files/docs/')
    objects = models.Manager()
    def __str__(self):
        return self.username
