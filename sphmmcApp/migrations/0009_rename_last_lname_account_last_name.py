# Generated by Django 4.2.7 on 2024-03-20 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sphmmcApp', '0008_rename_fieldofinterest_account_field_of_interest_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='last_lname',
            new_name='last_name',
        ),
    ]
