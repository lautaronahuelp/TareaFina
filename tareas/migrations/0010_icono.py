# Generated by Django 3.2.24 on 2024-02-26 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0009_categoria_normalized'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icono',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('className', models.CharField(max_length=50)),
            ],
        ),
    ]
