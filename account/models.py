from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    birth_date = models.DateField(blank=True, null=True)
    # Weight in pounds
    weight = models.IntegerField(blank=True, null=True)
    # Height in inches
    height = models.IntegerField(blank=True, null=True)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    gender = models.CharField(max_length=10,
                                choices=GENDER_CHOICES,
                                blank=True, null=True)
    EDUCATION_LEVEL_CHOICES = (
        ('', 'No Answer'),
        ('HIGH SCHOOL', 'High School'),
        ('SOME COLLEGE', 'Some College'),
        ('ASSOCIATES', 'Associates Degree'),
        ('BACHELORS', 'Bachelors Degree'),
        ('GRADUATE', 'Graduate / Professional Degree'),
    )
    education_level = models.CharField(max_length=30,
                                choices=EDUCATION_LEVEL_CHOICES,
                                blank=True, null=True)
    HAIR_COLOR_CHOICES = (
        ('', 'No Answer'),
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
    hair_color = models.CharField(max_length=30,
                                choices=HAIR_COLOR_CHOICES,
                                blank=True, null=True)
    EYE_COLOR_CHOICES = (
        ('', 'No Answer'),
        ('BLACK', 'Black'),
        ('BLUE', 'Blue'),
        ('BROWN', 'Brown'),
        ('GREY', 'Grey'),
        ('GREEN', 'Green'),
        ('HAZEL', 'Hazel'),
    )
    eye_color = models.CharField(max_length=30,
                                choices=EYE_COLOR_CHOICES,
                                blank=True, null=True)
    BODY_TYPE_CHOICES = (
        ('', 'No Answer'),
        ('SLENDER', 'Slender / Thin'),
        ('AVERAGE', 'Average'),
        ('ATHLETIC', 'Athletic'),
        ('HEAVYSET', 'Heavyset'),
        ('SLIGHTLY HEAVY', 'A Few Extra Pounds'),
        ('STOCKY', 'Stocky'),
    )
    body_type = models.CharField(max_length=30,
                                choices=BODY_TYPE_CHOICES,
                                blank=True, null=True)
    ASTROLOGICAL_SIGN_CHOICES = (
        ('', 'No Answer'),
        ('CAPRICORN', 'Capricorn'),
        ('AQUARIUS', 'Aquarius'),
        ('PISCES', 'Pisces'),
        ('ARIES', 'Aries'),
        ('TAURUS', 'Taurus'),
        ('GEMINI', 'Gemini'),
        ('CANCER', 'Cancer'),
        ('LEO', 'Leo'),
        ('VIRGO', 'Virgo'),
        ('LIBRA', 'Libra'),
        ('SCORPIO', 'Scorpio'),
        ('SAGITTARIUS', 'Sagittarius'),
    )
    astrological_sign = models.CharField(max_length=30,
                                choices=ASTROLOGICAL_SIGN_CHOICES,
                                blank=True, null=True)
    RELATIONSHIP_STATUS_CHOICES = (
        ('', 'No Answer'),
        ('CURRENTLY SEPARATED', 'Currently Separated'),
        ('DIVORCED', 'Divorced'),
        ('WIDOWED', 'Widow / Widower'),
    )
    relationship_status = models.CharField(max_length=30,
                                choices=RELATIONSHIP_STATUS_CHOICES,
                                blank=True, null=True)
    OCCUPATION_CHOICES = (
        ('', 'No Answer'),
        ('ADMINISTRATIVE', 'Administrative / Secretarial'),
        ('ARTISTIC', 'Artistic / Creative / Performance'),
        ('EXECUTIVE', 'Executive / Management'),
        ('FINANCE', 'Financial / Accounting / Real Estate'),
        ('LABOR', 'Labor / Construction'),
        ('LEGAL', 'Legal'),
        ('HEALTH', 'Medical / Dental / Veterinary / Fitness'),
        ('GOVERNMENT', 'Political / Government / Civil Service / Military'),
        ('RETAIL', 'Retail'),
        ('RETIRED', 'Retired'),
        ('MARKETING', 'Sales / Marketing'),
        ('SELF EMPLOYED', 'Self-Employed / Entrepreneur'),
        ('STUDENT', 'Student'),
        ('EDUCATION', 'Education / Teacher / Professor'),
        ('TECHNICAL', 'Technical / Science / Computers / Engineering'),
        ('HOSPITALITY', 'Travel / Hospitality / Transportation'),
        ('OTHER', 'Other Profession'),
        ('NONPROFIT', 'Nonprofit / Volunteer / Activist'),
        ('LAW ENFORCEMENT', 'Law Enforcement / Security / Military'),
        ('FASHION', 'Fashion / Model / Beauty'),
        ('ARCHITECTURE', 'Architecture / Interior Design'),
    )
    occupation = models.CharField(max_length=50,
                                choices=OCCUPATION_CHOICES,
                                blank=True, null=True)
    HAVE_KIDS_CHOICES = (
        ('', 'No Answer'),
        ('YES', 'Yes'),
        ('NO', 'No'),
    )
    have_kids = models.CharField(max_length=30,
                                choices=HAVE_KIDS_CHOICES,
                                blank=True, null=True)
    have_kids_num = models.IntegerField(blank=True, null=True)
    WANT_KIDS_CHOICES = (
        ('', 'No Answer'),
        ('YES', 'Yes'),
        ('NO', 'No'),
    )
    want_kids = models.CharField(max_length=30,
                                choices=WANT_KIDS_CHOICES,
                                blank=True, null=True)
    want_kids_num = models.IntegerField(blank=True, null=True)
    SMOKE_CHOICES = (
        ('', 'No Answer'),
        ('NO', 'No'),
        ('OCCASIONAL', 'Occasionally'),
        ('DAILY', 'Daily'),
        ('QUITTING', 'Yes, But Trying To Quit'),
    )
    smoke = models.CharField(max_length=30,
                                choices=SMOKE_CHOICES,
                                blank=True, null=True)
    DRINK_CHOICES = (
        ('', 'No Answer'),
        ('NEVER', 'Never'),
        ('SOCIAL', 'Social Drinker'),
        ('REGULAR', 'Regularly'),
    )
    drink = models.CharField(max_length=30,
                                choices=DRINK_CHOICES,
                                blank=True, null=True)
    EXERCISE_CHOICES = (
        ('', 'No Answer'),
        ('MODERATE', '1-3 Times Per Week'),
        ('FIEND', '4-5 Times Per Week'),
    )
    exercise = models.CharField(max_length=30,
                                choices=EXERCISE_CHOICES,
                                blank=True, null=True)
    ETHNICITY_CHOICES = (
        ('', 'No Answer'),
        ('ASIAN', 'Asian'),
        ('BLACK', 'Black / African Descent'),
        ('EAST INDIAN', 'East Indian'),
        ('HISPANIC', 'Latino / Hispanic'),
        ('MIDDLE EASTERN', 'Middle Eastern'),
        ('NATIVE AMERICAN', 'Native American'),
        ('PACIFIC ISLANDER', 'Pacific Islander'),
        ('CAUCASIAN', 'White / Caucasian'),
        ('OTHER', 'Other'),
    )
    ethnicity = models.CharField(max_length=30,
                                choices=ETHNICITY_CHOICES,
                                blank=True, null=True)
    RELIGION_CHOICES = (
        ('', 'No Answer'),
        ('AGNOSTIC', 'Agnostic'),
        ('ATHEIST', 'Atheist'),
        ('BUDDHIST', 'Buddhist'),
        ('CATHOLIC', 'Christian / Catholic'),
        ('LDS', 'Christian / LDS'),
        ('PROTESTANT', 'Christian / Protestant'),
        ('HINDU', 'Hindu'),
        ('JEWISH', 'Jewish'),
        ('ISLAM', 'Muslim / Islam'),
        ('SPIRITUAL', 'Spirital But Not Religious'),
        ('OTHER', 'Other'),
        ('OTHER CHRISTIAN', 'Christian / Other'),
    )
    religion = models.CharField(max_length=30,
                                choices=RELIGION_CHOICES,
                                blank=True, null=True)
    POLITICS_CHOICES = (
        ('', 'No Answer'),
        ('CONSERVATIVE', 'Conservative'),
        ('MODERATE', 'Moderate'),
        ('LIBERAL', 'Liberal'),
        ('NONCONFORMIST', 'Non-Conformist'),
        ('OTHER', 'Other'),
    )
    politics = models.CharField(max_length=30,
                                choices=POLITICS_CHOICES,
                                blank=True, null=True)
    HAVE_PETS_CHOICES = (
        ('', 'No Answer'),
        ('NO', 'No'),
        ('YES', 'Yes'),
    )
    have_pets = models.CharField(max_length=30,
                                choices=HAVE_PETS_CHOICES,
                                blank=True, null=True)
    LIKE_PETS_CHOICES = (
        ('', 'No Answer'),
        ('NO', 'No'),
        ('YES', 'Yes'),
    )
    like_pets = models.CharField(max_length=30,
                                choices=LIKE_PETS_CHOICES,
                                blank=True, null=True)




