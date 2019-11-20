from django.urls import path
from user import views

app_name = 'user'
urlpatterns = [
    path('manage/', views.to_manage_page, name='manage'),
    path('manage_render/', views.manage_handler, name='manage_render'),
    path('update_render/', views.update_handler, name='update_render'),
    path('user_add/', views.to_add_page, name='add'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]