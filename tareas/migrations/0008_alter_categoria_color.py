# Generated by Django 3.2.24 on 2024-02-21 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0007_alter_categoria_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='color',
            field=models.CharField(default='000000', max_length=6),
        ),
    ]