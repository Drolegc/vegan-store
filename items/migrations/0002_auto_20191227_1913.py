# Generated by Django 2.2 on 2019-12-27 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='fiabilidad_minus',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='items',
            name='fiabilidad_plus',
            field=models.IntegerField(default=0),
        ),
    ]
