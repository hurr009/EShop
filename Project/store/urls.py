from django.urls import path
from django.views.generic import TemplateView, ListView


from . import views
from .models import item, category


urlpatterns = [
    path('Cart/', views.CartView.as_view(), name='cart'),
    path('Detail/<int:pk>', views.ItemDetailView.as_view(), name='detail'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('<str:category_id>/', views.StoreListView.as_view(), name='store'),
]
