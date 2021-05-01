from django.shortcuts import render, redirect
from .models import Author, Book

def books(request):
    ctx={
        "all_books": Book.objects.all()
    }
    return render(request, 'books.html', ctx)

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

def add_auth_to_book(request,book_id):
    if request.POST['auth_id']:
        this_book = Book.objects.get(id=book_id)
        this_author = Author.objects.get(id=request.POST['auth_id'])
        this_book.authors.add(this_author)
    return redirect("/books/"+book_id)

def authors(request):
    ctx = {
        "all_authors": Author.objects.all()
    }
    return render(request, "authors.html", ctx)

def add_author(request):
    if request.POST['fname'] and request.POST['lname'] and request.POST['notes']:
        Author.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], notes=request.POST['notes'])
    return redirect('/authors')

def view_author(request, author_id):
    this_author = Author.objects.get(id=author_id)
    associate_books = this_author.books.all()
    non_associate_books = Book.objects.exclude(authors=this_author)
    ctx = {
        "this_author": this_author,
        "associate_books":associate_books,
        "non_associate_books": non_associate_books
    }
    return render(request, "author.html", ctx)

def add_book_to_auth(request,author_id):
    if request.POST['book_id']:
        this_author = Author.objects.get(id=author_id)
        this_book = Book.objects.get(id=request.POST['book_id'])
        this_author.books.add(this_book)
    return redirect('/authors/'+author_id)