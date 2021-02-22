from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Items, Orders


class OrderView(LoginRequiredMixin, DetailView):
    model = Orders
    template_name = 'orders/order_detail.html'

class HomeListView(LoginRequiredMixin, ListView):
    model = Orders
    template_name = 'orders/index.html'
    context_object_name = 'blog_entries_copy'
    ordering = ['-created_at']
    paginate_by = 3

class CreateOrdersView(LoginRequiredMixin, CreateView):
    model = Orders
    template_name = 'orders/create_order_view.html'
    fields = ['title', 'description', 'item', 'quantity']

    def form_valid(self,form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class CreateItemsView(LoginRequiredMixin, CreateView):
    model = Items
    template_name = 'orders/create_item_view.html'
    fields = ['name', 'description', 'price']

    def form_valid(self,form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
