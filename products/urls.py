from django.contrib import admin
from django.urls import path
from .views import index, show_author, show_product, add_new_comment


urlpatterns = [
    path('', index, name = 'index'),
    path('author/<int:id>', show_author, name='show_author'),
    path('product/<int:id>', show_product, name='show_product'),
    path('product/<int:id>/add_new_comment', add_new_comment, name='add_new_comment')
    
]
