from django.urls import path
from . import views

app_name = 'libra'
urlpatterns=[
    path('addBook/',views.addBook,name='addBook'),
    path('delBook/<int:book_id>', views.deleteBook, name='delBook'),
    path('updateBook/',views.updateBook, name='updateBook'),
    path('detail/', views.detail, name='detail'),
    path('', views.index, name='index'),
]