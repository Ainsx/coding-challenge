from django.db import models

# Create your models here.


class Todo(models.Model):
    # status choices
    STATUS_CHOICES = [
        # DB     Human
        ("NEW", "New"),
        ("IN_PROGRESS", "In progress"),
        ("DONE", "Done"),
    ]
    # text field for todo titles/ status field
    # python does not need data type
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True,
        default="Untitled",
        help_text="Enter your title here",
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="NEW")
    # stores time stamp when it was created
    created_at = models.DateTimeField(auto_now_add=True)

    # toString
    def __str__(self):  # current instance of the class
        return f"{self.title} ({self.status})"
