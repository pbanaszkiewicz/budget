# Generated by Django 3.0.2 on 2020-02-16 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0004_auto_20200208_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.ForeignKey(help_text='', on_delete=django.db.models.deletion.PROTECT, to='expenses.Category', verbose_name='Category'),
        ),
    ]
