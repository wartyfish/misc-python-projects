import pandas as pd
import re

def fruits():                   # DataFrame creation
    fruits = pd.DataFrame(
        {
            "Price": [1.20, 0.80, 1.00, 1.50],
            "Quantity": [50, 75, 40, 20]            
        },
        index=["Apple", "Bananana", "Orange", "Pear"]
    )
    return fruits

def column_operators(df):       # Multiply column values and add to new column
    result = df.copy()
    result["Total Value"] = result["Price"] * result["Quantity"]
    return result

def filter_expense(df):         # Filter by column value
    df = df[df["Price"] >= 1.2]
    return df

def series_stats(s):            # Return series stats
    df = pd.DataFrame([{
        "Mean":     s.mean(),
        "Median":   s.median(),
        "Min":      s.min(),
        "Max":      s.max(),
        "Std":      s.std()
    }])

    return df

def convert_temps(temps):       # Degrees C -> F
    df = pd.DataFrame({
        "Celcius":      temps,
        "Fahrenheit":   temps * 9 / 5 + 32
    })

    return df

def normalise_series(s):        # Normalises series
    df = pd.DataFrame({
        "Values": s,
        "Normalised": ((s - s.min()) / (s.max() - s.min()))
        })

    return df

def select_starting_with(df, letter):   # Return all rows where the name begins with a specifed letter
    letter = letter.lower()
    filtered = df[df["Name"].str[0].str.lower() == letter]
    return filtered

def add_density(df):            # Add column to dataframe
    copy = df.copy()
    copy["Population density"] = df["Population"] / df["Area"]
    return copy

def merge_people_scores(names, scores):  # Merge two dataframes 
    merged = pd.merge(names, scores, on="ID")
    return merged

def sort_by_columns(cities):    # Sort by column values
    sorted = cities.sort_values(by=["Name", "Population"])
    return sorted

def main():
    fruit = fruits()
    # print(fruit)

    fruit_values = column_operators(fruit)
    # print(fruit_values)

    filtered_fruit = filter_expense(fruit)
    # print(filtered_fruit)

    s = pd.Series([321, 9203, 3377, 100])
    # print(series_stats(s))

    t = pd.Series(range(-100, 105, 10))
    # print(convert_temps(t))

    # print(normalise_series(s))

    people = pd.DataFrame({
        "Name": ["Alice", "Bob", "Andy", "Charlie", "David", "Amy"],
        "Age": [20, 2, 12, 70, 100, 34],
        "Height": [190, 190, 43, 165, 12, 100]
    })

    letter = "A"
    # print(select_starting_with(people, letter))

    cities = pd.DataFrame({
        "Name":         ["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu"],
        "Population":   [643272, 279044, 231853, 223027, 201810],
        "Area":         [715.48, 528.03, 689.59, 240.35, 3817.52]
    })

    # print(add_density(cities))

    names = pd.DataFrame({
        "ID":       [1, 2, 3],
        "Name":     ["Alice", "Bob", "Charlie"]
    })

    scores = pd.DataFrame({
        "ID":       [1, 1, 2],
        "Score":    [80, 90, 70]
    })
    
    # print(merge_people_scores(names, scores))

    print(sort_by_columns(cities))
    


if __name__ == "__main__":
    main()