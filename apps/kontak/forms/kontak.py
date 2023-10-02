from django import forms

from ..models.kontak import Kontak as KontakModel


class Kontak(forms.ModelForm):
    class Meta:
        model = KontakModel
        fields = "__all__"
        widgets = {
            "nama": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "autofocus": "autofocus"
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "gender": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),
            "phone": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "type": "tel",
                }
            ),
            "alamat": forms.Textarea(
                attrs={
                    "class": "form-control"
                }
            ),
        }
