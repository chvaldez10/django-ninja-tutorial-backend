# Generated by Django 5.0 on 2024-09-02 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waitlists', '0002_rename_emails_waitlistentry_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='waitlistentry',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]