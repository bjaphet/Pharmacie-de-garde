# Generated by Django 5.1.1 on 2024-09-20 12:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharma', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pharmacie',
            name='ville',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='pharma.ville'),
        ),
    ]
