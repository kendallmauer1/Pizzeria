from django.db import models

# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length=100)
    #pizza_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.pizza_name
    
class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        return self.topping_name
    
class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.pizza.name} - {self.time}"