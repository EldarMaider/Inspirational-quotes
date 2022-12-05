from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns=[
    path('',views.all_quotes, name="all_quotes"),
    path('add_quote',views.add_quote,name='add_quote'),
    path('add_quote_action',views.add_quote_action,name='add_quote_action'),
    path('quote_details/<pk>',views.quote_details,name='quote_details'),
    path('delete_quote/<pk>',views.delete,name='delete'),
    path('edit_quote/<pk>',views.edit_quote,name='edit_quote'),
    path('search',views.search_quote,name='search_quote')
]