# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maim', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webuser',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='webuser',
            name='password',
        ),
        migrations.RemoveField(
            model_name='webuser',
            name='picture',
        ),
        migrations.AddField(
            model_name='webuser',
            name='user',
            field=models.OneToOneField(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='reply',
            field=models.ForeignKey(blank=True, to='maim.Comments', null=True),
        ),
        migrations.AlterField(
            model_name='picture',
            name='comment',
            field=models.ForeignKey(blank=True, to='maim.Comments', null=True),
        ),
    ]
