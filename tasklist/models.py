from django.db import models

class Tarefas(models.Model):
    STATUS = (
        ("Fazendo", "Fazendo"),
        ("Feito", "Feito")
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    select = models.CharField(
        max_length=10,
        choices=STATUS,
    )
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
