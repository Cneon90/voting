# Generated by Django 3.2.13 on 2022-06-18 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IP', models.CharField(max_length=20)),
                ('Name', models.CharField(max_length=30)),
                ('floor', models.CharField(max_length=2)),
            ],
        ),
    ]