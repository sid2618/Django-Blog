from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:pk>', views.post, name='post'),
    path('addpost', views.addpost, name='addpost'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('search', views.search, name='search'),
    path('signup', views.signup, name='signup'),
    path('login', views.login_view, name='login_view'),
    path('logout', views.logout_view, name='logout_view'),
]