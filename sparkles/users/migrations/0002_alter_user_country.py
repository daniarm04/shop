# Generated by Django 4.2 on 2023-05-11 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, choices=[('Россия', 'Россия'), ('США', 'США'), ('Великобритания', 'Великобритания'), ('Франция', 'Франция')], max_length=100, verbose_name='Страна'),
        ),
    ]