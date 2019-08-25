# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='categoria',
            field=models.CharField(default=None, max_length=50, choices=[(b'Facil', b'Recetas Faciles'), (b'Saludable', b'Recetas Saludables'), (b'Vegetariana', b'Recetas Vegetarianas'), (b'Gourmet', b'Recetas Gourmet')]),
        ),
    ]
