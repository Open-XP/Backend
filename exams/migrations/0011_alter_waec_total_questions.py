# Generated by Django 4.2.7 on 2024-05-24 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0010_alter_waec_total_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waec',
            name='total_questions',
            field=models.IntegerField(default=3),
        ),
    ]
