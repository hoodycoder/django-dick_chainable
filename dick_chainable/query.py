from django.db import models

class ExtendedQuerySet(models.query.QuerySet):
    def latest_or_none_expect_singular(self):
        try:
            return self.latest()
        except self.model.DoesNotExist:
            return None
    def latest_or_none_expect_multiple(self):
        try:
            return self.latest()
        except self.model.DoesNotExist, self.model.MultipleObjectsReturned:
            return None

    def earliest_or_none_expect_singular(self):
        try:
            return self.earliest()
        except self.model.DoesNotExist:
            return None
    def earliest_or_none_expect_multiple(self):
        try:
            return self.earliest()
        except self.model.DoesNotExist, self.model.MultipleObjectsReturned:
            return None

    def get_or_none_expect_singular(self):
        try:
            return self.get()
        except self.model.DoesNotExist:
            return None
    def get_or_none_expect_multiple(self):
        try:
            return self.get()
        except self.model.DoesNotExist, self.model.MultipleObjectsReturned:
            return None
