# Generated by Django 4.2.7 on 2024-06-02 11:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0018_alter_waec_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waec',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(seconds=60)),
        ),
    ]