# Generated by Django 4.0.1 on 2022-01-28 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0048_personlization_experience_background_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personlization',
            name='Animation',
            field=models.BooleanField(default=True, null=True, verbose_name='animation on homepage'),
        ),
        migrations.AlterField(
            model_name='personlization',
            name='Background_picture',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='home page bg '),
        ),
        migrations.AlterField(
            model_name='personlization',
            name='Experience_background_picture',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='experience page bg'),
        ),
        migrations.AlterField(
            model_name='personlization',
            name='Experience_background_picture_switch',
            field=models.BooleanField(default=True, null=True, verbose_name='experience page bg switch'),
        ),
        migrations.AlterField(
            model_name='personlization',
            name='Service_background_picture',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='service page bg'),
        ),
        migrations.AlterField(
            model_name='personlization',
            name='Service_background_picture_switch',
            field=models.BooleanField(default=True, null=True, verbose_name='service page bg switch'),
        ),
        migrations.AlterField(
            model_name='personlization',
            name='Terminal_icon_blink',
            field=models.BooleanField(default=True, null=True, verbose_name='Blink terminal icon'),
        ),
    ]