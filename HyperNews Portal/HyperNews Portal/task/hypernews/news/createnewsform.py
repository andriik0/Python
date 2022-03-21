from django import forms

class NewsForm(forms.Form):
    created = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M:%S', ])
    title = forms.CharField(max_length=512, min_length=10)
    text = forms.CharField(max_length=512)