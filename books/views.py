from django.shortcuts import render,redirect
from books.models import Books,Tasks
from books.forms import BooksCreate,TasksCreate,TaskList
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'books/home.html')

def index(request):
    shelf = Books.objects.all()
    return render(request,'books/library.html',{'shelf':shelf})
def index1(request):
    shelf1 = Tasks.objects.all()
    return render(request,'books/library.html',{'shelf1':shelf1})
def upload(request):
    upload = BooksCreate()
    if request.method == 'POST':
        upload = BooksCreate(request.POST,request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse('Your form is wrong')
    else:
        return render(request,'books/new_project.html',{'upload_form':upload})
def upload1(request):
    upload1 = TasksCreate()
    if request.method == 'POST':
        upload1 = TasksCreate(request.POST,request.FILES)
        if upload1.is_valid():
            upload1.save()
            return redirect('index1')
        else:
            return HttpResponse('Your form is wrong')
    else:
        return render(request,'books/new_task.html',{'upload_form':upload1})
def update_book(request,book_id):
    book_id = int(book_id)
    try:
        book_sel = Books.objects.get(id=book_id)
    except Books.DoesNotExist:
        return redirect('index')
    book_form = BooksCreate(request.POST or None,instance=book_sel)
    if book_form.is_valid():
        book_form.save()
        return redirect('index')
    return render(request,'books/new_project.html',{'upload_form':book_form})

def update_book1(request,book_id):
    book_id = int(book_id)
    try:
        book_sel = Books.objects.get(id=book_id)
    except Books.DoesNotExist:
        return redirect('index1')
    book_form1 = BooksCreate(request.POST or None,instance=book_sel)
    if book_form1.is_valid():
        book_form1.save()
        return redirect('index1')
    return render(request,'books/new_task.html',{'upload_form':book_form1})
 
def delete(request,book_id):
    book_id = int(book_id)
    try:
        book_sel = Books.objects.get(id=book_id)
    except Books.DoesNotExist:
        return redirect('index')
    book_sel.delete()
    return redirect('index')