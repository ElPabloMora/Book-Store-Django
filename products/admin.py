from django.contrib import admin
from .models import Libro, Author, Comment, Carrito

admin.site.register([Libro,Author,Comment, Carrito])
