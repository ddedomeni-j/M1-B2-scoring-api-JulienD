"""Shared fixtures for M1-B2 tests."""
from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture(scope="module")
def client() -> TestClient:
    """TestClient with lifespan triggered (model loaded)."""
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def valid_payload() -> dict:
    """Valid loan application payload.

    TODO — Align with the actual LoanApplication schema and feature_columns
    of pyrenex_risk_v2.json. The example below is a placeholder.
    """
    return {
        "loan_amnt": 7600,
        "term": "36 months",
        "int_rate": 11.39,
        "installment": 250.22,
        "grade": "B",
        "emp_length": "3 years",
         "home_ownership": "MORTGAGE",
        "annual_inc": 72500,
        "verification_status": "Verified",
        "purpose": "debt_consolidation",
        "dti": 13.12, "delinq_2yrs": 1, 
        "fico_range_low": 725, 
        "revol_util": 48.0
    }

