from django.db import models

class Client(models.Model):
    
    # Creating the client table
    name = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.name

class Purchase(models.Model):
    
    # Creating the pruchase using data from the purchase table

    # Choicefields
    payment_methods = (
        ('Cash','Cash'),
        ('Credit Card','Credit Card')
    )

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    price = models.FloatField(null=True, verbose_name='price')
    purchase_date = models.DateField()
    payment_methods = models.CharField(choices=payment_methods, max_length=20, null=True)

    def __str__(self):
        return self.name
