# Generated by Django 3.0.2 on 2020-01-02 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=40)),
                ('lname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
