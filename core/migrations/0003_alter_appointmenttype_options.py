# Generated by Django 4.2.1 on 2023-05-11 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_appointmenttype_alter_maritalstatus_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointmenttype',
            options={'ordering': ['-created_at']},
        ),
    ]