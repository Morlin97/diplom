# Generated by Django 2.2.2 on 2019-06-03 14:45

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment_mark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='cover',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='mark',
            field=blog.models.IntegerRangeField(default=0),
        ),
    ]