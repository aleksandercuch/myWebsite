# Generated by Django 2.0.13 on 2019-06-01 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190525_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='model_pic',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='../static/images/'),
        ),
    ]
