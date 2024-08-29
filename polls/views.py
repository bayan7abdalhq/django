from django.shortcuts import render, redirect
from .models import Author, Book
from .forms import AuthorForm, BookForm

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'polls/author_list.html', {'authors': authors})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'polls/book_list.html', {'books': books})

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'polls/add_author.html', {'form': form})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'polls/add_book.html', {'form': form})
