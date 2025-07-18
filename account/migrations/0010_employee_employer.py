# Generated by Django 5.0.1 on 2024-03-08 07:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_user_experience_user_qualification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('resume', models.FileField(blank=True, null=True, upload_to='employee_resumes/')),
                ('qualification', models.CharField(blank=True, max_length=50, null=True)),
                ('experience', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('company_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('location', models.CharField(max_length=255)),
            ],
        ),
    ]
