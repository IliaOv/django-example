from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PersonForm
from .models import Message, Person

@login_required
def index(request):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(request.get_full_path())
    name = request.GET.get('name', '')
    people = Person.objects.all()
    if name:
        people = people.filter(name=name)
    names = Person.objects.order_by('name').values_list('name', flat=True).distinct()
    return render(request, 'index.html', {
        'form': form,
        'people': people,
        'names': names,
    })

@login_required
def about(request):
    if request.method == 'POST':
        text = request.POST.get('text', '').strip()
        if text:
            Message.objects.create(text=text)
            Message.objects.create(
                text='42' if text == 'сколько?' else 'уточните вопрос',
                is_bot=True,
            )
        return redirect('about')
    return render(request, 'about.html', {'messages': Message.objects.all()})

# API — снять решётки вместе с serializers.py и urls:
# from rest_framework import viewsets
# from .serializers import PersonSerializer
#
# class PersonViewSet(viewsets.ModelViewSet):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer
