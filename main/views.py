from django.shortcuts import render, get_object_or_404
from main.models import Article
from forms import EmailForm
from django.db.models import Q
from django.core.paginator import Paginator

def home(requests):
    form = EmailForm()
    if requests.method == "POST":
        form = EmailForm(requests.POST)
        if form.is_valid():
            form.save()
    query = requests.GET.get('q')
    if query:
        article = Article.objects.filter(Q(title__icontains=query))
    else:
        article = Article.objects.all()
    articles = Article.objects.order_by("-date")[:4]
    articles_2 = Article.objects.order_by("-date")[:6]
    articles_3 = Article.objects.order_by("-date")[:3]

    travel = Article.objects.filter(category="Travel")[:3]
    food = Article.objects.filter(category="Food")[:3]
    technology = Article.objects.filter(category="Technology")[:3]
    business = Article.objects.filter(category="Business")[:3]

    all_categories = Article.objects.values_list("category", flat=True)
    all_categories = list(set(all_categories))

    

    context = {
        'article': article,
        'form': form,
        'articles': articles,
        "art": articles_2,
        'artic': articles_3,
        'query': query,
        'travel': travel,
        'food': food,
        'technology': technology,
        'business': business,
        'all_categories': all_categories,
    }

    return render(requests, 'index.html', context=context)


def single(requests, pk):
    article = get_object_or_404(Article, pk=pk)
    all_categories = Article.objects.values_list("category", flat=True)
    all_categories = list(set(all_categories))
    articles_3 = Article.objects.filter(category=article.category)[:3]

    form = EmailForm()
    if requests.method == "POST":
        form = EmailForm(requests.POST)
        if form.is_valid():
            form.save()
    
    context = {
        'article': article,
        'form': form,
        'art': articles_3,
        'all_categories': all_categories,
        
    }
    return render(requests, 'single.html', context=context)



def category(requests):
    all_categories = Article.objects.values_list("category", flat=True)
    all_categories = list(set(all_categories))
    category = requests.GET.get("category")
    category_filter = Article.objects.filter(category=category)
    paginator = Paginator(category_filter, 3)
    page_number = requests.GET.get('page')
    page_obj = paginator.get_page(page_number)
    article = Article.objects.filter(category=category)[:3]
    form  = EmailForm()
    if requests.method == 'POST':
        form = EmailForm(requests.POST)
        if form.is_valid():
            form.save()

    context = {
        'article': article,
        'form':form,
        'category_filter': category_filter,
        'category': category,
        'all_categories': all_categories,
        'page_obj': page_obj,
    }
    return render(requests, 'categories.html', context=context)

def search_category(requests):
    all_categories = Article.objects.values_list("category", flat=True)
    all_categories = list(set(all_categories))
    category = requests.GET.get("category")
    category_filter = Article.objects.filter(category=category)
    
    form  = EmailForm()
    if requests.method == 'POST':
        form = EmailForm(requests.POST)
        if form.is_valid():
            form.save()
    query = requests.GET.get('q')
    if query:
        article = Article.objects.filter(title__icontains=query)
        paginator = Paginator(article, 3)
        page_number = requests.GET.get('page')
        page_obj = paginator.get_page(page_number)
    else:
        article = Article.objects.all()
        paginator = Paginator(article, 3)
        page_number = requests.GET.get('page')
        page_obj = paginator.get_page(page_number)

    context = {
        "query": query,
        'article': article,
        'form':form,
        'category_filter': category_filter,
        'category': category,
        'all_categories': all_categories,
        'page_obj': page_obj
    }
    return render(requests, 'search_article.html', context=context)