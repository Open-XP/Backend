# Generated by Django 4.2.7 on 2024-05-25 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0015_alter_questions_subject_alter_questions_year_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waec',
            name='total_questions',
            field=models.IntegerField(default=60),
        ),
    ]
