# Generated by Django 2.0.5 on 2018-07-02 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180702_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='lnglat',
            field=models.CharField(blank=True, help_text='위도/경도 포맷으로 입력', max_length=50),
        ),
    ]
