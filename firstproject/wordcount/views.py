from django.shortcuts import render

# Create your views here.

def home(request) : 
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

# home.html에서 전송된 문장을 사용자가 원하는 데이터로 가공합니다.
def result(request): 
    full_text = request.GET['fulltext']     # fulltext로 설정한 textarea에 입력된 문장을 GET방식으로 받아와 full_text변수에 저장합니다.
    words = full_text.split()               # full_text에 저장된 문장을 띄어쓰기 기준으로 나누어 words에 리스트형으로 저장합니다.
    word_dictionary = {}                    # dictionary형 word_dictionary변수 선언
    for word in words :                     
        if word in word_dictionary:         
            word_dictionary[word] += 1      # words리스트를 하나씩 탐색하면서 word_dictionary에 key값으로 존재하면 value를 1씩 더해주고
        else:
            word_dictionary[word] = 1       # 존재하지 않는다면 key값의 value를 1로 저장합니다.
    # 가공된 데이터를 result로 전송합니다. full_text는 fulltext로 , words의 길이, 즉 총 단어 수는 total로, word_dictionary의 key-value값을 튜플로 묶어 dictionary라는 이름으로 반환한다.   
    return render(request,'result.html',{'fulltext':full_text, 'total' : len(words),'dictionary' : word_dictionary.items})
