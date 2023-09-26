# Generated by Django 4.0.6 on 2023-09-25 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('mom', '0006_remove_orderacceptnotifcation_customer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderAccept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_ordered', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OrderAcceptNotifcation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=300, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notify_order_accept', to='customer.customer')),
                ('mom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notify_order_accept', to='mom.mommodel')),
                ('ordered_item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='order_accept', to='mom.orderitem')),
            ],
        ),
    ]
