# Generated by Django 5.2.3 on 2025-07-03 19:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0011_rename_categoria_livros_categoria_and_more'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario'),
            preserve_default=False,
        ),
    ]
