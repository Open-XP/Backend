# Generated by Django 5.0 on 2024-01-01 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0007_remove_exam_subject_exam_exam_type_subject_exam_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='pass_mark',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='total_mark',
        ),
    ]
