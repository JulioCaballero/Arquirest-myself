# Generated by Django 2.2.1 on 2019-07-03 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumno', '0004_alumno_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='token',
            field=models.IntegerField(max_length=254, null=True),
        ),
    ]
