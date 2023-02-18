from django.shortcuts import render;
from django.http import HttpResponse

# Create your views here.
def f11(hi):
    return HttpResponse('<h1> HELLO MADAM UNARA</h1><hr/>')
def f22(hi):
    return HttpResponse('<h1> DP PETUKOVACHU GA PLZ😊</h1><hr>')
    
def homepage(request):
    htmldata='''<center>
        <h1>Welcome to DEFAULT Home-Page!!!</h1>
        <hr />
        <h2>Your Request Page is Not-Found...</h2>
        <hr />
        <h3>Plz try other URL or Links!!!</h3>
    </center>''';
    return HttpResponse(htmldata);
    