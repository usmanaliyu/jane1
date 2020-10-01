# Generated by Django 2.2.10 on 2020-10-01 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_item_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='style',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='color',
            field=models.CharField(blank=True, choices=[('black', 'Black'), ('white', 'White'), ('red', 'Red'), ('pink', 'Pink'), ('green', 'Green'), ('purple', 'Purple'), ('brown', 'Brown')], max_length=1000, null=True),
        ),
    ]
