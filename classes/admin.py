from django.contrib import admin

from classes import models

to_register = [
    models.Lecture,
    models.Slide,
]

admin.site.register(to_register)
