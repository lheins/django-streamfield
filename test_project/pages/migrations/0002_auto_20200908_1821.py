# Generated by Django 3.1.1 on 2020-09-08 18:21

from django.db import migrations
import streamfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='stream',
            field=streamfield.fields.StreamField(blank=True, default='[]', verbose_name='Page blocks'),
        ),
    ]