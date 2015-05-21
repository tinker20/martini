from django.views.generic import ListView
from django.utils import timezone

from store.models import Store
from product.models import Product, StoreCatalog

class IndexListView(ListView):
    model = Store

    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class StoreDetailListView(ListView):
	model = Product
	template_name = "store/store_detail.html"
	context_object_name = 'products'

	def get_context_data(self, **kwargs):
	    context = super(StoreDetailListView, self).get_context_data(**kwargs)
	    store_name = Store.objects.get(id = self.kwargs['pk'])
	    context['store_name'] = store_name
	    return context


	def get_queryset(self):
            pk = self.kwargs['pk']
            current_store = Store.objects.filter(id=pk)
            product_pks = [store_catalog.product.id for store_catalog in StoreCatalog.objects.filter(store=current_store)]
            products = Product.objects.filter(pk__in=product_pks).order_by('category__name', 'name')

            for i, current_product in enumerate(products):
                store_catalog = StoreCatalog.objects.get(store=current_store, product=current_product)
                products[i].price = store_catalog.price

            return products

