from django.db import models
from django.utils import timezone

class FlightManager(models.Manager):
    def cheapest(self):
        return self.order_by('price').filter(date__gt=timezone.now())


class WayManager(models.Manager):
    def org(self):
        return self.order_by('origion')
