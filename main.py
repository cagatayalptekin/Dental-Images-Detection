import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Load the data without headers
df = pd.read_excel('TotalExcel.xlsx', header=None)

# Count the number of detected (1) and not detected (0) pictures
counts = df[1].value_counts().sort_index()

# Create a bar chart
ax = counts.plot(kind='bar', rot=0)

# Add labels and a title
plt.xlabel('Detection')
plt.ylabel('Count')
plt.title('Detection Status of Pictures')

# Customize x-axis labels
ax.set_xticklabels(['Not Detected', 'Detected'])

# Display the exact counts on top of the bars
for i, v in enumerate(counts):
    ax.text(i, v + 20, str(v), ha='center', va='bottom')

detected_df = df[df[1] == 1]
counts = detected_df[2].value_counts().sort_index()

# Create the second subplot
plt.figure(figsize=(10, 6))

# Create a bar chart
bars = plt.bar(counts.index, counts.values)

# Add labels and a title for the second subplot
plt.xlabel('Error Number')
plt.ylabel('Count of "1"s')
plt.title('Counts of "1"s by Error Number')

error_labels = {
    1: 'BAŞ AŞAĞI',
    2: 'BAŞ YUKARI',
    3: 'ÇENTİĞİN ÖNDEN ISIRILMASI',
    4: 'ÇENTİĞİN ARKADAN ISIRILMASI',
    5: 'HASTA BAŞINI SAĞA SOLA ÇEVİRMİŞ',
    6: 'HASTA BAŞINI SAĞA SOLA YATIRMIŞ'
}

plt.xticks(counts.index, [error_labels.get(x, str(x)) for x in counts.index], rotation=45, ha='right')

# Display the exact counts on top of the bars for the second subplot
for bar in bars:
    height = bar.get_height()
    plt.annotate(f'{int(height)}', xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3), textcoords='offset points', ha='center')

counts = detected_df[3].astype(str).value_counts().sort_index()

# Create the third subplot
plt.figure(figsize=(10, 6))

# Create a bar chart for the third subplot
ax = counts.plot(kind='bar', rot=0)

# Add labels and a title for the third subplot
plt.xlabel('Combination')
plt.ylabel('Count')
plt.title('Combination Errors')


formatted_labels = ['(' + ','.join(digit for digit in combination if digit != '0').rstrip('.').rstrip(',') + ')' for combination in counts.index]
ax.set_xticklabels(formatted_labels)

# Display the exact counts on top of the bars for the third subplot
for i, v in enumerate(counts):
    ax.text(i, v + 20, str(v), ha='center', va='bottom')

# Show all the subplots
plt.show()
