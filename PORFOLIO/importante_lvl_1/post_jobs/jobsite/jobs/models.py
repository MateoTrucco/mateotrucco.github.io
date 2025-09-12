from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator, MinLengthValidator, MaxLengthValidator

# Create your models here.
class Job(models.Model):
    title = models.CharField(
        max_length=30,
        default="Trabajo",
        validators=[
            MinLengthValidator(5, message='El título debe tener al menos 5 caracteres.'),
            RegexValidator(
                regex=r'^[A-Za-záéíóúÁÉÍÓÚñÑ\s]+$',
                message='El título solo puede contener letras y espacios.'
            )
        ]
    )
    description = models.TextField(
        default="Descripción",
        validators=[
            MinLengthValidator(10, message='La descripción debe tener al menos 10 caracteres.'),
            RegexValidator(
                regex=r'^[A-Za-z0-9áéíóúÁÉÍÓÚñÑ\s.,;:!?@"\'-]+$',
                message='La descripción no puede contener caracteres especiales, solo .,;:!?"\'-'
            )
        ]
    )
    date_posted = models.DateField(auto_now_add=True)
    required_age = models.IntegerField(default=17, validators=[
        MinValueValidator(17, message='La edad mínima permitida es 17 años.'),
        MaxValueValidator(99, message='La edad máxima permitida es 99 años.')
    ])
    contact_number = models.CharField(default="1234567890", max_length=10, validators=[
        RegexValidator(regex=r'^\d{10}$', message='El número de teléfono debe tener 10 dígitos numéricos.')
    ])

    def __str__(self):
        return self.title
