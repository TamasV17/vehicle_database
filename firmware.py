import os
import yaml

def find_vehicles_with_back_radar(folder):
    #This list will stands for to store the vehicles where the firmware version of the back radar (B_LRR_C) is
    #older than 1.4
    vehicles_with_back_radar = []

    print(f"Looking in: {folder}")
    #Iterate in the folder
    for vehicle in os.listdir(folder):
        #Construct the full path to each item
        vehicle_path = os.path.join(folder, vehicle)
        #Debug: which vehicle folder is being checked
        print(f"Checking folder: {vehicle}")
        #Skip the 'Testbench' folder and any non-folder files.
        if vehicle == "Testbench" or not os.path.isdir(vehicle_path):            
            continue
        
        #Construct the path to the sensor configuration file within the vehicle's folder.
        config_file = os.path.join(vehicle_path, 'sensorconfig.yaml')
        #Check if the sensor configuration file exists.
        if os.path.exists(config_file):
            with open(config_file, 'r') as file:
                #Load the YAML data from the file.
                config = yaml.safe_load(file)
                #Iterate through a collection of items labeled as "sensors".
                for sensor in config.get('sensors'):
                    #Check if the current sensor is the back radar.
                    if sensor.get('label') == 'B_LRR_C':
                        #Check if the current back radar's firmware version is older than 1.4.
                        if sensor.get('fw_version') < 1.4:
                            #Add the vehicle to the list.
                            vehicles_with_back_radar.append(vehicle)
        else:
            #Debug: Print a message if the configuration file is missing.
            print(f"No config file found in {vehicle_path}")
    return vehicles_with_back_radar

#The path should be changed to your own.
folder_path = r'C:\Users\varga\Downloads\vehicle_database'
vehicles = find_vehicles_with_back_radar(folder_path)
print("Vehicles equipped with a back radar and their firmware version is older than 1.4:", vehicles)
                        
