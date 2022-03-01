# Generated by Django 4.0.2 on 2022-03-01 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Shop', '0002_alter_product_full_details'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('allready_purchased', models.BooleanField(default=False)),
                ('cart_added', models.DateTimeField(auto_now_add=True)),
                ('cart_updated', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartToOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allready_ordered', models.BooleanField(default=False)),
                ('order_time', models.DateTimeField(auto_now_add=True)),
                ('payment_ID', models.CharField(blank=True, max_length=264, null=True)),
                ('order_ID', models.CharField(blank=True, max_length=264, null=True)),
                ('orderitems', models.ManyToManyField(to='Order.Cart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
