# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='view',
            name='ip_address',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
