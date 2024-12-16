
from django.shortcuts import render
from django.views.generic import View

from .utils import  get_client_data, yelp_search


class IndexView(View):
    def get(self, request, *args, **Kwargs):
        items =[]

        city = None

        while not city:
            ret = get_client_data()
            city = ret['city']

        q = request.GET.get('key', None)
        loc = request.GET.get('loc', None)
        location = city

        context = {
            'city': city,
            'busca': False
        }

        if loc:
            location = loc
        if q:
            items = yelp_search(keyword=q, location=location)
            context = {
                'items': items,
                'city': location,
                'buscar': True

            }
        return  render(request, 'index.html', context)