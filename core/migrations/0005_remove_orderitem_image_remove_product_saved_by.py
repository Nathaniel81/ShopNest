# Generated by Django 5.0.4 on 2024-05-11 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_product_countinstock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='saved_by',
        ),
    ]