# Generated by Django 3.2.5 on 2021-07-21 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_alter_photo_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='content/'),
        ),
    ]
