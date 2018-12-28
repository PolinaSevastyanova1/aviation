# Generated by Django 2.1.2 on 2018-12-14 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20181130_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='account_no',
            field=models.TextField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='launches',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='minutes_flown',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='glidingsignup',
            name='total_aerotows',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='glidingsignup',
            name='total_launches',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='glidingsignup',
            name='total_minutes',
            field=models.IntegerField(default=0),
        ),
    ]