# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categoria', models.CharField(default=None, max_length=50, choices=[(b'Saludable', b'Recetas Saludables'), (b'Vegetariana', b'Recetas Vegetarianas'), (b'Gourmet', b'Recetas Gourmet')])),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
                ('pasos', models.TextField(max_length=500)),
                ('imagen', models.ImageField(upload_to=b'images/')),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('precio', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
