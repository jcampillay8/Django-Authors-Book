# Generated by Django 2.2.4 on 2021-05-01 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=45, null=True),
        ),
    ]