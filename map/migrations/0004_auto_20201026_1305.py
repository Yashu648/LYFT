# Generated by Django 3.1.1 on 2020-10-26 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_id',
        ),
        migrations.RemoveField(
            model_name='event',
            name='image',
        ),
        migrations.RemoveField(
            model_name='event',
            name='user_id',
        ),
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/events/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='cost',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='event',
            name='desc',
            field=models.TextField(max_length=300),
        ),
    ]
