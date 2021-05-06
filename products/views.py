from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product


#Class Based View
class ProductListView(ListView):
    model = Product
    template_name = "products/list.html"
    #traz todos os produtos do banco de dados sem filtrar nada
    queryset = Product.objects.all()
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/detail.html"

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Esse produto não existe!")
        return instance
