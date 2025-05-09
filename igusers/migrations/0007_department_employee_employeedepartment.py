# Generated by Django 4.2.4 on 2025-03-22 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('igusers', '0006_followunfollow'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='igusers.department')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='igusers.employee')),
            ],
        ),
    ]
