# Generated by Django 2.2.1 on 2019-06-28 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('lastName', models.CharField(max_length=254)),
                ('matricula', models.CharField(max_length=254)),
                ('career', models.CharField(max_length=254)),
            ],
            options={
                'db_table': 'Alumnos',
            },
        ),
        migrations.CreateModel(
            name='Rfid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.IntegerField()),
                ('id_alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alumno.Alumnos')),
            ],
            options={
                'db_table': 'Rfid',
            },
        ),
    ]