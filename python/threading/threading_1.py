# We are building a company monitoring service
# A customer database
# An external weather API
# An AI inference service

# sequential execution

import time

def read_customer():
    print("Reading customer record...")
    time.sleep(2) # blocking
    print("Customer record received")

def fetch_weather():
    print("Fetching weather...")
    time.sleep(3) # blocking
    print("Weather received")

def run_prediction():
    print("Running AI prediction...")
    time.sleep(2) # blocking
    print("Prediction completed")

start = time.perf_counter()

read_customer()
# time.sleep() blocks the thread
fetch_weather()
run_prediction()

end = time.perf_counter()

print(f"Total time: {end - start:.2f} seconds")