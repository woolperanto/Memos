from django import template
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.html import format_html_join

from ..models import Tag


register = template.Library()


@register.simple_tag(takes_context=True)
def tagcloud(context, author=None):
    if author == None:
        url = reverse('memos_index')
        tags = Tag.objects.all()
        tags = tags.annotate(count=models.Count('karte'))
        tags = tags.order_by('name').values_list('name','count')
        fmt = '<a href="%s?tag={0}">{0} ({1})</a><br>' % url
    else:
        url = reverse('memos_karten_user')
        tags = Tag.objects.all()
        tags = tags.annotate(count=models.Count('karte'))
        tags = tags.order_by('name').values_list('name', 'count')
        fmt = '<a href="%s?tag={0}">{0} ({1})</a>' % url
    return format_html_join('   ', fmt, tags)