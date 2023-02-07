from django import forms
from .models import Book, Comment

class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'body', 'author', 'publisher', 'photo']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']        