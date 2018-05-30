# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-30 18:08
from __future__ import unicode_literals

import cms.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeFeaturedArticlePlaceholder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_featured_article', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_featured_article', slotname='home_featured_article', to='cms.Placeholder')),
            ],
        ),
    ]
