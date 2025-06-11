import pandas as pd

df = pd.DataFrame(
    {
        "num_legs": [2, 4, 8, 0],
        "num_wings": [2, 0, 0, 0],
        "num_specimen_seen": [10, 2, 1, 8],
    },
    index=["falcon", "dog", "spider", "fish"],
)
print(df)

import numpy as np

mu, sigma = 500, 100  # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)
print(np.max(s))


pd.factorize(s)


data = pd.Series([0.25, 0.5, 0.75, 1.0])
print(data)
