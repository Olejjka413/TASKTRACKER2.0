from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, login, password=None):
        if not login:
            raise ValueError('User must have an login')

        user = self.model(login=login)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login, password):
        user = self.create_user(login=login, password=password)

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    login = models.CharField(verbose_name='Логин', max_length=50, unique=True)
    team = models.ForeignKey("task_tracker.Team", verbose_name='Команда', on_delete=models.CASCADE,  blank=True, null=True)

    is_admin = models.BooleanField(
        default=False, verbose_name='Администратор?')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False, verbose_name='Персонал')
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'login'

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return f'{self.login}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
