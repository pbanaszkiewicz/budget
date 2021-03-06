# Generated by Django 3.0.2 on 2020-01-29 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_auto_20200119_0834'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ['date', 'description']},
        ),
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.ForeignKey(help_text='', on_delete=django.db.models.deletion.PROTECT, to='expenses.Category', verbose_name='Category'),
        ),
    ]
