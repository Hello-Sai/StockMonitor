# Generated by Django 5.0.4 on 2024-05-13 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=25, unique=True)),
                ('timestamp', models.DateTimeField()),
                ('low', models.CharField(max_length=10)),
                ('high', models.CharField(max_length=10)),
                ('close', models.CharField(max_length=10)),
                ('timezone', models.CharField(max_length=25)),
            ],
        ),
    ]