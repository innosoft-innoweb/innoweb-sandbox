# Generated by Django 4.1.2 on 2022-10-23 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='photo',
            field=models.URLField(help_text='Imagen del evento'),
        ),
        migrations.AlterField(
            model_name='event',
            name='place',
            field=models.CharField(help_text='Lugar del evento', max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(help_text='Nombre del evento', max_length=100),
        ),
    ]
