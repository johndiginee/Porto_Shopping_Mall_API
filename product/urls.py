from django.urls import path
from . import views


urlpatterns = [
    path('all/', views.get_products, name="products"),
    path('new/', views.new_product, name="new_product"),
    path('upload_images/', views.upload_product_images, name="upload_product_images"),
    path('<str:pk>/', views.get_product, name="get_product_details"),
    path('<str:pk>/update/', views.update_product, name="update_product"),
    path('<str:pk>/delete/', views.delete_product, name="delete_product"),

    path('<str:pk>/reviews/', views.create_review, name="create_update_review"),
    path('<str:pk>/reviews/delete/', views.delete_review, name="delete_review"),
]