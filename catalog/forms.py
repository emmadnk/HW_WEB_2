from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            else:
                fild.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    forbidden_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция",
                       "радар"]

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price', 'created_at', 'updated_at', 'is_published')

    def clean_product_name(self):
        cleaned_data = self.cleaned_data["product_name"]
        for word in self.forbidden_words:
            if word in cleaned_data.lower():
                raise ValidationError(f"слово '{word}' нельзя использовать в названии")
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data["description"]
        for word in self.forbidden_words:
            if word in cleaned_data.lower():
                raise ValidationError(f"слово '{word}' нельзя использовать в описании")
        return cleaned_data


class VersionForm(StyleFormMixin, ModelForm):

    class Meta:
        model = Version
        fields = '__all__'


