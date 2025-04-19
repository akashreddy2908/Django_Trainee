from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import threading

# Signal receiver function
@receiver(post_save, sender=User)
def my_signal_receiver(sender, instance, **kwargs):
    # This prints the thread ID where the signal handler is executed
    print(f"Signal Receiver Thread ID: {threading.get_ident()}")

# Main code where the signal is triggered
if __name__ == '__main__':
    from django.test import TestCase

    class SignalTestCase(TestCase):
        def test_signal_execution(self):
            # This prints the thread ID of the main thread
            print(f"Main Thread ID: {threading.get_ident()}")
            # This will trigger the signal
            User.objects.create(username="test_user", password="test_password")

'''In a regular Django setup,
signals like post_save run in the same thread as the request or the code that triggers the signal.
Since we are using Django's default settings (which are synchronous),
both the main thread and the signal receiver should have the same thread ID,
indicating they are executed in the same thread.'''
