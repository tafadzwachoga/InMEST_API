# Generated by Django 5.0.1 on 2024-03-04 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imuser',
            name='Is_blocked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='imuser',
            name='Temperal_login_failed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='imuser',
            name='permanent_login_failed',
            field=models.IntegerField(default=0),
        ),
    ]
