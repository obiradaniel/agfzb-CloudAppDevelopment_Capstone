from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    #id = models.BigAutoField(primary_key=True)
    name = models.CharField(null=False, max_length=30)
    description = models.CharField(max_length=1000)
    Toyota = "Toyota"
    Volkswagen = "Volkswagen"
    Mitsubishi = "Mitsubishi"
    Ford = "Ford"
    Nissan = "Nissan"
    Honda = "Honda"
    Hyundai = "Hyundai"
    Suzuki = "Suzuki"
    Mazda = "Mazda"
    Subaru = "Subaru"
    manufacturer_choices = [
    (Toyota,"Toyota"),
    (Volkswagen, "Volkswagen"),
    (Mitsubishi, "Mitsubishi"),
    (Ford, "Ford"),
    (Nissan, "Nissan"),
    (Honda, "Honda"),
    (Hyundai, "Hyundai"),
    (Suzuki, "Suzuki"),
    (Mazda, "Mazda"),
    (Subaru, "Subaru")]
    manufacturer = models.CharField(max_length=20, choices=manufacturer_choices, default=Toyota)

    def __str__(self):
        return self.manufacturer + " "+ self.name + " " + self.description

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=30)
    description = models.CharField(max_length=1000)
    dealer_id = models.IntegerField(null=False)
    Sedan = "Sedan" 
    SUV = "Volkswagen" 
    Truck = "Truck" 
    MiniVan  = "MiniVan" 
    Van = "Van" 
    Bus = "Bus" 
    MiniBus = "MiniBus" 
    Bus = "Bus" 
    Wagon = "Wagon" 
    Pick_up = "Pick Up"
    cartype_choices = [
    (Sedan,"Sedan"),
    (SUV, "SUV"),
    (Truck, "Truck"),
    (MiniVan, "MiniVan"),
    (Van, "Van"),
    (Bus, "Bus"),
    (MiniBus, "MiniBus"),
    (Wagon, "Wagon"),
    (Pick_up, "Pick Up")]
    car_type = models.CharField(null=False, max_length=20, choices=cartype_choices, default=Sedan)
    year = models.DateField(null=False)
    # steering
    # transmission
    # four_wheel
    # fuel
    # price
    # condition
    # engine_model
    # engine_capacity_
    # doors
    # passengers
    # color_exterior
    # weight

    
    def __str__(self):
        return self.name + " " + self.description + " " + str(self.year)

# <HINT> Create a plain Python class `CarDealer` to hold dealer data

class CarDealer:
    def __init__(self, id, city, state, st, address, zip, lat, long, short_name, full_name, totalreviews=0):
        self.id = id
        self.city = city
        self.state = state
        self.st = st
        self.address = address
        self.zip = zip
        self.lat = lat
        self.long = long
        self.short_name = short_name
        self.full_name = full_name
        self.totalreviews = totalreviews

    def __str__(self):
        return str(self.full_name) + ", Id: " + str(self.id) + ", " + str(self.city) + ", " + str(self.st)

false = False
# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:
    def __init__(self, id, name, dealership, review, purchase, purchase_date, car_make, car_model, car_year, another="another", sentiment=None):
        self.id=id
        self.name=name
        self.dealership=dealership
        self.review=review
        self.purchase=purchase
        self.purchase_date=purchase_date
        self.car_make=car_make
        self.car_model=car_model
        self.car_year=car_year
        self.another=another
        self.sentiment=sentiment

    def __str__(self):
        return self.review + " " + self.car_model + " by " + self.name + ": " + self.sentiment.title()


django_model_fields_rels_etc = ['Aggregate',
 'AutoField',
 'Avg',
 'BLANK_CHOICE_DASH',
 'BigAutoField',
 'BigIntegerField',
 'BinaryField',
 'BooleanField',
 'CASCADE',
 'Case',
 'CharField',
 'CheckConstraint',
 'Choices',
 'CommaSeparatedIntegerField',
 'Count',
 'DEFERRED',
 'DO_NOTHING',
 'DateField',
 'DateTimeField',
 'DecimalField',
 'Deferrable',
 'DurationField',
 'EmailField',
 'Empty',
 'Exists',
 'Expression',
 'ExpressionList',
 'ExpressionWrapper',
 'F',
 'Field',
 'FileField',
 'FilePathField',
 'FilteredRelation',
 'FloatField',
 'ForeignKey',
 'ForeignObject',
 'ForeignObjectRel',
 'Func',
 'GenericIPAddressField',
 'IPAddressField',
 'ImageField',
 'Index',
 'IntegerChoices',
 'IntegerField',
 'JSONField',
 'Lookup',
 'Manager',
 'ManyToManyField',
 'ManyToManyRel',
 'ManyToOneRel',
 'Max',
 'Min',
 'Model',
 'NOT_PROVIDED',
 'NullBooleanField',
 'ObjectDoesNotExist',
 'OneToOneField',
 'OneToOneRel',
 'OrderBy',
 'OrderWrt',
 'OuterRef',
 'PROTECT',
 'PositiveBigIntegerField',
 'PositiveIntegerField',
 'PositiveSmallIntegerField',
 'Prefetch',
 'ProtectedError',
 'Q',
 'QuerySet',
 'RESTRICT',
 'RestrictedError',
 'RowRange',
 'SET',
 'SET_DEFAULT',
 'SET_NULL',
 'SlugField',
 'SmallAutoField',
 'SmallIntegerField',
 'StdDev',
 'Subquery',
 'Sum',
 'TextChoices',
 'TextField',
 'TimeField',
 'Transform',
 'URLField',
 'UUIDField',
 'UniqueConstraint',
 'Value',
 'ValueRange',
 'Variance',
 'When',
 'Window',
 'WindowFrame',
 'aggregates',
 'aggregates_all',
 'base',
 'constants',
 'constraints',
 'constraints_all',
 'deletion',
 'enums',
 'enums_all',
 'expressions',
 'fields',
 'fields_all',
 'functions',
 'indexes',
 'indexes_all',
 'lookups',
 'manager',
 'options',
 'prefetch_related_objects',
 'query',
 'query_utils',
 'signals',
 'sql',
 'utils']