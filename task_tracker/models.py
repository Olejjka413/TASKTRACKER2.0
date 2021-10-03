from django.db import models

class Team(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

class Current(models.Model):
    team = models.ForeignKey(Team, verbose_name='Команда', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Название', max_length=50)
    description = models.TextField(verbose_name="Описание")
    date = models.CharField(verbose_name='Дедлайн', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Нынешняя задача'
        verbose_name_plural = 'Нынешние задачи'


class Failed(models.Model):
    team = models.ForeignKey(Team, verbose_name='Команда', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Название', max_length=50)
    description = models.TextField(verbose_name="Описание")
    date = models.CharField(verbose_name='Дедлайн', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проваленная задача'
        verbose_name_plural = 'Проваленные задачи'


class Finished(models.Model):
    team = models.ForeignKey(Team, verbose_name='Команда', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Название', max_length=50)
    description = models.TextField(verbose_name="Описание")
    date = models.CharField(verbose_name='Дедлайн', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Выполненная задача'
        verbose_name_plural = 'Выполненные задачи'



class Planned(models.Model):
    team = models.ForeignKey(Team, verbose_name='Команда', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Название', max_length=50)
    description = models.TextField(verbose_name="Описание")
    date = models.CharField(verbose_name='Дедлайн', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запланированная задача'
        verbose_name_plural = 'Запланированные задачи'