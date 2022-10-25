from django.db import models
from django.utils import timezone

class To_do(models.Model):
    item = (
        ('1', '完了'),
        ('2', '未完了'),
    )
    states = models.CharField(max_length=1, choices=item, default='2')
    deadline = models.DateField(verbose_name="期日", blank=False, null=False, default=timezone.now)
    task = models.CharField(verbose_name="タスク名", blank=False, null=False, max_length=10)

    class Meta:
        verbose_name_plural = "Task"

    def __str__(self):
        return self.task
