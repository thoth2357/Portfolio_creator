# Generated by Django 3.2.5 on 2022-01-25 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0034_alter_user_info_profession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='Portfolio_name',
            field=models.CharField(default='MY PORTFOLIO CONFIG', max_length=50, null=True, unique=True, verbose_name='portfolio_name/id'),
        ),
    ]