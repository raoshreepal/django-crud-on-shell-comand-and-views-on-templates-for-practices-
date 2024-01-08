from django.shortcuts import render, get_object_or_404
from .models import Book
from .forms import BookForm
from django.shortcuts import redirect

def hello(request):
	return render(request,"hello.html")
def display(request):
	b1=Book.objects.all()
	return render(request,"display.html",{"book":b1})
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display')  # 'display' URL name par redirect karna
    else:
        form = BookForm()
    return render(request, "add_book.html", {'form': form})
def  delete_book(request ,book_id):
	book=get_object_or_404(Book,pk=book_id)
	if request.method =='POST':
		book.delete()
		return redirect('display')
	return render(request,'delete_book.html',{'book':book})
def update_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('display')  # Redirect after successful update
    else:
        form = BookForm(instance=book)
    return render(request, 'update_book.html', {'form': form})
