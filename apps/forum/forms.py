from django import forms

from .models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text', 'category']
        labels = {'text':'Topic'}

    def __init__(self, *args, **kwargs):
         super(TopicForm, self).__init__(*args, **kwargs)
         self.fields['category'].queryset = Category.objects.all()

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'text']
        labels = {'text': 'Entry', 'title' : 'Title'}
        widgets = {'text':forms.Textarea(attrs={'cols':80, 'class':'entry', 'id':'txtContent'})}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']
        labels = {'text': 'Comment'}
        widgets = {'text':forms.Textarea(attrs={'cols':80, 'class':'entry', 'id':'txtContent'})}
