# Generated by Django 4.2.3 on 2024-06-25 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_coupon_alter_colorvariant_color_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sizevariant',
            name='size_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
