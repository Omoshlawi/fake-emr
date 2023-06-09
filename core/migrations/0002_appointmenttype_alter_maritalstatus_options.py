# Generated by Django 4.2.1 on 2023-05-11 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointMentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_code', models.CharField(max_length=20, unique=True)),
                ('type', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='maritalstatus',
            options={'ordering': ['-created_at']},
        ),
    ]
