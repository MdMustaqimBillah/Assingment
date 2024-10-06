from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
import time
import threading
from SignalApp.models import TestModel

# Question 1: Synchronous execution
@receiver(post_save, sender=TestModel)
def slow_signal_handler(sender, instance, created, **kwargs):
    time.sleep(5)  # Simulate a time-consuming operation
    print(f"Signal handler executed for {instance.name}")

def test_synchronous_signal():
    start_time = time.time()
    TestModel.objects.create(name="Test Object")
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time} seconds")

# Question 2: Thread execution
@receiver(post_save, sender=TestModel)
def thread_signal_handler(sender, instance, created, **kwargs):
    current_thread = threading.current_thread()
    print(f"Signal handler running in thread: {current_thread.name}")

def test_signal_thread():
    current_thread = threading.current_thread()
    print(f"Main execution running in thread: {current_thread.name}")
    TestModel.objects.create(name="Thread Test Object")

# Question 3: Transaction execution
@receiver(post_save, sender=TestModel)
def transaction_signal_handler(sender, instance, created, **kwargs):
    # This will raise an exception
    TestModel.objects.create(name="Signal Object")

def test_transaction():
    try:
        with transaction.atomic():
            TestModel.objects.create(name="Transaction Test Object")
    except Exception as e:
        print(f"Exception caught: {e}")
    
    print(f"Number of objects in database: {TestModel.objects.count()}")



    # Answer to the Question - 4 [ Rectangle Class ]

class Rectangle:
   def __init__(self, length: int, width: int):
       self.length = length
       self.width = width
    
   def __iter__(self):
       yield {'length': self.length}
       yield {'width': self.width}

# Usage:
rect = Rectangle(2, 2)
for item in rect:
    print(item)

# Output:
# {'length': 5}
# {'width': 3}