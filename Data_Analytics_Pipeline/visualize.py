import pandas as pd
import matplotlib.pyplot as plt

def visualize_data(data):
    data.plot(kind='bar')
    plt.show()

if __name__ == "__main__":
    data = pd.read_csv('data/transformed_data.csv')
    visualize_data(data)