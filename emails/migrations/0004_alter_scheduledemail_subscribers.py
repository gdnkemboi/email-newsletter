# Generated by Django 4.2.4 on 2023-08-30 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0003_alter_subscriber_email'),
        ('emails', '0003_remove_scheduledemail_subscribers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduledemail',
            name='subscribers',
            field=models.ManyToManyField(related_name='subs', to='subscribers.subscriber'),
        ),
    ]
