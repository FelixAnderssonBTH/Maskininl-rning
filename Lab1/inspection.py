'''

Bara lite lek kod för att kunna analyzera datan så vi vet lite vad vi ska kolla efter


'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Load the CSV file into a DataFrame
file_path = 'Lab1/red.csv'  # Replace with your file path
df = pd.read_csv(file_path, delimiter=';')

# Extract each column as a separate array
fixed_acidity = df["fixed acidity"].values
volatile_acidity = df["volatile acidity"].values
citric_acid = df["citric acid"].values
residual_sugar = df["residual sugar"].values
chlorides = df["chlorides"].values
free_sulfur_dioxide = df["free sulfur dioxide"].values
total_sulfur_dioxide = df["total sulfur dioxide"].values
density = df["density"].values
pH = df["pH"].values
sulphates = df["sulphates"].values
alcohol = df["alcohol"].values
quality = df["quality"].values

all_arrays = [fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol, quality]
array_names = ["fixed_acidity", "volatile_acidity", "citric_acid", "residual_sugar", "chlorides", "free_sulfur_dioxide", "total_sulfur_dioxide", "density", "pH", "sulphates", "alcohol", "quality"]

for i in range(len(all_arrays)):
    array = all_arrays[i]

    unique_values, counts = np.unique(array, return_counts=True)

    norm = plt.Normalize(min(counts), max(counts))  
    colors = cm.viridis(norm(counts)) 
    plt.figure(figsize=(14, 10))
    plt.bar(unique_values, counts, color=colors)
    plt.xticks(unique_values)
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.title(array_names[i])

    for j, count in enumerate(counts):
        plt.text(unique_values[j], count + 0.1, str(count), ha='center', va='bottom')

    plt.show()
