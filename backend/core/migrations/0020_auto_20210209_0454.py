# Generated by Django 3.1.6 on 2021-02-09 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20210209_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='access',
            field=models.CharField(choices=[('private', 'private'), ('public', 'public')], max_length=100, null=True),
        ),
    ]
