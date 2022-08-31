from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

User = get_user_model()


class Profile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    nip = models.CharField(default=None,
                           max_length=10,
                           unique=True,
                           null=True,
                           blank=True,
                           validators=[RegexValidator(r'^\d{1,10}$')])
    regon = models.CharField(default=None,
                             max_length=9,
                             unique=True,
                             null=True,
                             blank=True,
                             validators=[RegexValidator(r'^\d{1,9}$')])
    street = models.CharField(default=None,
                              max_length=20,
                              null=True,
                              blank=True)
    city = models.CharField(default=None, max_length=20, null=True, blank=True)

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message=
        "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex],
                                    max_length=17,
                                    blank=True,
                                    null=True)

    def __str__(self):
        return self.user.username
