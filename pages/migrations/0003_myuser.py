# Generated by Django 4.0.1 on 2022-02-02 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_myuser1_delete_myuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='myuser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
    ]
