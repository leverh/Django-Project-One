# Generated by Django 4.2.2 on 2023-06-10 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='preparation',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
