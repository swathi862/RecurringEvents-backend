from django.db import models
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=60)
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(default=timezone.now)
    RecurringType = models.TextChoices('RecurringType', 'DOES-NOT-REPEAT YEARLY MONTHLY WEEKLY DAILY')
    recurring = models.CharField(blank=True, choices=RecurringType.choices, max_length=20, default='')
    count = models.IntegerField(default=0)
    # start_recurrence = models.DateTimeField(default=start)
    # end_recurrence = models.DateTimeField(default=end)
    ical_string = models.CharField(max_length=100, null=True)

    def _str_(self):
        return self.title

    def save(self, *args, **kwargs):
        return super(Event, self).save(*args, **kwargs)
