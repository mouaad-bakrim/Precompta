from django.db import models


class TenantQuerySet(models.QuerySet):
    def for_user(self, user):
        if user.is_superuser:
            return self

        return self.filter(
            organization__memberships__user=user,
            organization__memberships__is_active=True,
        ).distinct()


class TenantManager(models.Manager):
    def get_queryset(self):
        return TenantQuerySet(self.model, using=self._db)

    def for_user(self, user):
        return self.get_queryset().for_user(user)