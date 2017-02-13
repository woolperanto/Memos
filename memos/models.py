from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Tag(models.Model):

    name = models.CharField( max_length=100)

    class Meta:
        verbose_name = u'Tag'
        verbose_name_plural = u'Tags'

    def __unicode__(self):
        return self.name

class Karte(models.Model):
    karte_frontside_text = models.CharField(max_length=200)
    karte_backside_text = models.TextField( blank=True)
    times_showed = models.IntegerField(default=0)
    times_known = models.IntegerField(default=0)
    show_factor = models.IntegerField(default=0)
    tag = models.ManyToManyField(Tag, verbose_name=u'Tags')
    author = models.ForeignKey(User, verbose_name=u'User')
    date_created = models.DateTimeField(editable=False)
    date_updated = models.DateTimeField(editable=False)
    showed_last_date = models.DateTimeField(editable=False)

    class Meta:
        verbose_name = u'Karte'
        verbose_name_plural = u'Karten'
        ordering = ['-showed_last_date']

    def __unicode__(self):
        return self.karte_frontside_text

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = now()
        self.date_updated = now()
        self.showed_last_date = now()
        super(Karte, self).save(*args, **kwargs)