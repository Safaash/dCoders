from django.http import Http404, HttpResponse
from django.shortcuts import render,redirect
from home.models import Blog,Contact
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
#  Create your views here.
def home(request):
    return render(request,'home.html')

def blog(request):
    blogs=Blog.objects.all().order_by('-time')
    paginator = Paginator(blogs, 3 )# Show 3 blogs per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'blogs':page_obj}
    return render(request, 'blog.html',context)

def contact(request):
    return render(request,'contact.html')

def blogpost(request,slug):
    blog=Blog.objects.filter(slug=slug).first()
    context={'blog':blog}
    return render(request,'blogpost.html',context)
     
def search(request):
    if request.method=='POST':
        keyword= request.POST['keyword']
        blog=Blog.objects.all().filter(Q(title__icontains = keyword) | Q(contents__icontains = keyword)).order_by('-time')
        blog_count=blog.count()
        if blog:
        
            blog_count=blog.count()
            context={
            'blog':blog,
            'blog_count':blog_count
            }
            return render(request,'search.html',context)
        else:
            context={
            
            'blog_count':blog_count
            }
            return render(request,'search.html',context)
    else:
        return redirect('blog')

            
    

def contact(request):
    if request.method=='POST':
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        desc=request.POST["message"]
        ins=Contact(name=name,email=email,phone=phone,desc=desc)
        ins.save()
        messages.success(request,'Message Sent Successfully!!!')
        
    return render(request,'contact.html')