"""Pydantic schemas for the Pyrenex Risk API.

TODO — Align LoanApplication with the feature_columns from your
pyrenex_risk_v2.json metadata (M1-B1 output).
"""
from __future__ import annotations

from pydantic import BaseModel, Field


class LoanApplication(BaseModel):
    """Input schema for /predict.

    TODO — Replace placeholder fields with the actual feature_columns
    from your pyrenex_risk_v2.json. Add Field(..., ge=…, le=…) bounds
    where your EDA showed reasonable ranges.
    """

    loan_amnt: float = Field(..., ge=1_000, le=40_500, description="Loan amount (USD)")
    int_rate: float = Field(..., ge=1, le=40, description="Interest rate (%)")
    installment : float = Field(..., ge=50, le=1_500, description="Monthly installment (USD)")
    annual_inc: float = Field(..., ge=10_000, le=1_000_000, description="Annual income (USD)")
    dti : float = Field(..., ge=0.5, le=60, description="Debt ratio  (%)")
    delinq_2yrs: int = Field(..., ge=0, le=5, description="Number of payment defaults")
    fico_range_low : float = Field(..., ge=10, le=1500, description="Solvency rate (FICO score)")
    revol_util : float = Field(..., ge=0, le=100, description="Revolving line utilization rate (%)")

    term: str = Field(..., description="Loan term, e.g. '36 months' or '60 months'")
    grade: str = Field(..., description="Credit risk rating assigned to the loan (A = low risk, G = high risk")
    home_ownership: str = Field(..., description="Borrower's home ownership status (e.g., RENT, OWN, MORTGAGE)")
    verification_status: str = Field(..., description="Whether the borrower’s income was verified (e.g., Verified, Not Verified)")
    purpose: str = Field(..., description="Loan purpose (e.g., debt consolidation, credit card, home improvement)")
    emp_length: str = Field(..., description="Length of employment (e.g., 1 year, 10+ years)")


class Prediction(BaseModel):
    """Output schema for /predict."""

    prediction: int = Field(..., description="0 = Fully Paid, 1 = Charged Off")
    probability: float = Field(..., ge=0.0, le=1.0)
    model_version: str
    request_id: str


class HealthResponse(BaseModel):
    status: str

class InfoResponse(BaseModel):
    api_version: str
    model_name: str
    model_version: str
    model_created_at: str
    metrics_holdout: dict
