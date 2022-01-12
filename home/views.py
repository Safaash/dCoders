from django.shortcuts import render,HttpResponse
from home.models import Blog,Contact
import math
#  Create your views here.
def home(request):
    return render(request,'home.html')

def blog(request):
    blog_no=3
    page_number = request.GET.get('page')
    if page_number is None:
        page_number=1
    else:
        page_number=int(page_number)

    blogs=Blog.objects.all()
    no_of_blogs=len(blogs)
    blogs=blogs[(page_number-1)*blog_no:(page_number*blog_no)]

    if page_number>1:
        prev=page_number-1
    else:
        prev=None


    if page_number<math.ceil(no_of_blogs/blog_no):
        next=page_number+1
    else:
        next=None
    context={'blogs':blogs,'prev':prev,"next":next}
    return render(request, 'blog.html',context)



def contact(request):
    return render(request,'contact.html')

def blogpost(request,slug):
    blog=Blog.objects.filter(slug=slug).first()
    context={'blog':blog}
    return render(request,'blogpost.html',context)
     
def search(request):
    return render(request,'search.html')


def contact(request):
    if request.method=='POST':
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        desc=request.POST["message"]
        ins=Contact(name=name,email=email,phone=phone,desc=desc)
        ins.save()
        print("sucess")
        
    return render(request,'contact.html')