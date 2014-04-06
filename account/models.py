from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    birth_date = models.DateField(blank=True)
    # Weight in pounds
    weight = models.IntegerField(blank=True)
    # Height in inches
    height = models.IntegerField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICES)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    EDUCATION_LEVEL = (
        (None, 'No Answer'),
        ('HIGH SCHOOL', 'High School'),
        ('SOME COLLEGE', 'Some College'),
        ('ASSOCIATES', 'Associates Degree'),
        ('BACHELORS', 'Bachelors Degree'),
        ('GRADUATE', 'Graduate / Professional Degree'),
    )
    HAIR_COLOR = (
        (None, 'No Answer'),
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
        (None, 'No Answer'),
        ('BLACK', 'Black'),
        ('BLUE', 'Blue'),
        ('BROWN', 'Brown'),
        ('GREY', 'Grey'),
        ('GREEN', 'Green'),
        ('HAZEL', 'Hazel'),
    )
    BODY_TYPE = (
        (None, 'No Answer'),
        ('SLENDER', 'Slender / Thin'),
        ('AVERAGE', 'Average'),
        ('ATHLETIC', 'Athletic'),
        ('HEAVYSET', 'Heavyset'),
        ('SLIGHTLY HEAVY', 'A Few Extra Pounds'),
        ('STOCKY', 'Stocky'),
    )
    ASTROLOGICAL_SIGN = (
        (None, 'No Answer'),
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
    RELATIONSHIP_STATUS = (
        (None, 'No Answer'),
        ('CURRENTLY SEPARATED', 'Currently Separated'),
        ('DIVORCED', 'Divorced'),
        ('WIDOWED', 'Widow / Widower'),
    )
    OCCUPATION = (
        (None, 'No Answer'),
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
    HAVE_KIDS = (
        (None, 'No Answer'),
        ('YES', 'Yes'),
        ('NO', 'No'),
    )
    have_kids_num = models.IntegerField(blank=True)
    WANT_KIDS = (
        (None, 'No Answer'),
        ('YES', 'Yes'),
        ('NO', 'No'),
    )
    want_kids_num = models.IntegerField(blank=True)
    SMOKE = (
        (None, 'No Answer'),
        ('NO', 'No'),
        ('OCCASIONAL', 'Occasionally'),
        ('DAILY', 'Daily'),
        ('QUITTING', 'Yes, But Trying To Quit'),
    )
    DRINK = (
        (None, 'No Answer'),
        ('NEVER', 'Never'),
        ('SOCIAL', 'Social Drinker'),
        ('REGULAR', 'Regularly'),
    )
    EXERCISE = (
        (None, 'No Answer'),
        ('MODERATE', '1-3 Times Per Week'),
        ('FIEND', '4-5 Times Per Week'),
    )
    ETHNICITY = (
        (None, 'No Answer'),
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
    RELIGION = (
        (None, 'No Answer'),
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
    POLITICS = (
        (None, 'No Answer'),
        ('CONSERVATIVE', 'Conservative'),
        ('MODERATE', 'Moderate'),
        ('LIBERAL', 'Liberal'),
        ('NONCONFORMIST', 'Non-Conformist'),
        ('OTHER', 'Other'),
    )
    HAVE_PETS = (
        (None, 'No Answer'),
        ('NO', 'No'),
        ('YES', 'Yes'),
    )
    LIKE_PETS = (
        (None, 'No Answer'),
        ('NO', 'No'),
        ('YES', 'Yes'),
    )

    
