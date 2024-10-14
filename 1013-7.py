import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
rows_with_sum_gt_100 = df[df.sum(axis=1) > 100]
print(rows_with_sum_gt_100)
