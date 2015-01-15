# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150108_2120'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advert',
            options={'verbose_name': 'Alerta', 'verbose_name_plural': 'Alertas'},
        ),
        migrations.AlterModelOptions(
            name='blogindexpage',
            options={'verbose_name': 'Indice de Blogs', 'verbose_name_plural': 'Indices de Blogs'},
        ),
        migrations.AlterModelOptions(
            name='blogpage',
            options={'verbose_name': 'Blog', 'verbose_name_plural': 'Blogs'},
        ),
        migrations.AlterModelOptions(
            name='contactpage',
            options={'verbose_name': 'Página de Contacto', 'verbose_name_plural': 'Página de Contactos'},
        ),
        migrations.AlterModelOptions(
            name='eventindexpage',
            options={'verbose_name': 'Indice de Eventos', 'verbose_name_plural': 'Indices de Eventos'},
        ),
        migrations.AlterModelOptions(
            name='eventpage',
            options={'verbose_name': 'Evento', 'verbose_name_plural': 'Eventos'},
        ),
        migrations.AlterModelOptions(
            name='formpage',
            options={'verbose_name': 'Página de Formulario', 'verbose_name_plural': 'Página de Formularios'},
        ),
        migrations.AlterModelOptions(
            name='newindexpage',
            options={'verbose_name': 'Indice de Noticia', 'verbose_name_plural': 'Indice de Noticias'},
        ),
        migrations.AlterModelOptions(
            name='newpage',
            options={'verbose_name': 'Noticia', 'verbose_name_plural': 'Noticias'},
        ),
        migrations.AlterModelOptions(
            name='personpage',
            options={'verbose_name': 'Página Personal', 'verbose_name_plural': 'Páginas Personales'},
        ),
        migrations.AlterModelOptions(
            name='standardindexpage',
            options={'verbose_name': 'Indice de páginas estandar', 'verbose_name_plural': 'Indices de páginas estandar'},
        ),
        migrations.AlterModelOptions(
            name='standardpage',
            options={'verbose_name': 'Página Estandar', 'verbose_name_plural': 'Páginas Estandar'},
        ),
        migrations.AddField(
            model_name='contactpage',
            name='district',
            field=models.CharField(blank=True, verbose_name='Barrio', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personpage',
            name='district',
            field=models.CharField(blank=True, verbose_name='Barrio', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpagespeaker',
            name='first_name',
            field=models.CharField(blank=True, verbose_name='Nombres', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpagespeaker',
            name='last_name',
            field=models.CharField(blank=True, verbose_name='Apellidos', max_length=255),
            preserve_default=True,
        ),
    ]
