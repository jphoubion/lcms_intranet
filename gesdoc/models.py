from django.db import models

class DocumentCategories(models.Model):

    name = models.CharField(verbose_name="Nom", max_length=100)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Document categories'

    def __str__(self):
        return self.name
class Documents(models.Model):

    name = models.CharField(verbose_name="Nom", max_length=255)
    description = models.TextField(verbose_name="Description")
    category = models.ForeignKey(DocumentCategories, verbose_name="Catégorie", related_name="category",
                                 on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Documents'

    def __str__(self):
        return self.name