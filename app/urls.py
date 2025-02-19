from django.urls import path
from app import views


urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('update/<int:pk>',views.update,name='update'),
    # path('update/<int:pk>',views.update,name='update')
]