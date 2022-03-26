from django import forms

from .models import Contact, Post


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'body')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')
