# Generated by Django 2.2 on 2019-12-29 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_auto_20191229_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='locales',
            field=models.ManyToManyField(blank=True, to='locales.Local', verbose_name='Locales'),
        ),
    ]
