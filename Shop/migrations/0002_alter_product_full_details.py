# Generated by Django 4.0.2 on 2022-03-01 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='full_details',
            field=models.TextField(max_length=3000, verbose_name='full_details'),
        ),
    ]
