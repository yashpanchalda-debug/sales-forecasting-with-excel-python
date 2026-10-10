import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# ── 1. Load data ──────────────────────────────────────────────────────────────
df = pd.read_csv("data/sales_data.csv")

# Split: months 1–18 = training, months 19–24 = future (we have actuals to compare)
train = df[df["month"] <= 18].copy()
future = df[df["month"] > 18].copy()

X_train = train[["month"]]
y_train = train["sales"]

X_future = future[["month"]]
y_future = future["sales"]

# ── 2. Train linear regression model ─────────────────────────────────────────
model = LinearRegression()
model.fit(X_train, y_train)

# ── 3. Predict ────────────────────────────────────────────────────────────────
y_train_pred = model.predict(X_train)
y_future_pred = model.predict(X_future)

# ── 4. Metrics ────────────────────────────────────────────────────────────────
r2 = r2_score(y_train, y_train_pred)
mae = mean_absolute_error(y_train, y_train_pred)

print("=== Sales Forecast Model (Linear Regression) ===\n")
print(f"  Slope (monthly sales increase): ${model.coef_[0]:,.2f}")
print(f"  Intercept:                      ${model.intercept_:,.2f}")
print(f"  Training R²:                     {r2:.3f}")
print(f"  Training MAE:                   ${mae:,.2f}")
print()

print("  Forecast for months 19–24:")
for month, pred, actual in zip(future["month"], y_future_pred, y_future):
    print(f"    Month {month:>2}: Predicted ${pred:>8,.0f}  |  Actual ${actual:>8,.0f}")

forecast_mae = mean_absolute_error(y_future, y_future_pred)
print(f"\n  Forecast MAE (months 19–24): ${forecast_mae:,.2f}")

# ── 5. Visualisation ─────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 5))

# Actual sales — full dataset
ax.scatter(df["month"], df["sales"], color="steelblue", zorder=5, label="Actual Sales")

# Training fit line
x_line = np.linspace(1, 24, 200).reshape(-1, 1)
y_line = model.predict(x_line)
ax.plot(x_line, y_line, color="darkorange", linewidth=2, linestyle="--", label="Trend Line (Linear Regression)")

# Shade the forecast region
ax.axvspan(18.5, 24.5, alpha=0.08, color="green", label="Forecast Period")

# Forecast points
ax.scatter(future["month"], y_future_pred, color="green", marker="^", s=100, zorder=6, label="Forecasted Values")

# Vertical divider
ax.axvline(x=18.5, color="gray", linestyle=":", linewidth=1.2)
ax.text(18.6, ax.get_ylim()[0] * 1.01, "Forecast →", color="gray", fontsize=9)

ax.set_title("Monthly Sales: Actual vs. Forecasted (Linear Regression)", fontsize=13, fontweight="bold")
ax.set_xlabel("Month")
ax.set_ylabel("Sales ($)")
ax.legend()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x:,.0f}"))
ax.set_xticks(df["month"])
plt.tight_layout()

plt.savefig("forecast_chart.png", dpi=150)
print("\n  Chart saved to forecast_chart.png")
plt.show()