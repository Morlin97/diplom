# Generated by Django 2.2.2 on 2019-06-03 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='cover',
            field=models.ImageField(default=None, upload_to='images/'),
            preserve_default=False,
        ),
    ]