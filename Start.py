print("Lets see how this goes")


import pandas as pd

data = {
    "Study": ["Study 1", "Study 2", "Study 3"],
    "Focus": ["Focus 1", "Focus 2", "Focus 3"],
    "Research Question": ["Question 1", "Question 2", "Question 3"]
}

df = pd.DataFrame(data)

print(df)