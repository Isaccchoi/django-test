from django import forms


class PostCreateForm(forms.Form):
    title = forms.CharField(max_length=50)
    photo = forms.ImageField()
    content = forms.CharField(max_length=100)
