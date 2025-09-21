

import pandas as pd
from lifelines import KaplanMeierFitter
import matplotlib.pyplot as plt

# Fake oncology trial data (10 patients)
data = pd.DataFrame({
    "time": [5, 6, 6, 2, 4, 3, 8, 10, 7, 9],
    "status": [1, 0, 1, 1, 0, 1, 0, 1, 1, 0]
})

# Fit Kaplan-Meier
kmf = KaplanMeierFitter()
kmf.fit(durations=data["time"], event_observed=data["status"])

# Plot
kmf.plot_survival_function()
plt.title("Kaplan-Meier Curve (Synthetic Data)")
plt.xlabel("Time (months)")
plt.ylabel("Survival Probability")
plt.savefig("km_curve.png")
