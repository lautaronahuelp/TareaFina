# Generated by Django 3.2.24 on 2024-02-26 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0013_auto_20240226_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='color',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='tareas.color'),
        ),
    ]