# Generated by Django 5.0.3 on 2024-06-27 06:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guardian',
            name='orphan',
        ),
        migrations.AddField(
            model_name='guardian',
            name='orphans',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='guardians', to='webapp.orphan'),
        ),
        migrations.AlterField(
            model_name='orphan',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
