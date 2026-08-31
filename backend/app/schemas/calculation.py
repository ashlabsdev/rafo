from typing import Any

from pydantic import BaseModel


class CalculationRequest(BaseModel):
    operation: str
    values: dict[str, float]


class CalculationResponse(BaseModel):
    formula: str
    result: float
    unit: str
    steps: list[str]