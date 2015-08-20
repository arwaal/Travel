# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maim', '0002_auto_20150819_0859'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='webuser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelManagers(
            name='webuser',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='webuser',
            name='id',
        ),
        migrations.RemoveField(
            model_name='webuser',
            name='user',
        ),
        migrations.AddField(
            model_name='webuser',
            name='user_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
