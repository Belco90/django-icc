from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _


class TicketCategory(models.Model):
    ERROR_SUBCATEGORY_CANNOT_BE_CHILD_OF_SUBCATEGORY = _("Subcategory cannot be child of another Subcategory.")

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

    def clean(self):
        # If self is subcategory then check it is related to main category, not to another subcategory
        if self.is_subcategory and self.parent.is_subcategory:
            raise ValidationError({'parent': [self.ERROR_SUBCATEGORY_CANT_BE_RELATED_TO_SUBCATEGORY]})

    @property
    def is_main_category(self):
        return self.parent is None

    @property
    def is_subcategory(self):
        return self.parent is not None

    def is_parent_of(self, subcategory):
        return subcategory in self.susubcategories.all()
