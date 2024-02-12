# Generated by Django 5.0.1 on 2024-02-02 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('course_code', models.CharField(max_length=10)),
                ('course_description', models.TextField()),
                ('course_duration', models.IntegerField()),
                ('course_fee', models.IntegerField()),
                ('course_status', models.BooleanField(default=True)),
            ],
        ),
    ]
