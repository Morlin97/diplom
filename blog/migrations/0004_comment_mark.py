# Generated by Django 2.2.2 on 2019-06-03 14:42

import blog.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='mark',
            field=blog.models.IntegerRangeField(default=0),
            preserve_default=False,
        ),
    ]
