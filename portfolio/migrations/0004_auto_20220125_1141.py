# Generated by Django 3.2.5 on 2022-01-25 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_social_media_info_user_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='social_media_info',
            name='user_info',
        ),
        migrations.AddField(
            model_name='user_info',
            name='Social_media_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.social_media_info', verbose_name='social media info'),
        ),
    ]