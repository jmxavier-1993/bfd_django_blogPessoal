from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('login/', views.login_view, name='login'),
    # O nome 'account_logout' é o que você usou no seu base.html
    path('logout/', views.logout_view, name='account_logout'), 
]