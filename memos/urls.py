from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^minus/(?P<pk>\d+)$', 'memos.views.next_karte_minus',
        name='next_karte_minus'),
    url(r'^plus/(?P<pk>\d+)$', 'memos.views.next_karte_plus',
        name='next_karte_plus'),
    url(r'^training/$', 'memos.views.training',
        name='training'),
    url(r'^user/$', 'memos.views.karten_user',
        name='karten_user'),
    url(r'^del/(?P<pk>\d+)$', 'memos.views.karte_del',
        name='karte_del'),
    url(r'^add/(?P<pk>\d+)$', 'memos.views.karte_add',
        name='karte_add'),
    url(r'^create/$', 'memos.views.karte_create',
        name='karte_create'),
    url(r'^edit/(?P<pk>\d+)/$', 'memos.views.karte_edit',
        name='karte_edit'),
#    url(r'^tag=(?P<tagname>-\w+)\$, 'memos.views.tag_karten',
#       name='tag_karten'),
    url(r'^$', views.index, name='memos_index'),
]