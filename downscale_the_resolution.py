from ruamel.yaml import YAML
import os
import shutil

def find_vehicles_with_midrange_camera_and_backup(folder):
    print(f"Looking in folder: {folder}")
    yaml = YAML()
    #This setup preserves formatting and comments
    yaml.preserve_quotes = True
    
    for vehicle in os.listdir(folder):
        #Construct the full path to each item
        vehicle_path = os.path.join(folder, vehicle)
        #Debug: Which vehicle folder is being checked
        print(f"Checking folder: {vehicle}")
        #Skip the 'Testbench' folder and any non-folder files.
        if vehicle == "Testbench" or not os.path.isdir(vehicle_path):
            print(f"Skipping: {vehicle}")
            continue

        #Construct the path to the sensor configuration file within the vehicle's folder.
        config_file = os.path.join(vehicle_path, 'sensorconfig.yaml')
        #Check if the sensor configuration file exists.
        if os.path.exists(config_file):
            #Create a backup folder of the current cars config
            backup_folder = os.path.join(folder, "backup", vehicle)
            #If there is no backup folder, create one
            if not os.path.exists(backup_folder):
                os.makedirs(backup_folder)
            #Copy the original sensorconfig.yaml to the backup folder
            shutil.copy(config_file, backup_folder)
            print(f"Backup created for {vehicle} in {backup_folder}")

            #Load the YAML data from the file
            with open(config_file, 'r') as file:
                config = yaml.load(file)

            updated = False
            for sensor in config.get('sensors'):
                #Check if the current sensor is a backwards camera
                if sensor.get('label') == 'B_MIDRANGECAM_C':
                    #Check if the resolution is 2896x1876, replace with 1920x1080
                    if sensor.get('image_resolution_px') == [2896, 1876]:
                        sensor['image_resolution_px'] = [1920, 1080]
                        updated = True
                        #Debug: Which vehicle's camera has been modified
                        print(f"Updated resolution for {vehicle}")

            if updated:
                #Save the updated YAML data back to the original file.
                with open(config_file, 'w') as file:
                    yaml.dump(config, file)
        else:
            print(f"No config file found in {vehicle_path}")

#The path should be changed to your own.
folder_path = r'C:\Users\varga\Downloads\vehicle_database'
find_vehicles_with_midrange_camera_and_backup(folder_path)
