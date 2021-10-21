# Generated by Django 3.2.7 on 2021-09-18 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_edit', '0001_initial'),
        ('bbs', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_at', models.DateTimeField(auto_now_add=True, verbose_name='賛同日')),
                ('liked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_edit.profile', verbose_name='賛同者')),
                ('liked_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.bbs', verbose_name='投稿')),
            ],
        ),
    ]