
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .news_websites import get_websites,get_links
from .uNPW import insert_new,get_login
from django.urls import resolve
class Stack(object):
    def __init__(self):
        self.items=[]
    def push(self,item=''):
        self.items.append(item)
    def pop (self):
        return self.items.pop()
        pass
    def clear(self):
        self.items=[]
link="http://127.0.0.1:8000/"
stack=Stack()




def get_data(name):
    return name.lower()

def home(request):
    return HttpResponse('<h1>Blog home</h1>')
def about(request):

    context={

    }
    get_websites(context,"bbc_news")

    context_s={

    }
    stack.clear()
    n="web_address.html"
    stack.push(n)
    get_websites(context_s, "bbc_news")
    get_links(context, "bbc_news")

    return render(request,"web_address.html",{'first':context,'second':context_s})

def send(request):
    stack.push("practice.html")
    return render(request,"practice.html")

def create_account(request):
    return render(request,"createAccount.html")
def submit(request):

    username=request.GET['Uname']
    password=request.GET['Pword']
    insert_new(username,password)
    return render(request,"createAccount.html")
def login(request):
    userNameAttempt=request.POST.get('Fname', False)
    passwordAttempt=request.POST.get('lname', False)

    if get_login(userNameAttempt,passwordAttempt)==True:

        return redirect("http://127.0.0.1:8000/homeabout/")
    else:
        return render(request,"practice.html")

def URLview(request):
    return HttpResponseRedirect("http://127.0.0.1:8000/homeabout/")