# Generated by Django 2.2.11 on 2020-05-04 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_biblioteczny', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='available',
            field=models.IntegerField(choices=[('Tak', 'Tak'), ('Nie', 'Nie')], default=8),
        ),
    ]