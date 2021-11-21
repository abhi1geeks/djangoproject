# Generated by Django 3.2.9 on 2021-11-21 11:04

from django.db import migrations, models
import profiles.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleProfiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(help_text='*', max_length=200)),
                ('lastName', models.CharField(max_length=200, null=True)),
                ('dob', models.DateField(help_text='*It should be in DD-MM-YYYY format.', validators=[profiles.validators.validator_dob])),
                ('email', models.EmailField(help_text='*', max_length=254, unique=True)),
                ('mobileNumber', models.CharField(help_text='*It should be indian mobile number.', max_length=13, unique=True, validators=[profiles.validators.validator_mobileNumber])),
                ('password', models.CharField(help_text='*Password should contai: number, special character, alphabate(upeer and lower).', max_length=200, validators=[profiles.validators.validator_password])),
            ],
        ),
    ]