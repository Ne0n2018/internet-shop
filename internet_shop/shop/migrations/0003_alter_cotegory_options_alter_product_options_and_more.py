# Generated by Django 5.0.1 on 2024-01-23 17:10

import django.utils.timezone
import shop.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_user_product_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cotegory',
            options={'ordering': ['name'], 'verbose_name': 'категория', 'verbose_name_plural': 'категории'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name'], 'verbose_name': 'продукт', 'verbose_name_plural': 'продукция'},
        ),
        migrations.AddField(
            model_name='cotegory',
            name='date_created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cotegory',
            name='date_modified',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='date_created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='date_modified',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to=shop.models.image_product_path),
        ),
    ]