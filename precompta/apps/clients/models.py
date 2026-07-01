from django.db import models
from apps.core.models import OrganizationScopedModel
from apps.core.querysets import TenantManager


class Client(OrganizationScopedModel):
    class TvaRegime(models.TextChoices):
        MONTHLY = "monthly", "Mensuelle"
        QUARTERLY = "quarterly", "Trimestrielle"
        EXEMPT = "exempt", "Exonéré"

    company_name = models.CharField(max_length=255)
    ice = models.CharField(max_length=50, blank=True)
    if_number = models.CharField(max_length=50, blank=True)
    rc = models.CharField(max_length=50, blank=True)
    cnss = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)

    tva_regime = models.CharField(
        max_length=30,
        choices=TvaRegime.choices,
        default=TvaRegime.QUARTERLY,
    )

    is_active = models.BooleanField(default=True)

    objects = TenantManager()

    class Meta:
        indexes = [
            models.Index(fields=["organization", "company_name"]),
            models.Index(fields=["organization", "ice"]),
            models.Index(fields=["organization", "is_active"]),
        ]

    def __str__(self):
        return self.company_name