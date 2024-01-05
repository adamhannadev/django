# Generated by Django 5.0 on 2024-01-04 11:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dance_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_name', models.CharField(max_length=30)),
                ('level_value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Figure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('figure_name', models.CharField(max_length=30)),
                ('leader_description', models.TextField()),
                ('follower_description', models.TextField()),
                ('dance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='progress.dance')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='progress.level')),
            ],
        ),
    ]