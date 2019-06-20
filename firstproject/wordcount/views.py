from django.shortcuts import render

# Create your views here.

def home(request) : 
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def result(request): 
    full_text = request.GET['fulltext']
    words = full_text.split()
    word_dictionary = {}
    for word in words : 
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    return render(request,'result.html',{'fulltext':full_text, 'total' : len(words),'dictionary' : word_dictionary.items})