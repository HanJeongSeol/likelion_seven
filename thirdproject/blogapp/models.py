from django.db import models

# Create your models here.

class blogapp(models.Model) :
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()

    def __str__(self):
        return self.title