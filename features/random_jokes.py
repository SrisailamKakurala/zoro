import pandas as pd
df = pd.read_csv('shortjokes.csv')

def joke():
    random_joke = df['Joke'].sample(n=1).iloc[0]
    print(random_joke)
    return (random_joke)
