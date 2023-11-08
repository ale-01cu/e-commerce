from django import forms
from .models import Product
from django_svg_image_form_field import SvgAndImageFormField


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        exclude=[]
        field_classes={
            'photo': SvgAndImageFormField
        }