# Generated by Django 5.0.1 on 2024-03-08 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0022_rename_employer_company_rename_employee_jobseeker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobseeker',
            name='user',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='JobSeeker',
        ),
    ]
