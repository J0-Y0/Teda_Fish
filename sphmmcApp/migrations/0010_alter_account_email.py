# Generated by Django 4.2.7 on 2024-03-20 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sphmmcApp', '0009_rename_last_lname_account_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=300),
        ),
    ]
