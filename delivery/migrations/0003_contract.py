# Generated by Django 4.2.13 on 2024-07-13 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0002_receiver'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('patronymic', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]
