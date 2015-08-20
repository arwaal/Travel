# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField()),
                ('reply', models.ForeignKey(to='maim.Comments', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'Travel')),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('comment', models.ForeignKey(to='maim.Comments', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WebUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('profile_picture', models.ImageField(null=True, upload_to=b'Travel')),
                ('bio', models.TextField()),
                ('picture', models.ForeignKey(to='maim.Picture', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
