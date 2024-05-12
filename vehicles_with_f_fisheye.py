import os
import yaml

def find_vehicles_with_fisheye_camera(folder):
    #This list will stands for to store the vehicles that equipped with a front fisdheye camera.
    vehicles_with_fisheye = []

    print(f"Looking in: {folder}")  
    #Iterate in the folder
    for vehicle in os.listdir(folder):
        #Construct the full path to each item
        vehicle_path = os.path.join(folder, vehicle)
        # Debug: which vehicle folder is being checked
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
                    for sensor in config.get('sensors'):
                        #Check if the current sensor is the front fisheye camera.
                        if sensor.get('label') == 'F_FISHEYE_C':                           
                            #Add the vehicle to the list.
                            vehicles_with_fisheye.append(vehicle)               
        else:
            #Debug: Print a message if the configuration file is missing.
            print(f"No config file found in {vehicle_path}")  

    return vehicles_with_fisheye
    
#The path should be changed to your own.
folder_path = r'C:\Users\varga\Downloads\vehicle_database'
vehicles = find_vehicles_with_fisheye_camera(folder_path)
print("Vehicles equipped with a front fisheye camera:", vehicles)
