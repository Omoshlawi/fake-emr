# Generated by Django 4.2.1 on 2023-05-11 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medication', '0003_artregimen_patienthivmedication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hivlabtest',
            name='appointment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='medication.appointment'),
        ),
    ]