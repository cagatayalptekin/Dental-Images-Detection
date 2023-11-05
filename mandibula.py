import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

xml_file_path = "2250.xml"

# Load the XML data
with open(xml_file_path, 'r') as file:
    xml_data = file.read()

# Parse the XML
root = ET.fromstring(xml_data)

# Extract the coordinates from the XML
x_coords = []
y_coords = []

polygon = root.find(".//polygon")
for i in range(1, 85):  # Assuming there are 85 pairs of (x, y) coordinates
    x_coords.append(float(polygon.find(f'x{i}').text))
    y_coords.append(float(polygon.find(f'y{i}').text))

# Create a plot to draw the object
plt.figure()
plt.plot(x_coords, y_coords, marker='o', linestyle='-')
plt.title(root.find(".//name").text)  # Set the title as the object name
plt.gca().invert_yaxis()  # Invert the y-axis to match typical image coordinates
plt.show()
