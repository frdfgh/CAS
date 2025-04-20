from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login/')
def index(request):
    request.session.set_expiry(300)
    #cats = Category.objects.all()
    #posts = Post.objects.all()
    return render(request, 'index.html')#, {'categories': cats, 'posts': posts})


# @login_required(login_url='/login/')
# def categoryView(request, slug):
#     request.session.set_expiry(300)
#     cat = get_object_or_404(Category, slug=slug)
#     posts = Post.objects.all().filter(category=cat)
#     return render(request, 'category.html', {'category': cat, 'posts': posts})


# @login_required(login_url='/login/')
# def postView(request, slug):
#     request.session.set_expiry(300)
#     cat = get_object_or_404(Post, slug=slug)
#     post = Post.objects.all().filter(slug=slug)
#     return render(request, 'post.html', {'category': cat, 'posts': post})


def loginView(request):
    if not request.session.get('logged'):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                request.session['logged'] = 1
                request.session.set_expiry(300)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('mainPage')
        else:
            form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})


def logoutView(request):
    if request.method == 'POST':
        try:
            del request.session['logged']
        except KeyError:
            pass
        logout(request)
        return redirect("loginPage")


# def paymentView(request):
#     return render(request, 'payment.html')