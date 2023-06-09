# Generated by Django 3.2 on 2023-04-07 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeleVision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, choices=[('samsung', 'SAMSUNG'), ('tcl', 'TCL'), ('redmi', 'REDMI'), ('lg', 'LG'), ('sony', 'SONY')], default='lg', max_length=256, null=True)),
                ('model', models.CharField(max_length=256)),
                ('price', models.FloatField()),
            ],
        ),
    ]
