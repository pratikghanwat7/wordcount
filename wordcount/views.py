from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html',{'hi': '12' })
def count(request):
    fulltext = request.GET['fulltext']
    print(fulltext)
    wordlist = fulltext.split()

    worddic = {}
    for word in wordlist:
        if word in worddic:
            worddic[word] += 1
        else:
            worddic[word] = 1
    maxv = 0
    for word in worddic:
        if maxv < worddic[word]:
            maxv = worddic[word]
    sortedic = sorted(worddic.items(),key=operator.itemgetter(1), reverse = True)


    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedic':sortedic,'max':maxv})