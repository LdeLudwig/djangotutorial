# Generated by Django 5.1.4 on 2024-12-30 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='quastion_text',
            new_name='question_text',
        ),
    ]