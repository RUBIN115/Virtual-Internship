from datetime import datetime
from django.db import IntegrityError, models
from django.core.validators import RegexValidator

"""
Users model 
"""
class Users(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{7,15}$', message="Phone number must be entered in the format: '+799999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name

"""
Perevals model
"""
class Pereval(models.Model):

    NEW = 'new'
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'

    CHOICES_MODER = [
        (NEW, 'new'),
        (PENDING, 'pending'),
        (ACCEPTED, 'accepted'),
        (REJECTED, 'rejected'), 
    ]

    beauty_title = models.CharField(max_length=30, null=False)
    title = models.CharField(max_length=30, null=False)
    other_titles = models.CharField(max_length=30, null=False)
    connect = models.CharField(max_length=30, null=True)
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    status = models.CharField(max_length=8, choices=CHOICES_MODER, default=NEW)
    coord = models.ForeignKey('Coordinate', on_delete=models.CASCADE)
    image = models.ForeignKey('Image', on_delete=models.CASCADE)
    level = models.ForeignKey('Level', on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def __str__(self) -> str:
        return f'{self.beauty_title} {self.title} {self.other_titles} id: {self.pk}'

"""
Images model
"""
class Image(models.Model):
    title = models.CharField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"id: {self.pk} title:{self.title} {self.image}"

"""
Coordnate model
"""
class Coordinate(models.Model):
    latitude = models.DecimalField(verbose_name='Latitude', max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(verbose_name='Longitude', max_digits=9, decimal_places=6, null=True)
    height = models.IntegerField(verbose_name='Height', null=True)

    def __str__(self) -> str:
        return f'{self.latitude} {self.longitude} {self.height}'


"""
Areas model
"""
class Area(models.Model):
    parent = models.IntegerField(null=True)
    title = models.CharField(max_length=30, null=True)


"""
Actvity type model
"""
class Activity_types(models.Model):
    title = models.CharField(max_length=30, null=True)

"""
Levels model
"""
class Level(models.Model):
    winter = models.CharField(max_length=10, verbose_name='Winter', null=True, blank=True)
    summer = models.CharField(max_length=10, verbose_name='Summer', null=True, blank=True)
    autumn = models.CharField(max_length=10, verbose_name='Autumn', null=True, blank=True)
    spring = models.CharField(max_length=10, verbose_name='Spring', null=True, blank=True)

    def __str__(self):
        return f'{self.winter} {self.summer} {self.autumn} {self.spring}'