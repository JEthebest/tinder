from django.db import models
from django.contrib.auth import get_user_model


# from profile_app.models import User

User = get_user_model()

GENDER_CHOICES = (
    ('MAN', 'Man'),
    ('WOMAN', 'Woman'),
    ('BI', 'Bi'),
    ('OTHER', 'Other')
)

SEX_CHOICES = (
    ('MAIL', 'Mail'),
    ('FEMAIL', 'Femail'),
    ('OTHER', 'Other')
)

# Create your models here.

class Questionnaire(models.Model):
    nickname = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    birthday = models.DateField()
    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        default='OTHER'
    )
    description = models.TextField(max_length=255)
    sex = models.CharField(
        max_length=20,
        choices=SEX_CHOICES,
        default='OTHER'
    )
    phone = models.CharField(max_length=20)
    user = models.ForeignKey(
        User,
        related_name='questionnaire',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = "Анкета"
        verbose_name_plural = 'Анкеты'

    
        
class Like(models.Model):
    like = models.IntegerField()
    dislike = models.IntegerField()
    rating = models.FloatField()
    questionnaire = models.OneToOneField(
        Questionnaire,
        related_name='likes',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Лайк"
        verbose_name_plural = 'Лайки'

class Photo(models.Model):
    image = models.ImageField()
    questionnaire = models.ForeignKey(
        Questionnaire,
        related_name='photos',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = 'Фотки'