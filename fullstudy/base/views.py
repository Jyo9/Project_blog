from django.shortcuts import render


rooms=[
    {'id':1,'name':'Learn python'},
    {'id':2,'name':'Learn django'},
    {'id':3,'name':'Learn Flask'},
]
def home(request):
    return render(request,'home.html',{'rooms':rooms})

def room(request):
    return render(request,'room.html')

