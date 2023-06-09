# Generated by Django 3.2 on 2023-04-08 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_television'),
    ]

    operations = [
        migrations.AlterField(
            model_name='television',
            name='company',
            field=models.CharField(choices=[('samsung', 'SAMSUNG'), ('tcl', 'TCL'), ('redmi', 'REDMI'), ('lg', 'LG'), ('sony', 'SONY')], default='lg', max_length=256),
        ),
        migrations.AlterField(
            model_name='television',
            name='model',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='television',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
