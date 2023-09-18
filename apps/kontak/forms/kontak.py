from django import forms

from ..models.kontak import Kontak as KontakModel


class Kontak(forms.ModelForm):
    class Meta:
        model = KontakModel
        fields = [
            "nama",
            "email",
            "gender",
            "phone",
            "alamat",
        ]
