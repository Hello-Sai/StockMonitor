# Generated by Django 5.0.4 on 2024-05-16 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_stock_volume'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='open',
            field=models.CharField(default=150, max_length=10),
            preserve_default=False,
        ),
    ]
