from django.db import models

<<<<<<< HEAD
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title} by {self.author}"
=======
# Create your models here.
>>>>>>> 146de713437321d0f343a53201206dd113c6ee78
