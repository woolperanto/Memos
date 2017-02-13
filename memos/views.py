from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
import datetime

from .forms import KarteForm
from .models import Karte, Tag


def auswahl(karten):
    for x in range(len(karten) - 1):
        karte = karten[x]
        if karte.show_factor is 0:
            return karte
        else:
            karte.show_factor -= 1
            auswahl(karten)

def index(request):
    karten = Karte.objects.order_by('karte_frontside_text')
    if request.GET.get('tag'):
        tag = request.GET['tag']
        karten = karten.filter(tag__name=request.GET['tag'])
        context = {'karten': karten, 'tag': tag}
        return render(request, 'memos/index.html', context)
    else:
        context = {'karten': karten}
        return render(request, 'memos/index.html', context)

#def tag_karten(request, name):
#    tag = get_object_or_404(Tag, name=name)
#    karten = Karte.objects.filter(tag)

def karten_user(request):
    author = request.user
    karten = Karte.objects.filter(author__username=author)
    if request.GET.get('tag'):
        tag = request.GET['tag']
        karten = karten.filter(tag__name=request.GET['tag'])
    else:
        tag = 'gesamt'

    context = {'karten': karten, 'author': author, 'tag': tag}
    return render(request, 'memos/karten_user.html', context)
def gelernt(request):
    pass
@login_required
def training(request):
    author = request.user
    karten = Karte.objects.filter(author__username=author)
    karten = karten.order_by('showed_last_date')
    karte = karten[0]
    context = {'karte': karte, 'author': author}
    return render(request, 'memos/training.html', context)
@login_required
def next_karte_plus(request, pk, ):
    karte = get_object_or_404(Karte, pk=pk)
    karte.showed_last_date = datetime.datetime.now()
    karte.show_factor += 1
    karte.save()
    author = request.user
    karten = Karte.objects.filter(author__username=author)
    karten = karten.order_by('showed_last_date')
    karte = karten[0]
    context = {'karte': karte, 'author': author}
    return render(request, 'memos/training.html', context)

@login_required
def next_karte_minus(request, pk, ):
    karte = get_object_or_404(Karte, pk=pk)
    karte.showed_last_date = datetime.datetime.now()
    karte.show_factor = 0
    karte.save()
    author = request.user
    karten = Karte.objects.filter(author__username=author)
    karten = karten.order_by('showed_last_date')


    karte = auswahl(karten)
    context = {'karte': karte, 'author': author}
    return render(request, 'memos/training.html', context)


@login_required
def karte_create(request):
    if request.method == 'POST':
        form = KarteForm(data=request.POST)
        if form.is_valid():
            karte = form.save(commit=False)
            karte.author = request.user
            karte.save()
            form.save_m2m()
            return redirect('karten_user')
    else:
        form = KarteForm()
    context = {'form': form, 'create': True}
    return render(request, 'memos/form.html', context)

@login_required
def karte_del(request, pk):
    karte = get_object_or_404(Karte, pk=pk)

    karte.delete()
    return redirect('karten_user')

@login_required
def karte_add(request, pk):
    karte = get_object_or_404(Karte, pk=pk)
    karte.author = request.user
    karte.pk = None
    karte.save()
    return redirect('karten_user')


@login_required
def karte_edit(request, pk):
    karte = get_object_or_404(Karte, pk=pk)
    if karte.author is not request.user and not request.user.is_superuser:
        raise PermissionDenied
    if request.method == 'POST':
        form = KarteForm(instance=karte, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('karten_user', author=karte.author)
    else:
        form = KarteForm(instance=karte)
    context = {'form': form, 'create': False}
    return render(request, 'memos/form.html', context)



def render_to_response(self, context, **response_kwargs):
    self.request.memos = self.request.resolver_match.namespace
    return super(index, self).render_to_response(context, **response_kwargs)
