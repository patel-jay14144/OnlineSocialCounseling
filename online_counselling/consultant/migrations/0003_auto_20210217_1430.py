# Generated by Django 3.1.1 on 2021-02-17 09:00

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('consultant', '0002_auto_20210217_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultant',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]