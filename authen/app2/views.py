from django.shortcuts import render, redirect
from .forms import MediaFileForm

def upload_file(request):
    if request.method == 'POST':
        form = MediaFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = MediaFileForm()
    return render(request, 'media.html', {'form': form})

