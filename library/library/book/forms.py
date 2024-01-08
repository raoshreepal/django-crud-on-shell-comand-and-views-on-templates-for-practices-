from django import forms
from .models import Book

class BookForm(forms.ModelForm):
	class Meta:
		model=Book
		fields=["book_title","author_name","price","publish_date"]


	# book_title=models.CharField(max_length=100)
	# author_name=models.CharField(max_length=100)
	# price=models.DecimalField(max_digits=10,decimal_places=2)
	# # publish_date=models.DateTimeField(default=timezone.now