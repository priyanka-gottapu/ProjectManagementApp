from django import forms
from books.models import Books,Tasks,TaskList

class BooksCreate(forms.ModelForm):
    class Meta:
        model = Books
        fields = "__all__"

class TasksCreate(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = "__all__"

class TaskList(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = "__all__"