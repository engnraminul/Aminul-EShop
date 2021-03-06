# Generated by Django 4.0.2 on 2022-02-24 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_image', models.ImageField(upload_to='Products')),
                ('Product_name', models.CharField(max_length=250)),
                ('sort_details', models.TextField(max_length=300, verbose_name='sort_details')),
                ('full_details', models.TextField(max_length=300, verbose_name='full_details')),
                ('price', models.FloatField()),
                ('old_price', models.FloatField(default=0.0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='Shop.category')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
