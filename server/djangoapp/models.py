from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default="Specify Make")
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):

    # Many to One relationship with CarMake model
    car_make = models.ForeignKey(CarMake, on_delete = models.CASCADE)

    # Informations on CarModel Table
    name = models.CharField(null=False, max_length=30, default="Specify Model")
    dealer_id = models.IntegerField(default=1)

    HATCHBACK = "hatchback"
    SEDAN = "sedan"
    SUV = "suv"
    COUPE = "coupe"
    CONVERTIBLE = "convertible"
    WAGON = "wagon"
    SPORTS_CAR = "sports_car"
    OTHERS = "others"

    TYPE_CHOICES = [
        (HATCHBACK, "Hatchback"),
        (SEDAN, "Sedan"),
        (SUV, "Sports Utility Vehicle (SUV)"),
        (COUPE, "Coupe"),
        (CONVERTIBLE, "Convertible"),
        (WAGON, "Wagon"),
        (SPORTS_CAR, "Sports Car"),
        (OTHERS, "Others")
    ]

    car_type = models.CharField(null=False, max_length=30,\
         choices=TYPE_CHOICES, default=HATCHBACK)
    year = models.DateField()

    def __str__(self):
        return "Model Name : " + self.name + ", " \
                "Car Type : " + self.car_type 


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
