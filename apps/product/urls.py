from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductsListView.as_view(), name='products_list_view'),
    path('products/<int:product_id>/<product_name>', views.ProductDetailView.as_view(), name='product_detail_view')

]
