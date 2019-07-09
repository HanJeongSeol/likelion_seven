from django.db import models

# Create your models here.

class blogapp(models.Model) :
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]          # 사용자에게 글자수를 100자로 제한해서 보여준다.

    