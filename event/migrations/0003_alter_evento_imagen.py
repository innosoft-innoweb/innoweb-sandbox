# Generated by Django 4.1.2 on 2022-10-23 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0002_alter_evento_imagen_alter_evento_lugar_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="photo",
            field=models.URLField(help_text="Url de la imagen del evento"),
        ),
    ]