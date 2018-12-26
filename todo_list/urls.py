from django.contrib import admin
from django.urls import path
from .views import home,delete,cross_off,un_cross,edit

urlpatterns = [
    path('', home ,name='todo-list'),
    path('delete/<list_id>', delete ,name='todo-delete'),
    path('cross_off/<list_id>', cross_off ,name='cross_off'),
    path('un_cross/<list_id>', un_cross ,name='un_cross'),
    path('edit/<list_id>', edit ,name='edit'),
    
]