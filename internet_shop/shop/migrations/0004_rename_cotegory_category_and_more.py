# Generated by Django 5.0.1 on 2024-01-23 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_cotegory_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cotegory',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='cotegory',
            new_name='category',
        ),
    ]