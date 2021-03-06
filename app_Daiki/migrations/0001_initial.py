# Generated by Django 4.0.4 on 2022-05-12 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('estado_emision', models.CharField(max_length=20)),
                ('estudio', models.CharField(max_length=30)),
                ('temporadas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('genero', models.CharField(max_length=20)),
                ('autor', models.CharField(max_length=30)),
                ('anio_lanzamiento', models.IntegerField()),
                ('cantidad_tomos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('estudio', models.CharField(max_length=30)),
                ('fecha_estreno', models.DateField()),
                ('duracion', models.IntegerField()),
            ],
        ),
    ]
