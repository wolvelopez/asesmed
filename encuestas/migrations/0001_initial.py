# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eleccion',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('eleccion_texto', models.CharField(max_length=200)),
                ('votos', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('pregunta_texto', models.CharField(max_length=200)),
                ('pregunta_fecha', models.DateTimeField(verbose_name='fecha Publicacion')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='eleccion',
            name='pregunta',
            field=models.ForeignKey(to='encuestas.Pregunta'),
            preserve_default=True,
        ),
    ]
