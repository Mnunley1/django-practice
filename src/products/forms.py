from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Enter Title'}))
    email = forms.EmailField()
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'class': 'new-class-name two', 'rows': 20, 'cols': 120}))
    price = forms.DecimalField(initial=19.99)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not 'TRACK' in title:
            raise forms.ValidationError('This is not a valid title')
        else:
            return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith('edu'):
            raise forms.ValidationError('This is not a valid email')
        else:
            return email


class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Enter Title'}))
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'class': 'new-class-name two', 'rows': 20, 'cols': 120}))
    price = forms.DecimalField(initial=19.99)
