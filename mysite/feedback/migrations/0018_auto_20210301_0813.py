# Generated by Django 3.1.5 on 2021-03-01 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0017_auto_20210301_0805'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FeedbackTopics',
            new_name='FeedbackTopic',
        ),
    ]
