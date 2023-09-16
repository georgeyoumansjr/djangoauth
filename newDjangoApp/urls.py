# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, 'index'),
#     path('something2/', views.index, 'index'),
# ]
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('hello/', views.hello_view, name='hello'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('logout2/', views.user_logout2, name='logout'),
    path('register/', views.register, name='register'),
    # path('/dashboard', views.)
]