from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError("ENTER AN EMAIL BUDDY")
        if not username:
            raise ValueError("I KNOW YOU HAVE A NAME")
        if not password:
            raise ValueError("PASSWORD?!?!?!? HELLO??")

        user = self.model(username = username, email = self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)   # using=self._db to use default database
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("super user must have is_staff True")

        return self.create_user(username, email, password, **extra_fields)
