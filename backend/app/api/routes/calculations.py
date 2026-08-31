from fastapi import APIRouter, HTTPException

from app.calculators.electrical.ohms_law import calculate_ohms_law
from app.schemas.calculation import (
    CalculationRequest,
    CalculationResponse,
)

router = APIRouter(
    prefix="/api/calculate",
    tags=["Calculations"],
)

@router.post(
    "/electrical-ohms-law",
    response_model=CalculationResponse,
)

def calculate_electrical_ohms_law(
    request: CalculationRequest,
):
    try:
        result = calculate_ohms_law(
            operation=request.operation,
            values=request.values,
        )
        return result

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        )