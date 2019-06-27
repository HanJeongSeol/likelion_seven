from django.contrib import admin
from .models import modelapp      # 같은 폴더에 있는 models에서 modelapp 클래스를 가져온다.

admin.site.register(modelapp)       # addmin 사이트에 modelapp를 적용한다.