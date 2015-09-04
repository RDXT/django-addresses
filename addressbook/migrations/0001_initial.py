# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('contact_name', models.CharField(max_length=50, verbose_name='contact name', blank=True)),
                ('address_one', models.CharField(max_length=50, verbose_name='address one', blank=True)),
                ('address_two', models.CharField(max_length=50, verbose_name='address two', blank=True)),
                ('town', models.CharField(max_length=50, verbose_name='town', blank=True)),
                ('county', models.CharField(max_length=50, verbose_name='county', blank=True)),
                ('postcode', models.CharField(max_length=50, verbose_name='postcode', blank=True)),
                ('status', models.IntegerField(default=0, verbose_name='status', choices=[(0, b'Active'), (1, b'Display only'), (2, b'Deleted')])),
            ],
            options={
                'ordering': ['created'],
                'get_latest_by': 'created',
                'verbose_name': 'address',
                'verbose_name_plural': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('iso_code', models.CharField(unique=True, max_length=2, verbose_name='ISO code')),
                ('name', models.CharField(max_length=60, verbose_name='name')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'country',
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.ForeignKey(verbose_name='country', to='addressbook.Country'),
        ),
    ]
