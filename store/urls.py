from django.urls import path

from . import views

urlpatterns = [
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
    path('about/', views.about, name='about'), 
    path('login/', views.store_login, name='store_login'),
    path('logout/', views.store_logout, name='store_logout'),
    path('courses/python', views.python, name='python'), 
    path('courses/rust', views.rust, name='rust'), 
    path('courses/ruby', views.ruby, name='ruby'), 
    path('courses/data_science', views.data_science, name='data_science'), 
    path('courses/c', views.c, name='c'), 
    path('courses/agile', views.agile, name='agile'), 
    path('finish/', views.finish, name='finalizar'), 

]