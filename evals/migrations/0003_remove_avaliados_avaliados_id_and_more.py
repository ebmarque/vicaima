# Generated by Django 5.0.6 on 2024-05-14 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evals', '0002_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliados',
            name='avaliados_id',
        ),
        migrations.RemoveField(
            model_name='eventos',
            name='event_id',
        ),
        migrations.RemoveField(
            model_name='form',
            name='form_id',
        ),
        migrations.RemoveField(
            model_name='login',
            name='login_id',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='questions_id',
        ),
        migrations.RemoveField(
            model_name='resultados',
            name='result_id',
        ),
    ]