from django.shortcuts import render, get_object_or_404
from .models import Category, Option



# Create your views here.

def option_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    options = Option.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category,
                                     slug = category_slug)
        options = options.filter(category=category)
    return render(request,
                    'restaurant/option/list.html',
                    {'category': category,
                    'categories': categories,
                    'options':options})
    

def option_detail(request, id, slug):
    option = get_object_or_404(Option,
                               id=id,
                               slug=slug,
                               available =True)
    return render(request,
                  'restaurant/option/detail.html',
                  {'option': option})



                      