from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    data={
        "context":"where is the data"
    }
    return render(request,"index.html")


