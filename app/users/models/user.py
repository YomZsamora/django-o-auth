import pytz
from datetime import datetime
from django.db import models
from core.settings import TIME_ZONE
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    email = models.EmailField(max_length=100, null=False, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    password = models.CharField(max_length=255)
    last_login = models.DateTimeField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    _password = None

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.email

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def refresh_last_login(self):
        self.last_login = datetime.now(tz=pytz.timezone(TIME_ZONE))
        self.save()

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)
