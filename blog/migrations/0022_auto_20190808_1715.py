# Generated by Django 2.0.13 on 2019-08-08 15:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20190808_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
