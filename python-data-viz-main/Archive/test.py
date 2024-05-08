#pip install matplotlib seaborn pandas

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def load_csv(filename):
    return pd.read_csv(filename)

def load_excel(filename):
    return pd.read_excel(filename)


def scatter_plot(data, x, y):
    plt.scatter(data[x], data[y])
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title('Scatter Plot')
    plt.show()

def bar_plot(data, x, y):
    sns.barplot(x=x, y=y, data=data)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title('Bar Plot')
    plt.show()


def main():
    # Load data
    filename = input("Enter the File name:")
    file_extension = filename.split('.')[-1]
    
    if file_extension == 'csv':
        data = load_csv(filename)
    elif file_extension == 'xlsx':
        data = load_excel(filename)
    else:
        print("Unsupported file format.")
        return

    # Visualize data
    print("Choose visualization type:")
    print("1. Scatter Plot")
    print("2. Bar Plot")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        x = input("Enter x-axis column name: ")
        y = input("Enter y-axis column name: ")
        scatter_plot(data, x, y)
    elif choice == 2:
        x = input("Enter x-axis column name: ")
        y = input("Enter y-axis column name: ")
        bar_plot(data, x, y)
    else:
        print("Invalid choice.")
        return

if __name__ == "__main__":
    main()
