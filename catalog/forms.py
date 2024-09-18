from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    forbidden_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция",
                       "радар"]

    class Meta:
        model = Product
        exclude = ('views_counter', )

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
    model = Version
    fields = '__all__'

    def clean_is_active(self):
        product = Product.objects.get(product_name="Продукт")
        versions = product.version_set.all()
        cleaned_data = self.cleaned_data["is_active"]
        for active_version in versions:
            if active_version.is_active and cleaned_data:
                raise ValidationError('Не может быть несколько актуальных версий')
        return cleaned_data
