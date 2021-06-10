from frontend.models import Partner, Product, Skill, TeamMember
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):
    products = Product.objects.all()
    latest_products = products[:6]
    return render(request, 'frontend/index.html', {'latest_products': latest_products})

def products(request):
    products_list = Product.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(products_list, 6)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'frontend/products.html', {'products': products})

def about(request):
    partners = Partner.objects.all()
    skills = Skill.objects.all()
    team_members = TeamMember.objects.all()
    return render(request, 'frontend/about.html', {'team_members': team_members, 'skills': skills, 'partners': partners})

def contact(request):
    return render(request, 'frontend/contact.html', {})