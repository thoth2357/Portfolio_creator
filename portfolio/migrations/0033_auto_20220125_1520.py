# Generated by Django 3.2.5 on 2022-01-25 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0032_auto_20220125_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_info',
            name='profession',
            field=models.CharField(help_text='professions to be placed on homepage. Use comma to separate profession', max_length=50, null=True, verbose_name='Professions'),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='Curriculum_vitae',
            field=models.FileField(help_text='File upload for CV', null=True, upload_to='upload/', verbose_name='Curriculum_Vitae'),
        ),
    ]