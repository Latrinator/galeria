# Generated by Django 5.1.5 on 2025-01-16 17:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id_artist', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('date_of_death', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='eksponaty',
            name='id_artysty',
        ),
        migrations.CreateModel(
            name='Exhibit',
            fields=[
                ('id_exhibit', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('status', models.CharField(max_length=20)),
                ('is_valuable', models.BooleanField(default=False)),
                ('id_artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.artist')),
            ],
        ),
        migrations.DeleteModel(
            name='Artysci',
        ),
        migrations.DeleteModel(
            name='Eksponaty',
        ),
    ]
