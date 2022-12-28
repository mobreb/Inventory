from django.shortcuts import render, redirect
from .models import Item, Person
from .forms import ItemForm, PersonForm
from django.urls import reverse_lazy


# Create your views here.

def goods_list(request):
    if request.method == "POST":
        query = request.POST.get('q')
    else:
        items = Item.objects.order_by("date_created")
        print(items)
    return render(
        request,
        'goods/goods_list.html',
        {'goods_list': items}
    )


def item_create(request):
    if request.method == "POST":
        item_form = ItemForm(request.POST)
        person_form = PersonForm(request.POST)
        if person_form.is_valid():
            if item_form.is_valid():
                new_person = person_form.save()
                new_item = item_form.save(commit=False)
                new_item.related_person = new_person
                new_item.save()
        return redirect(reverse_lazy("item-create"))
    item_form = ItemForm()
    person_form = PersonForm()
    context = {'item_form': item_form, 'person_form': person_form}
    return render(request,
                  'goods/item_form.html',
                  context)


def update_view(request, pk):
    item = Item.objects.get(pk=pk)
    person = Person.objects.get(pk=item.related_person.pk)
    if request.method == "POST":
        item_form = ItemForm(data=request.POST,instance=item)
        person_form = PersonForm(instance=person)
        if item_form.is_valid():
            item_form.save()
        if person_form.is_valid():
            person_form.save()
        return redirect(reverse_lazy('home'))
    item_form = ItemForm(instance=item)
    person_form = PersonForm(instance=person)
    context = {'item_form': item_form, 'person_form': person_form}
    return render(request, 'goods/item_form.html', context)
