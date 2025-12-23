# Decision-Focused Forecasting
From Prediction to Action

This project demonstrates how forecasts create value only when they change decisions.

Rather than optimising purely for predictive accuracy, the focus is on:
- defining an operational decision
- creating an auditable decision rule
- measuring impact with a before vs after simulation

Core question:
What decision would someone make differently if they trusted this forecast?

---

## Decision Framing

Decision: daily ordering quantity for a perishable or fast-moving product.

Baseline policy:
Order yesterday’s demand plus a fixed safety buffer.

Forecast-informed policy:
Order forecast demand plus a dynamic buffer.

Evaluation focuses on outcomes:
- stockout rate
- average buffer
- simple cost trade-off (holding vs stockout penalty)

---

## Repository Structure
```text
decision-focused-forecasting/
├── notebooks/   # narrative and analysis
├── src/         # reusable logic
├── data/        # generated datasets (gitignored)
└── outputs/     # figures and summary tables



## How to Read

1. `00_project_brief.ipynb` – decision framing  
2. `01_data_build.ipynb` – clean demand data  
3. `02_model.ipynb` – forecasting model  
4. `03_decision_simulation.ipynb` – decision rule + impact  

---

## Author

Yeji Choe  
Data Scientist – Forecasting & Decision Systems  
Auckland, New Zealand
