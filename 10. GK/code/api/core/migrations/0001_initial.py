# Generated by Django 4.2.1 on 2023-05-08 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=20, null=True)),
                ('gender', models.TextField(choices=[('Nam', 'Male'), ('Nữ', 'Female')], default=0)),
                ('DoB', models.TextField(default='2023')),
                ('university_name', models.CharField(max_length=200, null=True)),
                ('major', models.TextField(default='NULL')),
            ],
        ),
    ]
