# Generated by Django 4.0.4 on 2022-05-30 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picturesque', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picturesque',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]