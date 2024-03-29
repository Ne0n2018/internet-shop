from django.views.generic import ListView, DetailView

from .models import Product


class ProductList(ListView):
    model = Product
    template_name = "index.html"
    context_object_name = 'products'
    poginate_by = 2


class ProductDetails(DetailView):
    model = Product
    template_name = "product.html"
    context_object_name = 'product'
