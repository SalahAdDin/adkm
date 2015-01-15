# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import modelcluster.fields
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0002_initial_data'),
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('core', '0003_auto_20150108_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(to='wagtailcore.Page', primary_key=True, auto_created=True, parent_link=True, serialize=False)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('feed_image', models.ForeignKey(to='wagtailimages.Image', on_delete=django.db.models.deletion.SET_NULL, related_name='+', null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='NewIndexPageRelatedLink',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('sort_order', models.IntegerField(editable=False, null=True, blank=True)),
                ('link_external', models.URLField(blank=True, verbose_name='Enlace externo')),
                ('title', models.CharField(max_length=255, help_text='Título del Enlace')),
                ('link_document', models.ForeignKey(to='wagtaildocs.Document', related_name='+', null=True, blank=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NewPage',
            fields=[
                ('page_ptr', models.OneToOneField(to='wagtailcore.Page', primary_key=True, auto_created=True, parent_link=True, serialize=False)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('feed_image', models.ForeignKey(to='wagtailimages.Image', on_delete=django.db.models.deletion.SET_NULL, related_name='+', null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='NewPageCarouselItem',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('sort_order', models.IntegerField(editable=False, null=True, blank=True)),
                ('link_external', models.URLField(blank=True, verbose_name='Enlace externo')),
                ('embed_url', models.URLField(blank=True, verbose_name='Embed URL')),
                ('caption', models.CharField(max_length=255, blank=True)),
                ('image', models.ForeignKey(to='wagtailimages.Image', on_delete=django.db.models.deletion.SET_NULL, related_name='+', null=True, blank=True)),
                ('link_document', models.ForeignKey(to='wagtaildocs.Document', related_name='+', null=True, blank=True)),
                ('link_page', models.ForeignKey(to='wagtailcore.Page', related_name='+', null=True, blank=True)),
                ('page', modelcluster.fields.ParentalKey(related_name='carousel_items', to='core.NewPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NewPageRelatedLink',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('sort_order', models.IntegerField(editable=False, null=True, blank=True)),
                ('link_external', models.URLField(blank=True, verbose_name='Enlace externo')),
                ('title', models.CharField(max_length=255, help_text='Título del Enlace')),
                ('link_document', models.ForeignKey(to='wagtaildocs.Document', related_name='+', null=True, blank=True)),
                ('link_page', models.ForeignKey(to='wagtailcore.Page', related_name='+', null=True, blank=True)),
                ('page', modelcluster.fields.ParentalKey(related_name='related_links', to='core.NewPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='newindexpagerelatedlink',
            name='link_page',
            field=models.ForeignKey(to='wagtailcore.Page', related_name='+', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newindexpagerelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='related_links', to='core.NewIndexPage'),
            preserve_default=True,
        ),
    ]
