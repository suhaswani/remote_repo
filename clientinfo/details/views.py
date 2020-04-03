from django.shortcuts import render,redirect
from .forms import ClientDetailsForm
from .models import ClientDetails


def register(request):
    form = ClientDetailsForm()
    # data = ClientDetails.objects.all()
    if request.method == 'POST':
        form =ClientDetailsForm(request.POST)
        if form.is_valid():
            form.save()

            # return redirect('/show')
    form = ClientDetailsForm()
    return render(request, 'register.html', {'form': form})


def show_firstname(request):
    firstname = request.POST.get('name')

    f = ClientDetails.objects.filter(first_Name=firstname)
    return render(request,'show.html',{'f':f})


def s_f(request):
    return render(request,'s.html')