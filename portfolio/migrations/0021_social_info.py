# Generated by Django 3.2.5 on 2022-01-25 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0020_alter_portfolio_portfolio_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Facebook_url', models.URLField(verbose_name='Facebook Account Url')),
                ('Instagram_url', models.URLField(verbose_name='Instagram Account Url')),
                ('Twitter_url', models.URLField(verbose_name='Twitter Account Url')),
                ('LinkedIn_url', models.URLField(verbose_name='LinkedIn Account Url')),
                ('Mail_account_name', models.URLField(verbose_name='Mail Name')),
            ],
            options={
                'verbose_name': 'Social_info',
                'verbose_name_plural': 'Social_infos',
            },
        ),
    ]