# Generated by Django 4.2.6 on 2023-11-27 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='cars',
            field=models.ManyToManyField(through='myapp.Ownership', to='myapp.car'),
        ),
    ]
