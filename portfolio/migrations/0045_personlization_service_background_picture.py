# Generated by Django 4.0.1 on 2022-01-28 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0044_alter_services_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='personlization',
            name='Service_background_picture',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='Background picture for service section page'),
        ),
    ]