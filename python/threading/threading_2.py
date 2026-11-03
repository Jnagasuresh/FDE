# create our first thread
import threading
import time

def check_service(service_name):
    print(f"Checking {service_name}...")
    time.sleep(2)  # Simulate waiting for a response
    print(f"{service_name} is responding")


thread = threading.Thread(
    target=check_service,
    args=("Customer API",)
)
# thread object

thread.start() # Starts the thread

thread.join() # wait until the thread finishes.

print("Monitoring check completed")

'''
1. The main thread creates a new thread.
2. start() allows the new thread to execute check_service()
3. The new thread prints the first message and sleeps for two seconds.
4. Meanwhile, the main thread reaches join() and waits
5. The new thread wakes up and prints that the service is responding.
6. The new thread finishes
7. join() returns, and the main thread prints the final message.
'''