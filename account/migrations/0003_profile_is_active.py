# Generated by Django 4.1 on 2023-07-08 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_profile_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Ativo'),
        ),
    ]