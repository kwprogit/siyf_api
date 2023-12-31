from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from config import settings


class Language(models.TextChoices):
    UZB = 'uz', "O'zbek"
    RUS = 'ru', "Русский"
    ENG = 'en', 'English'



class Admin(AbstractUser):
    # raw_password = models.TextField()
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)

    def has_usable_password(self) -> bool:
        return False


class HeaderNews(models.Model):
    lang_code = models.CharField(
            max_length=2,
            choices=Language.choices,
            default=Language.UZB, 
            verbose_name="Язык плаката"
        )
    first_header = models.TextField(
            verbose_name='Загаловок первой карточки'
        )
    first_text = models.TextField(
            verbose_name='Текст первой карточки'
        )
    second_header = models.TextField(
            verbose_name='Загаловок второй карточки'
        )
    second_text = models.TextField(
            verbose_name='Текст второй карточки'
        )
    image = models.ImageField(
            upload_to=settings.IMAGE_ROOT,
            verbose_name='Фото плаката'
        )
    main_title = models.TextField(
            verbose_name='Загаловок плаката'
        )

    def __str__(self) -> str:
        return self.main_title
    
    class Meta:
        verbose_name = "Плакат"
        verbose_name_plural = "Плакаты"






class News(models.Model):
    lang_code = models.CharField(
            max_length=2,
            choices=Language.choices,
            default=Language.UZB, 
            verbose_name="Язык плаката"
        )
    image = models.ImageField(
            upload_to=settings.IMAGE_ROOT,
            verbose_name='Фотография для новости'
        )
    text = models.TextField(
        verbose_name='Контент новости'
    )

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural ='Новости'

    def __str__(self) -> str:
        return self.text






class Feedback(models.Model):
    title = models.TextField(
            verbose_name = "Загаловок отзыва", 
            null=True , 
            blank=True
        )
    
    email = models.EmailField(
            verbose_name ='Электронная почта отзывателя'
        )
    phone = models.TextField(
            verbose_name = "Номер телефона отзывателя", 
            null=True , 
            blank=True
        )
    feedback = models.TextField(
        verbose_name = "Текст отзыва"
    )
    created_at = models.DateTimeField(
            auto_now_add=True,
            verbose_name = "Дата и время отзыва"
        )
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self) -> str:
        out =  self.created_at.strftime("%d %B %Yг, %H:%M")
        months = {
            "January": "Января",
            "February": "Февраля",
            "March": "Марта",
            "April": "Апреля",
            "May": "Мая",
            "June": "Июня",
            "July": "Июля",
            "August": "Августа",
            "September": "Сентября",
            "October": "Октября",
            "November": "Ноября",
            "December": "Декабря"
        }
        for english, russian in months.items():
            out.replace(english, russian)
        return out




class Employee(models.Model):
    lang_code = models.CharField(
            max_length=2,
            choices=Language.choices,
            default=Language.UZB, 
            verbose_name="Язык плаката"
        )
    fullname = models.CharField(
            max_length = 255 , 
            verbose_name  = "Полное имя сотрудника"
        )
    description = models.TextField(
            verbose_name = "О сотруднике"
        )
    image = models.ImageField(
            upload_to=settings.IMAGE_ROOT, 
            verbose_name="Фото сотрудника"
        )
    
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудник'
    
    def __str__(self) -> str:
        return self.fullname
    



class Sponsor(models.Model):
    name = models.TextField(
            verbose_name = "Имя спонсора",
            unique=True
        )
    image = models.ImageField(
            upload_to=settings.IMAGE_ROOT, 
            verbose_name="Фото спонсора"
        )
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Спонсор"
        verbose_name_plural = "Спонсоры"