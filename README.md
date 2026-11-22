# Student Grade Calculator

Small Streamlit app: add subjects, enter grades, see average per subject,
GPA (4.0 scale) and charts (Plotly).

## Setup
```
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run
```
streamlit run app.py
```

## Grade -> GPA points
90+ = 4.0, 80+ = 3.0, 70+ = 2.0, 60+ = 1.0, below 60 = 0.0
