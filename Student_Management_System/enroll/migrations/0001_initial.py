# Generated by Django 4.2.11 on 2024-05-07 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stundent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=70)),
                ('Lname', models.CharField(max_length=70)),
                ('username', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=70)),
                ('rollno', models.IntegerField()),
                ('contactno', models.IntegerField()),
            ],
        ),
    ]