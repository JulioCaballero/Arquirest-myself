# Generated by Django 2.2.1 on 2019-07-01 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumno', '0003_remove_alumno_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='token',
            field=models.IntegerField(null=True),
        ),
    ]