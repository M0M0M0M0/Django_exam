from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


def book_list(request):
    books = Book.objects.all().order_by('-created_at')
    total = books.count()
    return render(request, 'book_app/book_list.html', {'books': books, 'total': total})


def book_add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book_app/book_add.html', {'form': form})


def book_expensive(request):
    books = Book.objects.filter(price__gt=100).order_by('price')
    return render(request, 'book_app/book_expensive.html', {'books': books})