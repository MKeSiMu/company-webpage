from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

from webpage_app.models import Manufacturer, BearingType, BearingCategory, Purchaser


class ManufacturerForm(forms.ModelForm):
    PHONE_REGEX = r"\b[0-9]{11}\b"

    contact_phone = forms.CharField(
        required=True,
        validators=[RegexValidator(PHONE_REGEX)],
        error_messages={
            "invalid": "Contact phone number should have 11 digits"
        }
    )
    produce_bearing_type = forms.ModelMultipleChoiceField(
        queryset=BearingType.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Manufacturer
        fields = "__all__"


class ManufacturerPublicForm(forms.ModelForm):
    PHONE_REGEX = r"\b[0-9]{11}\b"

    contact_phone = forms.CharField(
        required=True,
        validators=[RegexValidator(PHONE_REGEX)],
        error_messages={
            "invalid": "Contact phone number should have 11 digits"
        }
    )
    produce_bearing_type = forms.ModelMultipleChoiceField(
        queryset=BearingType.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    captcha = CaptchaField()

    class Meta:
        model = Manufacturer
        fields = [
            "name",
            "address",
            "business_model",
            "contact_person",
            "contact_phone",
            "website",
            "produce_bearing_type"
        ]


class ManufacturerNameSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Enter manufacturer name for search...",
            "style": "width: 400px"
        })
    )


class BearingTypeNameSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Enter bearing type name for search...",
            "style": "width: 400px"
        })
    )


class PurchaserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Purchaser
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "is_staff",
            "is_superuser"
        )


class PurchaserUpdateForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Purchaser
        fields = [
            "username",
            "first_name",
            "last_name",
            "is_staff",
            "is_superuser"
        ]
