# Generated by Django 4.2.2 on 2023-06-10 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choices', '0003_choice_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='choices_pictures'),
        ),
    ]
