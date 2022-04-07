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
            "currentprice",
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

        placeholders = {
            'category': 'Category',
            'category2': 'Sale or New Arrival?',
            'sku': 'SKU',
            'name': 'Name',
            'description': 'Description',
            'price': 'Original Price',
            'currentprice': 'Current Price',
            'rating': 'Rating',
            'image_url': 'Image URL',
            'image': 'Image',
            'width': 'Width',
            'height': 'Height',
            'depth': 'Depth',
        }

        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False