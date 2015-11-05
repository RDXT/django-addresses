# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


def fix_countries(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Country = apps.get_model("addressbook", "Country")
    Address = apps.get_model("addressbook", "Address")
    for address in Address.objects.all():
        try:
            c = Country.objects.get(pk=int(address.country))
            address.country = c.iso_code
            address.save()
        except ValueError:
            pass


class Migration(migrations.Migration):
    dependencies = [
        ('addressbook', '0002_auto_20150903_2227'),
    ]

    operations = [
        migrations.RunPython(fix_countries),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, verbose_name='country'),
        ),
    ]
