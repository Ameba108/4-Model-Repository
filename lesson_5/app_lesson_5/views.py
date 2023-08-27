from django.shortcuts import render, redirect
from django.urls import reverse,reverse_lazy
from .models import Advertisement
from .forms import AdvertisementForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib.auth import get_user_model
User = get_user_model()

def index(request):
    input = request.GET.get("query")
    if input:
        advertisements = Advertisement.objects.filter(title_icontains=input)
    else:
        advertisements =  Advertisement.objects.all()
    context = {"advertisements" : advertisements}
    return render(request,"app_lesson_5/index.html", context)

def top_sellers(request):
    users= User.objects.annotate(
        adv_count=Count('advertisement')
    ).order_by('-adv_count')
    context={'users':users}
    return render(request,"app_lesson_5/top-sellers.html", context)

@login_required(login_url=reverse_lazy('login'))
def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            new_advertisement = form.save(commit=False)
            new_advertisement.user = request.user
            new_advertisement.save()
            url = reverse('index')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'app_lesson_5/advertisement-post.html', context)

def advertisement_detail(request,pk):
    advertisement=Advertisement.objects.filter(id=pk)
    context={'advertisement':advertisement}
    return render(request,"app_lesson_5/advertisement.html", context)