import pandas as pd
import os
import shutil

# Load the Excel file
excel_file = 'TotalExcel.xlsx'
df = pd.read_excel(excel_file)

# Define source and destination directories
source_dir = 'FullImages'
destination_dir_detected = 'detected_with_error'
destination_dir_not_detected = 'not_detected'

# Iterate through the DataFrame and move images to appropriate folders
for index, row in df.iterrows():
    image_filename = str(int(row[1]))
    if int(image_filename)==3147 or int(image_filename)==3221:
        image_filename += ".png"
    elif int(image_filename)>3000:
        image_filename += ".bmp"
    else:
        image_filename += ".jpg"
    label = str(int(row[0]))

    if label == '1':
        destination = os.path.join(destination_dir_detected, image_filename)
    else:
        destination = os.path.join(destination_dir_not_detected, image_filename)
##FullImages/2
    source = os.path.join(source_dir, image_filename)


    shutil.copy(source, destination)

print("Images labeled and moved successfully.")
