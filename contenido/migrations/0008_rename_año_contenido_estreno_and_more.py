# Generated by Django 5.1.2 on 2024-11-12 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contenido", "0007_rename_descripcion_contenido_sinopsis_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contenido",
            old_name="año",
            new_name="estreno",
        ),
        migrations.RenameField(
            model_name="contenido",
            old_name="actores",
            new_name="protagonistas",
        ),
    ]
