from django.urls import path
from .import views


app_name = 'Topshop'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
    path('categories/', views.CategoriesView.as_view(), name='categories'),
    path('subcategory/<int:pk>/', views.SubcategoriesView.as_view(), name='subcategories'),
    path('subcategory/<int:pk>/products/', views.ProductsView.as_view(), name='products'),
    path('subcategory/<int:pk>/products/new/', views.CreateProductView.as_view(), name='create_products'),
    path('subcategory/<int:pk>/products/update/', views.UpdateProductView.as_view(), name='update_products'),
    path('subcategory/<int:pk>/products/delete/', views.DeleteProductView.as_view(), name='delete_products'),
    path('letters/reciever/', views.IndexRecieverLetterView.as_view(), name='reciever_letters'),
    path('letters/sender/', views.IndexSenderLetterView.as_view(), name='sender_letters'),
    path('letters/<int:pk>/', views.DetailLetterView.as_view(), name='letter_details'),
    path('letters/new/', views.CreateLetterView.as_view(), name='create_letters'),
    path('letters/<int:pk>/update/', views.UpdateLetterView.as_view(), name='update_letters'),
    path('letters/<int:pk>/delete/', views.DeleteLetterView.as_view(), name='delete_letters'),
    path('profile/<int:user_id>/update_profile>', views.UpdateProfileView.as_view(), name='update_profile'),
	]