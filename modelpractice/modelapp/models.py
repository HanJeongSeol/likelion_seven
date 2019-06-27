from django.db import models

# Create your models here.

class modelapp(models.Model):                           # 클래스 명은 우리가 생성한 app이름과 동일하다.
    title = models.CharField(max_length=200)            # 문자열을 받을 때 최대 길이가 200일 것 까지 가능하다.
    pub_date = models.DateTimeField('data published')   # 날짜와 시간을 나타내는 데이터를 pub_data에 나타낸다.
    body = models.TextField()                           # charfield보다 긴 문자열을 받을 수 있다.

    def __str__(self):          # 페이지의 admin으로 들어가서 저장한 데이터 확인 시 title이 제목으로 나올 수 있도록 해준다,
        return self.title