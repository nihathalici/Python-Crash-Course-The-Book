18-2-Short-Entries.md
========================================================

The __str__() method in the Entry model currently appends an ellipsis to every instance of Entry when Django shows it in the admin site or the shell. Add an if statement to the __str__() method that adds an ellipsis only if the entry is longer than 50 characters. Use the admin site to add an entry that’s fewer than 50 characters in length, and check that it doesn’t have an ellipsis when viewed.

```python3
class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    # Modified __str__ method 
    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return f"{self.text}."
```
