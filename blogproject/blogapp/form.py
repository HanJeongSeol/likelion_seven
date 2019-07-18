# blogapp의 models.py에 정의한 BlogModel클래스를 기반으로 form을 구성하기 위해 blogapp폴더 안에 form.py를 생성하였다.

# django에서 기본으로 제공하는 forms 라이브러리 불러오기.
from django import forms
# models.py에서 클래서 가져오기
from .models import BlogModel

# form을 클래스로 정의, 모델 기반으로한 입력공간 만들기 위해 인자 값으로 forms.의 ModelForm을 준다.
# 모델 기반이 아닌 form을 생성하고 싶다면, forms.Form을 가져온다.
class BlogPost(forms.ModelForm):
    # Meta클래스 생성
    class Meta:
        # 어떤 모델을 기반으로 입력공간은 만들 것인지.
        model = BlogModel
        # 어떤 항목을 입력받을지 작성한 후 처리해줄 함수를 views.py에 정의한다/
        fields = ['title', 'body']


# 모델을 기반으로 하지 않는 form생성. 모델의 데이터 타입을 결정한 것과 같이 써준다.
# class BlogPost(forms.Form):
#     email = forms.EmailField()
#     files = forms.FileField()
#     url = forms.URLField()
#     words = forms.CharField(max_length=200)
#     max_number= forms.ChoiceField(choices=[('1','one'),('2','two'),('3','three')])