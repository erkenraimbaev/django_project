# Generated by Django 4.2.7 on 2024-01-08 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_confirm_key',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='код подтверждения почты'),
        ),
    ]
