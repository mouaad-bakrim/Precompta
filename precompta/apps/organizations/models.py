from django.conf import settings
from django.db import models
from apps.core.models import TimeStampedModel


class Organization(TimeStampedModel):
    name = models.CharField(max_length=255)
    ice = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    address = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Membership(TimeStampedModel):
    class Role(models.TextChoices):
        OWNER = "owner", "Owner"
        MANAGER = "manager", "Manager"
        ACCOUNTANT = "accountant", "Accountant"
        ASSISTANT = "assistant", "Assistant"
        CLIENT = "client", "Client"

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="memberships",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="memberships",
    )
    role = models.CharField(max_length=30, choices=Role.choices)
    is_active = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["organization", "user"],
                name="unique_membership_per_organization_user",
            )
        ]

    def __str__(self):
        return f"{self.user} - {self.organization} - {self.role}"