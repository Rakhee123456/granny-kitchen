# Generated by Django 4.0.6 on 2023-09-20 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('mom', '0002_remove_order_is_delivered_remove_order_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderAcceptNotifcation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notify_order_accept', to='customer.customer')),
                ('mom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notify_order_accept', to='mom.mommodel')),
            ],
        ),
        migrations.CreateModel(
            name='OrderAccept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_placed', models.BooleanField(default=False)),
                ('order_placed', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='order_accept', to='mom.orderitem')),
            ],
        ),
    ]
