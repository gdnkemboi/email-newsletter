# Generated by Django 4.2.4 on 2023-08-29 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0003_alter_subscriber_email'),
        ('emails', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduledemail',
            name='subscribers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subscribers.subscriber'),
        ),
    ]
