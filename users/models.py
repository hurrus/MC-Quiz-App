from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


def validate_email_address(value):
    if not value.endswith("@student.uni-halle.de"):
        raise ValidationError(_('Es sind nur studentische Emailadresse erlaubt!'))


class Profile(models.Model):
    #   user = models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, validators=[validate_email_address])
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    profession = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)

