# Generated by Django 3.2.5 on 2022-01-25 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20220125_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social_media_info',
            name='user_info',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portfolio.user_info', verbose_name='user info'),
        ),
    ]