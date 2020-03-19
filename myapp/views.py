from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import UserForm
from .models import User

# Create your views here.

def home(request):
    return render(request, 'home.html')

def upload(request):
    context = {}
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)

def file_list(request):
    files = User.objects.all()
    return render(request, 'file_list.html',{
        'files': files
    })


def upload_file(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = UserForm()
    return render(request, 'upload_file.html', {
        'form': form
    })

def delete_file(request, pk):
    if request.method == 'POST':
        user = User.objects.get(pk=pk)
        user.delete()
    return redirect('file_list')

def count(request):
    return render(request, 'count.html')
