# Generated by Django 2.2.1 on 2019-07-03 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumno', '0005_auto_20190703_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='token',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
