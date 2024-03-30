from django.urls import path
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('', views.option_list, name = 'option_list'),
    path('<slug:category_slug>/', views.option_list, name = 'option_list_by_category'),
    path('<int:id>/<slug:slug>/', views.option_detail, name='option_detail'),
]

