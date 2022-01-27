# Generated by Django 3.2.5 on 2022-01-25 12:44

from django.db import migrations, models
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0017_alter_user_info_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personlization',
            name='Color_theme',
            field=models.CharField(choices=[('YELLOW', 'YELLOW'), ('RED', 'RED'), ('BLUE', 'BLUE'), ('ORANGE', 'ORANGE')], default='Choose color theme', max_length=50, verbose_name='Color Theme for Portfolio Colors'),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='City',
            field=models.CharField(default='Enter City Name', help_text='name of city that would be displayed on front page', max_length=50, verbose_name='City_Name'),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='Country',
            field=django_countries.fields.CountryField(default='Choose Country', help_text='Country of Residence', max_length=2),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='Fullname',
            field=models.CharField(default='Enter Full Name', help_text='Full name to be displayed on portfolio', max_length=50, verbose_name='FullName'),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='Phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='Enter phone number', help_text='Phone number to display on home page', max_length=128, region=None, verbose_name='Phone Number'),
        ),
    ]
