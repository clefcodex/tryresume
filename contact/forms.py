# from django import forms
from .models import Contact

class BookForm(forms.Form):
	title = forms.CharField(label='Title', max_length=120)
	author = forms.CharField(label='Author', max_length=120)
	isbn = forms.CharField(label='Isbn', max_length=120)


# # The name should BookForm instead of ModelBookForm
# # But since BookForm is already taking
# class ModelBookForm(forms.ModelForm):
# 	class Meta:
# 		model = Book
# 		fields = ['title', 'author', 'isbn']

