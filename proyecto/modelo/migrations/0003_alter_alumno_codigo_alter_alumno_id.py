# Generated by Django 4.2.4 on 2023-12-07 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0002_alumno_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='codigo',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
