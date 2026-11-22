# AGENTS.md

Instructions for AI coding agents working in this repository.
Status: describes the repository at the time of writing; update it when the structure changes.

## Purpose
Student Grade Calculator: a small Streamlit app to add subjects, enter grades,
see per-subject averages, a credit-weighted GPA (4.0 scale) and Plotly charts.
It is a coursework project (Software Engineering, Assignment #05). It has no users, no real data and no deployment.

## Architecture
- `app.py` is the whole application (Streamlit script). Data lives only in `st.session_state.subjects`,
  a dict `{subject_name: {"credits": number, "grades": [numbers]}}`. Nothing is persisted.
- GPA conversion (average -> points) and the weighted GPA are computed inline in `app.py`.
- `requirements.txt` lists dependencies (currently unpinned). No database, no network calls, no secrets.

## Setup
Windows (PowerShell):
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    pip install -r requirements.txt
macOS/Linux:
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

## Safe commands (allowed without asking)
- `streamlit run app.py`
- `python -m pytest` (once tests exist), `python -m ruff check .` (once configured)
- `python -m py_compile app.py`
- `pip freeze`, `pip list`
- `git status`, `git diff`, `git log`, `git checkout -b <branch>`, `git add`, `git commit` on a feature branch

## Ask first (needs explicit human approval)
- Adding, removing or upgrading any dependency, or editing `requirements.txt`
- Creating, renaming or deleting files outside the task scope
- Changing the GPA scale or any rule listed in ACCEPTANCE_CRITERIA.md

## Forbidden
- Never read, create or commit secrets (`.env`, API keys, tokens, `.streamlit/secrets.toml`) or real personal data
- No production deployment, no publishing, no pushing to `main`, no force-push, no history rewriting
- No destructive commands (`rm -rf`, `git reset --hard`, `git clean -fd`, dropping files not created by the task)
- No unreviewed dependency changes
- Do not edit or delete the `baseline` git tag
- Do not claim tests or builds passed unless you actually ran them; report real output only

## Coding conventions
- Python 3.10+, PEP 8, type hints on new functions, short docstrings
- Keep calculation logic free of Streamlit calls so it can be unit-tested
- Small diffs: one concern per change, no drive-by refactors

## Test expectations
- Every bug fix comes with a test that fails before the fix and passes after
- Behavior in ACCEPTANCE_CRITERIA.md must keep passing
- Before finishing, run the checks above and include the exact commands and results in your summary

## Review gates
- A human reviews every diff before it is committed or merged
- Work happens on a feature branch, never directly on `main`
- Risky or ambiguous changes: stop and ask instead of guessing