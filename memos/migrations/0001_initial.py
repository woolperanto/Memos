# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Karte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('karte_frontside_text', models.CharField(max_length=200)),
                ('karte_backside_text', models.TextField(blank=True)),
                ('times_showed', models.IntegerField(default=0)),
                ('times_known', models.IntegerField(default=0)),
                ('show_factor', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(editable=False)),
                ('date_updated', models.DateTimeField(editable=False)),
                ('showed_last_date', models.DateTimeField(editable=False)),
                ('author', models.ForeignKey(verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_created'],
                'verbose_name': 'Karte',
                'verbose_name_plural': 'Karten',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AddField(
            model_name='karte',
            name='tag',
            field=models.ManyToManyField(to='memos.Tag', verbose_name='Tags'),
        ),
    ]
