# Generated by Django 5.1.1 on 2024-09-18 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='coment_author',
            new_name='comment_author',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='coment_content',
            new_name='comment_content',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='coment_date',
            new_name='comment_date',
        ),
    ]
