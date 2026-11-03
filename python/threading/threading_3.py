# create our first thread
import threading
import time

def check_service(service_name):
    print(f"Checking {service_name}...")
    time.sleep(2)  # Simulate waiting for a response
    print(f"{service_name} is responding")

start = time.perf_counter()

threads = []

services = [
    "Customer API",
    "Payment API",
    "Inventory API"
]

for service in services:
    thread = threading.Thread(
        target=check_service,
        args=(service,)
    )

    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

elapsed = time.perf_counter() - start


print(f"All checks completed in {elapsed:.2f} seconds")

print("Monitoring check completed")