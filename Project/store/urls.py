from django.urls import path
from django.views.generic import TemplateView, ListView


from . import views
from .models import item, category


urlpatterns = [
    path('Cart/', views.CartView.as_view(), name='cart'),
    path('StripeCheckout/', views.StripeCheckoutView.as_view(), name='stripecheckout'),
    path('Checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('Detail/<int:pk>', views.ItemDetailView.as_view(), name='detail'),
    path('Orders/', views.OrderListView.as_view(), name='orders'),
    path('<str:category_id>/', views.StoreListView.as_view(), name='store'),
]
