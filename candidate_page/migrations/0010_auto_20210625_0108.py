# Generated by Django 3.2.4 on 2021-06-24 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('candidate_page', '0009_alter_position_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='title',
        ),
        migrations.AddField(
            model_name='candidate',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='candidate',
            name='body',
            field=models.TextField(help_text='Write a brief introduction of yourself', verbose_name='About'),
        ),
    ]