from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    RELIGION = (
        ('NO ANSWER', 'NO ANSWER'),
        ('CHRISTIAN', 'Christian'),
        ('MUSLIM', 'Muslim'),
        ('NA', 'Prefer Not To Say'),
        ('AGNOSTIC', 'Agnostic'),
    )
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    birth_date = models.DateField()
    # Weight in pounds
    weight = models.IntegerField()
    # Height in inches
    height = models.IntegerField()
    EDUCATION_LEVEL = (
        ('NO ANSWER', 'NO ANSWER'),
        ('HIGH SCHOOL', 'High School'),
        ('SOME COLLEGE', 'Some College'),
        ('COLLEGE GRADUATE', 'College Graduate'),
        ('POST GRADUATE', 'Post Graduate'),
    )
    HAIR_COLOR = (
        ('NO ANSWER', 'NO ANSWER'),
        ('BLACK', 'Black'),
        ('BLONDE', 'Blonde'),
        ('DARK BLONDE', 'Dark Blonde'),
        ('LIGHT BROWN', 'Light Brown'),
        ('DARK BROWN', 'Dark Brown'),
        ('RED', 'Red'),
        ('GREY', 'Grey'),
        ('SALT AND PEPPER', 'Salt and Pepper'),
        ('BALD', 'Bald'),
    )
    EYE_COLOR = (
        ('NO ANSWER', 'NO ANSWER'),
        ('BLACK', 'Black'),
        ('BLUE', 'Blue'),
        ('BROWN', 'Brown'),
        ('GREY', 'Grey'),
        ('GREEN', 'Green'),
        ('HAZEL', 'Hazel'),
    )
    BODY_TYPE = (
        ('NO ANSWER', 'NO ANSWER'),
        ('SLENDER', 'Slender / Thin'),
        ('AVERAGE', 'Average'),
        ('ATHLETIC', 'Athletic'),
        ('HEAVYSET', 'Heavyset'),
        ('SLIGHTLY HEAVY', 'A Few Extra Pounds'),
        ('STOCKY', 'Stocky'),
    )
    ASTROLOGICAL_SIGN = (
        ('NO ANSWER', 'NO ANSWER'),
        ('CAPRICORN', 'CAPRICORN'),
        ('AQUARIUS', 'AQUARIUS'),
        ('PISCES', 'PISCES'),
        ('ARIES', 'ARIES'),
        ('TAURUS', 'TAURUS'),
        ('GEMINI', 'GEMINI'),
        ('CANCER', 'CANCER'),
        ('LEO', 'LEO'),
        ('VIRGO', 'VIRGO'),
        ('LIBRA', 'LIBRA'),
        ('SCORPIO', 'SCORPIO'),
        ('SAGITTARIUS', 'SAGITTARIUS'),
    )
    RELATIONSHIP_STATUS = (
        ('NO ANSWER', 'NO ANSWER'),
        ('CURRENTLY SEPARATED', 'CURRENTLY SEPARATED'),
        ('DIVORCED', 'DIVORCED'),
        ('WIDOW / WIDOWER', 'WIDOW / WIDOWER'),
    )
    OCCUPATION = (

    )
    ETHNICITY = ()

    
