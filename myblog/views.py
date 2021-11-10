from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from myblog.models import Article, Category, Tag


def index(request):
    allarticle=Article.objects.order_by('-views')
    newarticle=Article.objects.order_by('created_time')[0:10]
    category = Category.objects.order_by('index')[0:10]
    tag= Tag.objects.order_by('-id')
    paginator = Paginator(allarticle, 2)  # 第页只显示4行
    num_p = request.GET.get('page')
    try:
        contacts = paginator.page(num_p)
        articles = contacts.object_list
        # 参数错误返回第一页数据
    except PageNotAnInteger:
        contacts = paginator.page(1)
        articles = contacts.object_list
        # 超过最大页数返回最后一页
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
        articles = contacts.object_list
    text={
    'allarticle':allarticle,
    'newarticle':newarticle,
    'category':category,
        'tag':tag,
        'list': contacts,
        'articles': articles,
    }
    return render(request,'index.html'  ,text)


def blog(request):
    allarticle = Article.objects.order_by('-created_time')
    paginator = Paginator(allarticle, 4) #第页只显示4行
    num_p= request.GET.get('page')
    try:
        contacts = paginator.page(num_p)
        articles = contacts.object_list
        # 参数错误返回第一页数据
    except PageNotAnInteger:
        contacts = paginator.page(1)
        articles = contacts.object_list
        # 超过最大页数返回最后一页
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
        articles = contacts.object_list
    text = {
        'list': contacts,
        'articles': articles,
    }
    print(articles)
    return render(request, 'full-width.html', text)



def retail(request,id):
    article=Article.objects.filter(id=id)
    text = {
        'article': article,

    }
    return render(request, 'retail.html', text)




def about(request):
    allarticle = Article.objects.all()
    text = {
        'allarticle': allarticle,

    }
    return render(request, 'about.html', text)

def contact(request):
    allarticle = Article.objects.all()
    text = {
        'allarticle': allarticle,

    }
    return render(request, 'contact.html', text)