# Generated by Django 4.2.7 on 2024-05-23 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0003_year_alter_questions_option_e_alter_questions_year'),
        ('quiz_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testinstance',
            name='year',
            field=models.ManyToManyField(to='exams.year'),
        ),
    ]
