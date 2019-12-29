# Generated by Django 2.2 on 2019-12-29 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locales', '0001_initial'),
        ('items', '0003_auto_20191229_0350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='local',
        ),
        migrations.AddField(
            model_name='items',
            name='locales',
            field=models.ManyToManyField(blank=True, null=True, to='locales.Local', verbose_name='Locales'),
        ),
    ]
