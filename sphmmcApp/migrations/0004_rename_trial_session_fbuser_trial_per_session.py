# Generated by Django 4.2.7 on 2024-03-20 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sphmmcApp', '0003_fbuser_session_key_fbuser_trial_session'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fbuser',
            old_name='trial_session',
            new_name='trial_per_session',
        ),
    ]