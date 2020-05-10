# Generated by Django 3.0.6 on 2020-05-10 23:00

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredients', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), size=None)),
                ('instructions', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_term', models.CharField(max_length=128)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Recipe')),
            ],
        ),
    ]
