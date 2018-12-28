# Generated by Django 2.1.2 on 2018-11-30 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='glidingsession',
            options={'verbose_name': 'Gliding Session'},
        ),
        migrations.AddField(
            model_name='glidingsession',
            name='max_attendees',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='glidingsignup',
            name='is_driver',
            field=models.BooleanField(default=False),
        ),
    ]