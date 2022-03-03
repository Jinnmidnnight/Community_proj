from django.shortcuts import get_object_or_404, render, redirect
from .models import Community, Comment
from .forms import Commentform
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    community_index = Community.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'community_index':community_index})

@login_required(login_url='/account/login/')
def new(request):
    if request.method == 'GET':
        return render(request, 'new.html')
    else:
        community = Community.objects.create()
        community.title = request.POST['title']
        community.content = request.POST['content']
        community.image = request.FILES.get('image')
        community.save()
        return redirect('detail', community.id)

@login_required(login_url='/account/login/')
def detail(request, community_id):
    community = get_object_or_404(Community, pk=community_id)
    return render(request, 'detail.html', {'community':community})

@login_required(login_url='/account/login/')
@csrf_exempt
def comment(request, community_id):
    form = Commentform(request.POST)
    if form.is_valid():
        finished_form = form.save(commit=False)
        finished_form.post = get_object_or_404(Community, pk=community_id)
        finished_form.save()
    return redirect('detail', community_id)