from django.shortcuts import render, get_object_or_404
from .models import Video, Category


def Search(request):
    if request.method == "POST":
        search = request.POST['search']
        search_v = Video.objects.filter(title__contains=search)
        categories_c = Category.objects.all()
        
        
        return render(request,'search.html',{"search":search,"search_v":search_v,"categories_c":categories_c,})
    else:
   
        return render(request,'search.html',{"message":"Content Not Available",})

def homePage(request,movie_id):
    categories_c = Category.objects.all()
    video = Video.objects.get(pk = movie_id)
    return render(request,'player.html',{"video":video,"categories_c":categories_c})

def contact(request):
    categories_c = Category.objects.all()
    return render(request,'contactus.html',{"categories_c":categories_c})

def about(request):
    categories_c = Category.objects.all()
    return render(request,'aboutus.html',{"categories_c":categories_c})

def home(request):
    categories_c = Category.objects.all()
    video_h = Video.objects.all()
    chunked_video_h = [video_h[i:i + 4] for i in range(0, len(video_h), 4)]
    return render(request,'home.html',{"video_h":video_h, "categories_c":categories_c, "category":category,'chunked_video_h': chunked_video_h,})

def category(request, category_slug=None):
    category = None
    categories_c = Category.objects.all()
    video_c = Video.objects.all()
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        video_c = Video.objects.filter(category=category)
    
    return render(request, 'category_data.html', {"video_c": video_c, "categories_c": categories_c, "category": category})

