from django.shortcuts import render, redirect
from .models import Author, Book

def books(request):
    data={
        "all_books": Book.objects.all()
    }
    return render(request, 'books.html', data)

def add_book(request):
    if request.POST['title'] and request.POST['desc']:
        Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
    return redirect('/')

def view_book(request, book_id):
    this_book = Book.objects.get(id=book_id)
    associate_author = this_book.authors.all()
    non_associate_author = Author.objects.exclude(books=this_book)
    ctx ={
        'this_book': this_book,
        'associate_author': associate_author,
        'non_associate_author': non_associate_author
    }
    return render(request, "book.html", ctx)