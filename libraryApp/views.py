from django.shortcuts import render
from .models import book
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def addBook(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        year = request.POST.get('year')

        mybook = book(title=title, author=author, description=description, year=year)
        mybook.save()

        return HttpResponse("Book saved Successfully")
    else:
        return HttpResponse("Wrong method used")


    
