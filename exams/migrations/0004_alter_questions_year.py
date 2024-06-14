# Generated by Django 4.2.7 on 2024-05-23 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0003_year_alter_questions_option_e_alter_questions_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='year',
            field=models.ForeignKey(default=2000, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='years', to='exams.year'),
        ),
    ]
