from django.shortcuts import render,redirect
from .models import blogs
from .forms import blogForm

# Create your views here.

def home(request):
    blog = blogs.objects.all()
    context = {'blog':blog}
    return render(request,'home.html',context)

def post(request,pk):
    post = blogs.objects.get(id=pk)
    context = {'post':post}

    return render(request,'post.html',context)

def createBlog(request):
    form = blogForm

    if request.method == 'POST' :
        form = blogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form }
    return render(request,'blog_form.html',context)

def updateBlog(request,pk):
    post = blogs.objects.get(id=pk)
    form = blogForm(instance=post)

    if request.method == 'POST':
        form = blogForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}

    return render(request,'blog_form.html',context)

def deleteBlog(request,pk):
    post = blogs.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(request,'delete.html',{'obj':post})
