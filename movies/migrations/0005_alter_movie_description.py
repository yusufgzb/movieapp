# Generated by Django 3.2.7 on 2022-02-03 19:45

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20220203_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]