from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def result(request):
    sentence = request.GET['sentence']

    wordList = sentence.split()
    
    wordDict = {}

    for word in wordList: 
        if word in wordDict:
            wordDict[word] += 1 # wordDict안에 단어가 있으면 1 증가
        else:                   #처음 나오는 단어이면
            wordDict[word] = 1  # 그 단어는 1로 초기화

    return render(request, 'result.html', {'fulltext':sentence, 'count':len(wordList), 'wordDict':wordDict.items})
    #result.html의 fulltext를 키 값으로, 값을 sentece로  / 
