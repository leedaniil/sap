from datetime import date, datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from application.sap.managers import (
    CommentedFeedbackManager,
    EstimatedFeedbackManager,
    FeedbackSettingsManager,
    UserManager,
)


class User(AbstractUser):
    patronymic = models.CharField(
        max_length=100, 
        verbose_name="Patronymic",
    )
    registration_date = models.DateTimeField(
        default=timezone.now, 
        verbose_name="User's Registration Date"
    )
    upload = models.ImageField(
        default="default/default_avatar.png", 
        upload_to="uploads/%Y/%m/%d/", 
        verbose_name="User's Avatar"
    )

    objects = UserManager()

    def __str__(self):
        return self.username


class FeedbackSettings(models.Model):
    group_name = models.CharField(max_length=100, verbose_name="Group name")
    subject = models.CharField(max_length=100, verbose_name="Subject name")
    class_type = models.CharField(max_length=100, verbose_name="Class type")
    chat_name = models.CharField(max_length=100, verbose_name="Chat name")
    feedback_type = models.CharField(max_length=100, verbose_name="Feedback type")
    url = models.CharField(max_length=100, default="", verbose_name="URL to feedback page")
    _hash = models.CharField(max_length=100, default="", verbose_name="Hash")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=("User"))
    date = models.DateField(default=date.today, verbose_name="Commented feedback date")

    objects = FeedbackSettingsManager()
    

class CommentedFeedback(models.Model):
    text = models.TextField(verbose_name="Comment text")
    date = models.DateField(default=date.today, verbose_name="Commented feedback date")
    time = models.TimeField(default=timezone.now, verbose_name="Commented feedback time")
    settings = models.ForeignKey(FeedbackSettings, on_delete=models.CASCADE, verbose_name=("Feedback settings"))

    objects = CommentedFeedbackManager()


class EstimatedFeedback(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, choices=RATING_CHOICES)
    text = models.TextField(blank=True, null=True)
    date = models.DateField(default=date.today, verbose_name="Estimated feedback date")
    time = models.TimeField(default=timezone.now, verbose_name="Estimated feedback time")
    settings = models.ForeignKey(FeedbackSettings, on_delete=models.CASCADE, verbose_name=("Feedback settings"))

    objects = EstimatedFeedbackManager()
