from django.contrib import admin
from django.urls import path
from .views import index, show_author, show_product, add_new_comment, delete_comment, edit_comment,ver_carrito
from .views import add_carrito, actualizar_cantidad, eliminar_carrito, show_genero, show_filter

urlpatterns = [
    path('', index, name = 'index'),
    path('author/<int:id>', show_author, name='show_author'),
    path('product/<int:id>', show_product, name='show_product'),
    path('product/<int:id>/add_new_comment', add_new_comment, name='add_new_comment'),
    path('product/<int:id_comment>/<int:id_libro>/delete', delete_comment, name='delete_comment'),
    path('product/<int:id_comment>/<int:id_libro>/edit', edit_comment, name='edit_comment'),
    path('shopping_cart/<int:id>', add_carrito, name='add_carrito'),
    path('shopping_cart/', ver_carrito, name='ver_carrito'),
    path('shopping_cart/actualizar/<int:id>', actualizar_cantidad, name='actualizar_cantidad'),
    path('shopping_cart/eliminar/<int:id>', eliminar_carrito, name='eliminar_carrito'),
    path('showGenero/<str:Genero>', show_genero, name='show_genero'),
    path('showGenero/<str:Genero>/filter/<int:min>/<int:max>', show_filter, name='show_filter'),
]
