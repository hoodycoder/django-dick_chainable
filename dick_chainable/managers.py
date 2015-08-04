from django.db import models

class QuerySetManager(models.Manager):
    def get_queryset(self):
        return self.model.QuerySet(self.model)

    def __getattr__(self, attr, *args):
        return getattr(self.get_queryset(), attr, *args)
