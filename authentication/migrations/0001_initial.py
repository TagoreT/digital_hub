# Generated by Django 5.0.1 on 2024-01-11 17:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('mentor_id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100, verbose_name='Full Name')),
                ('employee_id', models.CharField(max_length=20, verbose_name='Employee-ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=10, verbose_name='Phone Number')),
                ('expertise', models.CharField(max_length=50, verbose_name='Expertise')),
                ('college_name', models.CharField(max_length=100, verbose_name='College Name')),
                ('department', models.CharField(choices=[('CSE', 'Computer Science and Engineering'), ('EEE', 'Electrical and Electronics Engineering'), ('IT', 'Information Technology'), ('MECH', 'Mechanical Engineering'), ('ECE', 'Electronics and Communication Engineering'), ('MET', 'Metallurgical Engineering'), ('CIVIL', 'Civil Engineering')], max_length=50, verbose_name='Department')),
                ('years_of_experience', models.IntegerField(verbose_name='Years of Experience')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='Full Name')),
                ('student_id', models.CharField(max_length=20, verbose_name='Student-ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=10, verbose_name='Phone Number')),
                ('university_name', models.CharField(max_length=100, verbose_name='University Name')),
                ('college_name', models.CharField(max_length=100, verbose_name='College Name')),
                ('department', models.CharField(choices=[('CSE', 'Computer Science and Engineering'), ('EEE', 'Electrical and Electronics Engineering'), ('IT', 'Information Technology'), ('MECH', 'Mechanical Engineering'), ('ECE', 'Electronics and Communication Engineering'), ('MET', 'Metallurgical Engineering'), ('CIVIL', 'Civil Engineering')], max_length=50, verbose_name='Department')),
                ('date_of_birth', models.DateField(verbose_name='Date of Birth')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forget_password_token', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('none', 'None'), ('student', 'Student'), ('mentor', 'Mentor'), ('admin', 'Admin')], default='student', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
