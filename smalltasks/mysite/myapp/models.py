from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.utils.translation import gettext as _
from django.core.validators import MaxValueValidator, MinValueValidator

ANIMAL_CHOICES = (
    (1, _("Badger - Барсук")),
    (2, _("Monkey - Обезьяна")),
    (3, _("Bear - Медведь")),
)

GENDER_CHOICES = (
    (1, _("Male")),
    (2, _("Female")),
    (3, _("Other")),
)


def get_display(key, listed_values):
    d = dict(listed_values)
    if key in d:
        return d[key]
    return None


class Animal(models.Model):
    animalType = models.IntegerField(choices=ANIMAL_CHOICES, default=1)
    animalName = models.CharField(max_length=50, blank=True, null=True)
    # animalAge = models.SmallIntegerField()
    animalAge = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)])
    animalArrivalDate = models.DateField(default=timezone.now())
    animalGender = models.IntegerField(choices=GENDER_CHOICES, default=3)

    def __str__(self):
        return "{} is a {}.".format(self.animalName, get_display(self.animalType, ANIMAL_CHOICES))


# {Animal.get__animalType__display} # return get_display(self.meal, CHOICES)


class Visitor(models.Model):
    visitorAge = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(120)])
    #   visitorAge = models.SmallIntegerField()
    visitorName = models.CharField(max_length=50, blank=True, null=True)
    visitorGender = models.IntegerField(choices=GENDER_CHOICES, default=3)

    def __str__(self):
        return "{} who is {} years old.".format(self.visitorName, self.visitorAge)


class Ticket(models.Model):
    readonly_fields = ('ticketValid',)
    ticketBought = models.DateField(default=timezone.now)
#    ticketValid = models.DateField(default=timezone.now)
#    ticketAgeCheck = models.BooleanField(default=False)
    ticketVisitor = models.ForeignKey(Visitor, on_delete=models.DO_NOTHING)

    def save(self, **kwargs):
        self.ticketValid = timezone.now() + timedelta(days=1)
        super().save(**kwargs)

    def __str__(self):
        if self.ticketVisitor.visitorAge > 8:
            return "Ticket No{} is bought at {} by {}".format(self.id, self.ticketBought, self.ticketVisitor)
        else:
            return "This ticket No. {} is reserved, parents should pay!".format(self.id)


class Visit(models.Model):
    visitedAnimal = models.ForeignKey(Animal, on_delete=models.DO_NOTHING, default=0)
    whoVisited = models.ForeignKey(Ticket, on_delete=models.DO_NOTHING, default=0)
    timeOfVisit = models.DateField(default=timezone.now())

    def __str__(self):
        return "Visit No.{} of {}: {} by {}, ticket No.{}.".format(self.id, self.visitedAnimal.animalName
                                                                   , get_display(self.visitedAnimal.animalType,
                                                                                 ANIMAL_CHOICES),
                                                                   self.whoVisited.ticketVisitor.visitorName,
                                                                   self.whoVisited.id)

# Create your models here.
