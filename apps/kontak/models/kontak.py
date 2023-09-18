from enum import Enum

from django.db import models


class Kontak(models.Model):
    GENDER = (
        ("Pria", "Pria"),
        ("Wanita", "Wanita"),
    )

    nama = models.CharField(max_length=45)
    email = models.EmailField(max_length=225, unique=True)
    gender = models.CharField(max_length=9, choices=GENDER, default="Pria")
    phone = models.CharField(max_length=20)
    alamat = models.TextField()
