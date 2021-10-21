# Generated by Django 3.2.7 on 2021-10-14 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_work'),
    ]

    operations = [
        migrations.CreateModel(
            name='Essay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=128, verbose_name='URL')),
                ('year', models.IntegerField(verbose_name='Year')),
                ('month', models.IntegerField(verbose_name='Month')),
                ('date', models.IntegerField(verbose_name='Date')),
            ],
        ),
    ]
