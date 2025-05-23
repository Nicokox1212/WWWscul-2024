# Generated by Django 5.0.3 on 2025-05-13 19:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kolor', models.CharField(max_length=50)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=6)),
                ('pojemnosc', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Malowanie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pomieszczenia', models.IntegerField()),
                ('id_sciany', models.IntegerField()),
                ('liczba_puszek', models.IntegerField()),
                ('id_farby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farbyapp.farba')),
            ],
        ),
    ]
