from django.db import models
from django.contrib.auth.admin import User

# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=150, blank=False)
    created_by = models.ForeignKey(
        User,
        related_name='polls',
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('pub_date',)

    def __str__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(
        Poll,
        related_name = 'choices',
        on_delete = models.CASCADE
    )
    choice = models.CharField(max_length=250)

    def __str__(self):
        return self.choice

class Vote(models.Model):
    choice = models.ForeignKey(
        Choice,
        related_name='votes',
        on_delete=models.CASCADE
    )
    poll = models.ForeignKey(
        Poll,
        on_delete = models.CASCADE
    )
    voted_by = models.ForeignKey(
        User,
        on_delete = models.CASCADE
    )

    class Meta:
        unique_together = ('poll', 'voted_by')