from django.shortcuts import render
from django.http import HttpResponse
import requests

API_KEY='ebf5dfbf8a0746c981fda70acb7ecc25'


# Create your views here.
def home(request):
    country= request.GET.get('country')
    search=request.GET.get('search')
    category=request.GET.get('category')

    condic = {'INDIA' : 'in',
                   'JAPAN': 'jp',
                   'AUSTRALIA': 'au',
                   'US': 'us',
                   'UNITED STATES': 'us',
                   'CHINA': 'cn',
                   'NEW ZEALAND': 'nz',
                   'CANADA': 'ca',
                   'UKRAINE': 'ua',
                    'RUSSIA': 'ru',
                   }
    if country:
        c_name = country.upper()
        val=""
        if c_name in condic.keys():
            val=condic[c_name]

            url=f'https://newsapi.org/v2/top-headlines?country={val}&apiKey={API_KEY}'
            response = requests.get(url)
            data = response.json()
            articles= data['articles']
        else:
            url=f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
            response = requests.get(url)
            data = response.json()
            articles= data['articles']

    elif search:
        url=f'https://newsapi.org/v2/everything?q={search}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles= data['articles']
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey=ebf5dfbf8a0746c981fda70acb7ecc25'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']


    context= {
        'articles': articles
    }
    return render(request, 'home.html', context)
