# Generated by Django 4.2.5 on 2023-09-27 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('sex', models.CharField(max_length=10)),
                ('place', models.TextField(max_length=10)),
            ],
        ),
    ]
