# Generated by Django 4.0.6 on 2022-07-31 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Publisher')),
                ('discriptione', models.TextField(blank=True, verbose_name='Publisher discriptione')),
            ],
        ),
    ]
