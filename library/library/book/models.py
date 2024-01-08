from django.db import models
from django.utils import timezone

class Book(models.Model):
	book_title=models.CharField(max_length=100)
	author_name=models.CharField(max_length=100)
	price=models.DecimalField(max_digits=10,decimal_places=2)
	publish_date=models.DateTimeField(default=timezone.now())
	def __str__(self):
		return self.book_title
# Create your models here.
