# Generated by Django 2.1.3 on 2018-11-20 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pink_forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='topic',
            name='status',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='vote',
            name='point',
            field=models.SmallIntegerField(default=0),
        ),
    ]
