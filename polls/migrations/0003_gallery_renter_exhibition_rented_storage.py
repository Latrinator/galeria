# Generated by Django 5.1.5 on 2025-01-21 18:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_artist_remove_eksponaty_id_artysty_exhibit_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id_gallery', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('localisation', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Renter',
            fields=[
                ('id_renter', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('localisation', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Exhibition',
            fields=[
                ('id_exhibition', models.AutoField(primary_key=True, serialize=False)),
                ('since', models.DateField()),
                ('until', models.DateField(blank=True, null=True)),
                ('id_exhibit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.exhibit')),
                ('id_gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.gallery')),
            ],
        ),
        migrations.CreateModel(
            name='Rented',
            fields=[
                ('id_rented', models.AutoField(primary_key=True, serialize=False)),
                ('since', models.DateField()),
                ('until', models.DateField(blank=True, null=True)),
                ('id_exhibit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.exhibit')),
                ('id_renter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.gallery')),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id_storage_session', models.AutoField(primary_key=True, serialize=False)),
                ('cause', models.CharField(max_length=40)),
                ('since', models.DateField()),
                ('until', models.DateField(blank=True, null=True)),
                ('id_exhibit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.exhibit')),
            ],
        ),
    ]
