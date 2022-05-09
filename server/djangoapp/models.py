from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(null=False, max_length=30)
    description = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.Name + " " + self.Description
    


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
    Description = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.Name + " " + self.Description

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data



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