# -*- coding: utf-8 -*-

from django.db import models


class Registrant(models.Model):
    """Model to handle the registrants
    for  hackathons """

    OCCUPATION_CHOICES = (
        (1, 'Elev'),
        (2, 'Student'),
        (3, 'Profesionist'),
    )
    EXPERIENCE_CHOICES = (
        (1, 'Abia încep'),
        (2, 'Mai puţin de un an'),
        (3, '1-2 ani'),
        (4, '3-5 ani'),
        (5, '5+ ani'),
    )
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField()
    occupation = models.CharField(max_length=1, choices=OCCUPATION_CHOICES)
    experience = models.CharField(max_length=1, choices=EXPERIENCE_CHOICES)
    institution = models.TextField(null=True, blank=True)
    email = models.EmailField()
