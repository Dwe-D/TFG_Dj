# Generated by Django 4.2.6 on 2023-12-11 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensores', '0002_usuarioarduino_nombre_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuarioarduino',
            old_name='nombre',
            new_name='alias',
        ),
    ]
