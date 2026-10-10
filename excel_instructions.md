# Reproducing the Sales Forecast in Excel

This guide walks you through building the same linear regression forecast in Excel that `forecasting.py` produces in Python.

---

## Step 1 — Import the Data

1. Open Excel and create a new workbook.
2. In **Sheet1**, add these headers in row 1:
   - `A1` → `Month`
   - `B1` → `Sales`
3. Copy the values from `data/sales_data.csv` into columns A and B (rows 2–25).

---

## Step 2 — Calculate the Trend Line (Slope & Intercept)

In a blank area (e.g., `D1:E2`), add the following:

| Cell | Formula | What it does |
|------|---------|--------------|
| D1   | `Slope` | Label |
| E1   | `=SLOPE(B2:B19, A2:A19)` | Calculates the monthly rate of increase |
| D2   | `Intercept` | Label |
| E2   | `=INTERCEPT(B2:B19, A2:A19)` | Calculates the starting value |

> **Note:** Rows 2–19 = months 1–18 (training data only).

---

## Step 3 — Forecast Months 19–24

In column C, create the predicted/forecasted values:

1. `C1` → label: `Predicted`
2. `C2` → `=$E$1*A2+$E$2`  (slope × month + intercept)
3. Drag this formula down from C2 to C25 to cover all 24 months.

**Alternative: use the FORECAST.LINEAR function**

In `C2`:
```
=FORECAST.LINEAR(A2, $B$2:$B$19, $A$2:$A$19)
```
Drag down through C25.

---

## Step 4 — Calculate Accuracy Metrics

In a blank area, add:

| Cell | Formula | What it does |
|------|---------|--------------|
| D4   | `R²`    | Label |
| E4   | `=RSQ(B2:B19, C2:C19)` | R-squared on training data |
| D5   | `MAE`   | Label |
| E5   | `=AVERAGEIF(A2:A19,"<=18",ABS(B2:B19-C2:C19))` | Mean Absolute Error on training |

> For MAE you may need a helper column: in D2 enter `=ABS(B2-C2)` and drag down, then use `=AVERAGE(D2:D19)`.

---

## Step 5 — Create a Chart

1. Select columns A, B, and C (all 24 rows of data).
2. Insert → **Scatter Chart** → Scatter with Straight Lines.
3. Right-click the actual sales series → **Add Trendline** → Linear → check **Display R² on chart**.
4. Format the chart:
   - Title: *Monthly Sales: Actual vs. Forecasted*
   - X-axis label: *Month*
   - Y-axis label: *Sales ($)*
   - Add a vertical line or shading at month 18 to separate training from forecast (use a dummy series or a shape).

---

## Step 6 — Compare Results

Your Excel slope, intercept, and R² should closely match what Python prints:

```
Slope (monthly sales increase): ~$1,680
Intercept:                      ~$26,900
Training R²:                    ~0.957
```

Small differences may appear due to rounding — both tools use ordinary least squares regression, so the math is identical.

---

## Key Takeaway

Excel is fast and visual for small datasets. Python lets you automate, scale, and version-control the same analysis — the underlying math is exactly the same.