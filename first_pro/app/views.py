from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.shortcuts import render
from app.forms import CreateList

# Create your views here.
from app.models import UserList, Item


def index(request):
    lists = UserList.objects.all()
    context = {
        'lists': lists
    }
    return render(request, 'index.html', context=context)


def items(request, id):
    list = UserList.objects.get(id=id)
    items = Item.objects.filter(list_name=list)
    context = {
        'list': list,
        'items': items
    }

    return render(request, 'items.html', context=context)


def create(request):
    if request.method == "POST":
        form = CreateList(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            UserList.objects.create(name=name)
        # name = request.POST.get('name')
        # UserList.objects.create(name=name)
        return redirect('index')
    form = CreateList()
    return render(request, 'create.html', {'form': form})
