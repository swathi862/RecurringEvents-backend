# Generated by Django 3.1.7 on 2021-03-29 04:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('start', models.DateTimeField(default=django.utils.timezone.now)),
                ('end', models.DateTimeField(default=django.utils.timezone.now)),
                ('recurring', models.CharField(blank=True, choices=[('DOES-NOT-REPEAT', 'Does-Not-Repeat'), ('YEARLY', 'Yearly'), ('MONTHLY', 'Monthly'), ('WEEKLY', 'Weekly'), ('DAILY', 'Daily')], default='', max_length=20)),
                ('count', models.IntegerField(default=0)),
                ('start_recurrence', models.DateTimeField(default=models.DateTimeField(default=django.utils.timezone.now))),
                ('end_recurrence', models.DateTimeField(default=models.DateTimeField(default=django.utils.timezone.now))),
                ('ical_string', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]