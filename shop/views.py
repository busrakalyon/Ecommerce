from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

from .models import Item
from .forms import SearchForm


def shop_all(request):
    items = Item.objects.all()
    return render(request, 'shop/itemview.html', {'items': items})


def beauty_category(request):
    items = Item.objects.filter(CategoryId=1)
    return render(request, 'shop/categoryview.html', {'items': items})


def clothing_category(request):
    items = Item.objects.filter(CategoryId=2)
    return render(request, 'shop/categoryview.html', {'items': items})


def jewelry_category(request):
    items = Item.objects.filter(CategoryId=3)
    return render(request, 'shop/categoryview.html', {'items': items})


def shoes_category(request):
    items = Item.objects.filter(CategoryId=4)
    return render(request, 'shop/categoryview.html', {'items': items})

def search(request):
    if request.POST:
        form = SearchForm(request.POST)

        if form.is_valid():
            search_terms = form.cleaned_data['search_phrase']
            split_search_terms = search_terms.split()

            items = set([])

            for search_term in split_search_terms:
                items = items.union(set(Item.objects.filter(Q(SearchTerm__icontains=search_term) | Q(ProductName__icontains=search_term))))

            return render(request, 'shop/itemview.html', {'items': items})
        else:
            return render(request, 'shop/itemview.html')