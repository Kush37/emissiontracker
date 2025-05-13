from codecarbon import EmissionsTracker
import time

# tracker = EmissionsTracker()
tracker = EmissionsTracker(save_to_file=False, prometheus_url="localhost:5000/metrics")

for i in range(1,5):
    print("Hello")
    tracker.start()
    time.sleep(1)
    tracker.stop()
    # print(dir(tracker))
    print('*---------------------------------------------*')
    print(tracker.final_emissions_data)
    print('*----------------Emission Rate-----------------------------*')
    print(tracker._previous_emissions.emissions_rate)
    print('*-------------------Energy Consumed--------------------------*')
    print(tracker._previous_emissions.energy_consumed)

    print(tracker._previous_emissions.emissions_rate/tracker._previous_emissions.energy_consumed)
    # print(tracker.final_emissions_data.emissions_rate/tracker.final_emissions_data.energy_consumed)
    
    # print(tracker._emissions.emissions_rate/tracker._emissions.energy_consumed)


