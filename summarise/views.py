from django.shortcuts import render
from gensim.summarization import summarize
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')

def summarising(request):
    text = request.POST["textsum"]
    textlength = len(text.split())
    wc = int(textlength/3)
    pdy = summarize(text,word_count=wc)
    return render(request,'result.html',{'sumtext' : pdy})
