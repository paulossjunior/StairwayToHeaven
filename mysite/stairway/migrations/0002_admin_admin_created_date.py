# Generated by Django 3.0.3 on 2020-03-31 17:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stairway', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='admin_created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]