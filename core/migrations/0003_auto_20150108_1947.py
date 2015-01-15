# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields
import wagtail.wagtailcore.fields
import django.db.models.deletion
import modelcluster.tags


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0002_initial_data'),
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('taggit', '0001_initial'),
        ('core', '0002_create_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('text', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AdvertPlacement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('advert', models.ForeignKey(related_name='+', to='core.Advert')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, serialize=False, parent_link=True, to='wagtailcore.Page', primary_key=True)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogIndexPageRelatedLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link_external', models.URLField(verbose_name='Enlace externo', blank=True)),
                ('title', models.CharField(help_text='Título del Enlace', max_length=255)),
                ('link_document', models.ForeignKey(to='wagtaildocs.Document', null=True, related_name='+', blank=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, serialize=False, parent_link=True, to='wagtailcore.Page', primary_key=True)),
                ('body', wagtail.wagtailcore.fields.RichTextField()),
                ('date', models.DateField(verbose_name='Post date')),
                ('feed_image', models.ForeignKey(to='wagtailimages.Image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogPageCarouselItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link_external', models.URLField(verbose_name='Enlace externo', blank=True)),
                ('embed_url', models.URLField(verbose_name='Embed URL', blank=True)),
                ('caption', models.CharField(blank=True, max_length=255)),
                ('image', models.ForeignKey(to='wagtailimages.Image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', blank=True)),
                ('link_document', models.ForeignKey(to='wagtaildocs.Document', null=True, related_name='+', blank=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogPageRelatedLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link_external', models.URLField(verbose_name='Enlace externo', blank=True)),
                ('title', models.CharField(help_text='Título del Enlace', max_length=255)),
                ('link_document', models.ForeignKey(to='wagtaildocs.Document', null=True, related_name='+', blank=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogPageTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content_object', modelcluster.fields.ParentalKey(related_name='tagged_items', to='core.BlogPage')),
                ('tag', models.ForeignKey(related_name='core_blogpagetag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, serialize=False, parent_link=True, to='wagtailcore.Page', primary_key=True)),
                ('name', models.CharField(verbose_name='Nombre', blank=True, max_length=100)),
                ('telephone', models.CharField(verbose_name='Teléfono', blank=True, max_length=20)),
                ('email', models.EmailField(verbose_name='Correo Electrónico', blank=True, max_length=75)),
                ('address_1', models.CharField(verbose_name='Dirección 1', blank=True, max_length=255)),
                ('address_2', models.CharField(verbose_name='Dirección 2', blank=True, max_length=255)),
                ('city', models.CharField(verbose_name='Ciudad', blank=True, max_length=255)),
                ('country', models.CharField(verbose_name='País', blank=True, max_length=255)),
                ('post_code', models.CharField(verbose_name='Código Postal', blank=True, max_length=10)),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('feed_image', models.ForeignKey(to='wagtailimages.Image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='EventIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, serialize=False, parent_link=True, to='wagtailcore.Page', primary_key=True)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='EventIndexPageRelatedLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link_external', models.URLField(verbose_name='Enlace externo', blank=True)),
                ('title', models.CharField(help_text='Título del Enlace', max_length=255)),
                ('link_document', models.ForeignKey(to='wagtaildocs.Document', null=True, related_name='+', blank=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, serialize=False, parent_link=True, to='wagtailcore.Page', primary_key=True)),
                ('date_from', models.DateField(verbose_name='Start date')),
                ('date_to', models.DateField(verbose_name='End date', blank=True, help_text='Not required if event is on a single day', null=True)),
                ('time_from', models.TimeField(verbose_name='Start time', blank=True, null=True)),
                ('time_to', models.TimeField(verbose_name='End time', blank=True, null=True)),
                ('audience', models.CharField(choices=[('public', 'Público'), ('private', 'Privado')], max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('cost', models.CharField(max_length=255)),
                ('signup_link', models.URLField(blank=True)),
                ('feed_image', models.ForeignKey(to='wagtailimages.Image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='EventPageCarouselItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link_external', models.URLField(verbose_name='Enlace externo', blank=True)),
                ('embed_url', models.URLField(verbose_name='Embed URL', blank=True)),
                ('caption', models.CharField(blank=True, max_length=255)),
                ('image', models.ForeignKey(to='wagtailimages.Image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', blank=True)),
                ('link_document', models.ForeignKey(to='wagtaildocs.Document', null=True, related_name='+', blank=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventPageRelatedLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link_external', models.URLField(verbose_name='Enlace externo', blank=True)),
                ('title', models.CharField(help_text='Título del Enlace', max_length=255)),
                ('link_document', models.ForeignKey(to='wagtaildocs.Document', null=True, related_name='+', blank=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventPageSpeaker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link_external', models.URLField(verbose_name='Enlace externo', blank=True)),
                ('first_name', models.CharField(verbose_name='Name', blank=True, max_length=255)),
                ('last_name', models.CharField(verbose_name='Surname', blank=True, max_length=255)),
                ('image', models.ForeignKey(to='wagtailimages.Image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', blank=True)),
                ('link_document', models.ForeignKey(to='wagtaildocs.Document', null=True, related_name='+', blank=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('label', models.CharField(help_text='The label of the form field', max_length=255)),
                ('field_type', models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time')], max_length=16)),
                ('required', models.BooleanField(default=True)),
                ('choices', models.CharField(blank=True, help_text='Comma separated list of choices. Only applicable in checkboxes, radio and dropdown.', max_length=512)),
                ('default_value', models.CharField(blank=True, help_text='Default value. Comma separated values supported for checkboxes.', max_length=255)),
                ('help_text', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FormPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, serialize=False, parent_link=True, to='wagtailcore.Page', primary_key=True)),
                ('to_address', models.CharField(blank=True, help_text='Optional - form submissions will be emailed to this address', max_length=255)),
                ('from_address', models.CharField(blank=True, max_length=255)),
                ('subject', models.CharField(blank=True, max_length=255)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('thank_you_text', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='HomePageCarouselItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link_external', models.URLField(verbose_name='Enlace externo', blank=True)),
                ('embed_url', models.URLField(verbose_name='Embed URL', blank=True)),
                ('caption', models.CharField(blank=True, max_length=255)),
                ('image', models.ForeignKey(to='wagtailimages.Image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', blank=True)),
                ('link_document', models.ForeignKey(to='wagtaildocs.Document', null=True, related_name='+', blank=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HomePageRelatedLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link_external', models.URLField(verbose_name='Enlace externo', blank=True)),
                ('title', models.CharField(help_text='Título del Enlace', max_length=255)),
                ('link_document', models.ForeignKey(to='wagtaildocs.Document', null=True, related_name='+', blank=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, serialize=False, parent_link=True, to='wagtailcore.Page', primary_key=True)),
                ('name', models.CharField(verbose_name='Nombre', blank=True, max_length=100)),
                ('telephone', models.CharField(verbose_name='Teléfono', blank=True, max_length=20)),
                ('email', models.EmailField(verbose_name='Correo Electrónico', blank=True, max_length=75)),
                ('address_1', models.CharField(verbose_name='Dirección 1', blank=True, max_length=255)),
                ('address_2', models.CharField(verbose_name='Dirección 2', blank=True, max_length=255)),
                ('city', models.CharField(verbose_name='Ciudad', blank=True, max_length=255)),
                ('country', models.CharField(verbose_name='País', blank=True, max_length=255)),
                ('post_code', models.CharField(verbose_name='Código Postal', blank=True, max_length=10)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('biography', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('feed_image', models.ForeignKey(to='wagtailimages.Image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', blank=True)),
                ('image', models.ForeignKey(to='wagtailimages.Image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='PersonPageRelatedLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link_external', models.URLField(verbose_name='Enlace externo', blank=True)),
                ('title', models.CharField(help_text='Título del Enlace', max_length=255)),
                ('link_document', models.ForeignKey(to='wagtaildocs.Document', null=True, related_name='+', blank=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StandardIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, serialize=False, parent_link=True, to='wagtailcore.Page', primary_key=True)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('feed_image', models.ForeignKey(to='wagtailimages.Image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='StandardIndexPageRelatedLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link_external', models.URLField(verbose_name='Enlace externo', blank=True)),
                ('title', models.CharField(help_text='Título del Enlace', max_length=255)),
                ('link_document', models.ForeignKey(to='wagtaildocs.Document', null=True, related_name='+', blank=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StandardPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, serialize=False, parent_link=True, to='wagtailcore.Page', primary_key=True)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('feed_image', models.ForeignKey(to='wagtailimages.Image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='StandardPageCarouselItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link_external', models.URLField(verbose_name='Enlace externo', blank=True)),
                ('embed_url', models.URLField(verbose_name='Embed URL', blank=True)),
                ('caption', models.CharField(blank=True, max_length=255)),
                ('image', models.ForeignKey(to='wagtailimages.Image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', blank=True)),
                ('link_document', models.ForeignKey(to='wagtaildocs.Document', null=True, related_name='+', blank=True)),
                ('link_page', models.ForeignKey(to='wagtailcore.Page', null=True, related_name='+', blank=True)),
                ('page', modelcluster.fields.ParentalKey(related_name='carousel_items', to='core.StandardPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StandardPageRelatedLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link_external', models.URLField(verbose_name='Enlace externo', blank=True)),
                ('title', models.CharField(help_text='Título del Enlace', max_length=255)),
                ('link_document', models.ForeignKey(to='wagtaildocs.Document', null=True, related_name='+', blank=True)),
                ('link_page', models.ForeignKey(to='wagtailcore.Page', null=True, related_name='+', blank=True)),
                ('page', modelcluster.fields.ParentalKey(related_name='related_links', to='core.StandardPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='standardindexpagerelatedlink',
            name='link_page',
            field=models.ForeignKey(to='wagtailcore.Page', null=True, related_name='+', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='standardindexpagerelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='related_links', to='core.StandardIndexPage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personpagerelatedlink',
            name='link_page',
            field=models.ForeignKey(to='wagtailcore.Page', null=True, related_name='+', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personpagerelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='related_links', to='core.PersonPage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepagerelatedlink',
            name='link_page',
            field=models.ForeignKey(to='wagtailcore.Page', null=True, related_name='+', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepagerelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='related_links', to='core.HomePage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepagecarouselitem',
            name='link_page',
            field=models.ForeignKey(to='wagtailcore.Page', null=True, related_name='+', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepagecarouselitem',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='carousel_items', to='core.HomePage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='formfield',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='form_fields', to='core.FormPage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventpagespeaker',
            name='link_page',
            field=models.ForeignKey(to='wagtailcore.Page', null=True, related_name='+', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventpagespeaker',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='speakers', to='core.EventPage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventpagerelatedlink',
            name='link_page',
            field=models.ForeignKey(to='wagtailcore.Page', null=True, related_name='+', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventpagerelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='related_links', to='core.EventPage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventpagecarouselitem',
            name='link_page',
            field=models.ForeignKey(to='wagtailcore.Page', null=True, related_name='+', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventpagecarouselitem',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='carousel_items', to='core.EventPage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventindexpagerelatedlink',
            name='link_page',
            field=models.ForeignKey(to='wagtailcore.Page', null=True, related_name='+', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventindexpagerelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='related_links', to='core.EventIndexPage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpagerelatedlink',
            name='link_page',
            field=models.ForeignKey(to='wagtailcore.Page', null=True, related_name='+', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpagerelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='related_links', to='core.BlogPage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpagecarouselitem',
            name='link_page',
            field=models.ForeignKey(to='wagtailcore.Page', null=True, related_name='+', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpagecarouselitem',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='carousel_items', to='core.BlogPage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpage',
            name='tags',
            field=modelcluster.tags.ClusterTaggableManager(verbose_name='Tags', to='taggit.Tag', help_text='A comma-separated list of tags.', blank=True, through='core.BlogPageTag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogindexpagerelatedlink',
            name='link_page',
            field=models.ForeignKey(to='wagtailcore.Page', null=True, related_name='+', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogindexpagerelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='related_links', to='core.BlogIndexPage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='advertplacement',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='advert_placements', to='wagtailcore.Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='advert',
            name='page',
            field=models.ForeignKey(to='wagtailcore.Page', null=True, related_name='adverts', blank=True),
            preserve_default=True,
        ),
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Página de Inicio'},
        ),
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
            preserve_default=True,
        ),
    ]
