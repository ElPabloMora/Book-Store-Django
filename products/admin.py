from django.contrib import admin
from .models import Libro, Author, Comment

admin.site.register([Libro,Author,Comment ])
