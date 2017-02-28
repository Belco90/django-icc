from django.db import models
from django.utils.translation import ugettext_lazy as _


class TicketCategory(models.Model):
    name = models.CharField(_("Name"), max_length=30, db_index=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='subcategories',
        related_query_name='subcategories',
    )

    class Meta:
        ordering = ['parent__name', 'name', ]
        unique_together = ('name', 'parent')
        verbose_name = _("ticket category")
        verbose_name_plural = _("ticket categories")

    def __str__(self):
        return self.name
