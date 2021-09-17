from django.shortcuts import render,redirect
from school_app.models import *
from school_app.forms import *
from .forms import *

from django.contrib import messages

# Create your views here.
def admin_dashboard(request):
  return render(request,'admin_panel/admin_dashboard.html')

def add_post(request):
  if request.method == 'POST':
    add_post_form = PostForm(request.POST,request.FILES,instance=request.user)
    if add_post_form.is_valid():
      post = add_post_form.save(commit=False)
      post.user = request.user
      post.save()
      messages.success(request, f'New post added successfully')
      return redirect('admin_dashboard')

  else:
    add_post_form = PostForm()

  return render(request,'admin_panel/add_post.html',{'add_post_form':add_post_form})
