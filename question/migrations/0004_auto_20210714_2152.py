# Generated by Django 3.2.5 on 2021-07-14 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_answer_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
