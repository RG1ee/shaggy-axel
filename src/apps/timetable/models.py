from django.db import models


class WeekDay(models.Model):
    title = models.CharField(max_length=20)
    weekend = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title


class Job(models.Model):
    title = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    
    def __str__(self):
        return f"{self.title} | {self.price} RUB/hour"


def get_default_job():
    """ Return default job as free time """
    return Job.objects.get_or_create(title="Free Time", price=0.0)[0]


def get_default_job_id():
    """ Return id of default job as free time """
    return get_default_job().id


class WorkTime(models.Model):
    start_time = models.CharField(max_length=15)
    end_time = models.CharField(max_length=15)
    weekday = models.ForeignKey(WeekDay, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.SET(get_default_job), default=get_default_job_id)

    def __str__(self):
        return f"{self.job} | {self.weekday} | {self.start_time} - {self.end_time}"