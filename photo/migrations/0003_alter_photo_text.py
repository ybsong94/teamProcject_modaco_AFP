# Generated by Django 3.2.5 on 2021-07-20 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_rename_phot_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
