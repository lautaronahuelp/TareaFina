# Generated by Django 3.2.24 on 2024-02-15 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0002_rename_resultado_reaccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tareafina',
            name='satisfaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tareas.reaccion'),
        ),
    ]