# Generated by Django 4.0.1 on 2022-01-28 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0045_personlization_service_background_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='personlization',
            name='Service_background_picture_switch',
            field=models.BooleanField(default=False, null=True, verbose_name='ON or OFF picture on the service page'),
        ),
    ]