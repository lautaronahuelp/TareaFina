# Generated by Django 3.2.24 on 2024-02-16 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0003_alter_tareafina_satisfaction'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TareaFina',
            new_name='Actividad',
        ),
        migrations.AddField(
            model_name='tarea',
            name='act_completas',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tarea',
            name='act_total',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tarea',
            name='completed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
