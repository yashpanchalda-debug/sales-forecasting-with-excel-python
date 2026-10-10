# Sales Forecasting with Excel + Python

A simple sales forecasting project that demonstrates how to build a linear regression model first in Excel, then reproduce it in Python — comparing both approaches side by side.

## Skills Demonstrated
- Excel (formulas, charts, trendlines, FORECAST function)
- Python (pandas, scikit-learn, matplotlib)
- Data Visualization
- Linear Regression basics

## Project Structure

```
sales-forecasting/
├── README.md
├── data/
│   └── sales_data.csv        # Monthly sales data (12 months)
├── forecasting.py            # Python model + visualization
└── excel_instructions.md     # Step-by-step guide to reproduce in Excel
```

## Dataset

The dataset (`sales_data.csv`) contains 24 months of fictional monthly sales data with columns:
- `month` — month number (1–24)
- `sales` — sales revenue in dollars

Months 1–18 are used for training; months 19–24 are forecasted.

## How to Run (Python)

### 1. Install dependencies
```bash
pip install pandas scikit-learn matplotlib numpy
```

### 2. Run the forecasting script
```bash
python forecasting.py
```

This will:
- Load the CSV data
- Train a linear regression model on months 1–18
- Forecast sales for months 19–24
- Print model metrics (R², MAE)
- Display a chart comparing actual vs. forecasted values

## How to Reproduce in Excel

See `excel_instructions.md` for a full walkthrough of building the same model in Excel using the FORECAST function and a trendline chart.

## Sample Output

```
=== Sales Forecast Model ===
Training R²:  0.957
MAE (training): $1,842.33

Forecast for months 19–24:
  Month 19: $54,210
  Month 20: $55,890
  ...
```

A chart (`forecast_chart.png`) is saved in the project root.

## Excel vs. Python Comparison

| Feature              | Excel                        | Python                        |
|----------------------|------------------------------|-------------------------------|
| Ease of use          | Very easy, visual            | Requires coding               |
| Reproducibility      | Manual steps                 | Fully scripted                |
| Scalability          | Limited (large data is slow) | Handles large datasets easily |
| Visualization        | Built-in charts              | matplotlib / seaborn          |
| Automation           | Macros / VBA                 | Fully automatable             |

## Author

Built as a portfolio project to demonstrate data analysis and forecasting skills.