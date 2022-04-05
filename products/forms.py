from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            "category",
            "category2",
            "sku",
            "name",
            "description",
            "price",
            "current_price",
            "rating",
            "image_url",
            "image",
            "width",
            "height",
            "depth",
        ]

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        website_names = [(c.id, c.get_website_name()) for c in categories]

        self.fields['category'].choices = website_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'

