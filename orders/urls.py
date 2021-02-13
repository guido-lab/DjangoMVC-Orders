from orders.models import Orders
from django.urls import path
from .views import (
OrderView, HomeListView, CreateOrdersView,
)

urlpatterns = [

    # -------------------------------
    path('', HomeListView.as_view(), name = 'orders-home'),
    path("orders/<int:pk>/", OrderView.as_view(), name = "orders-detail"),
    path('create_order/', CreateOrdersView.as_view(success_url='/'), name = 'create_entry'),

]
