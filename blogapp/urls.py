from django.urls import path
from . import views

app_name = 'blogapp'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('<slug:article>/', views.article_full, name='article_full'),
]