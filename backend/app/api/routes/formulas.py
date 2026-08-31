from fastapi import APIRouter, HTTPException

from app.services.formula_catalog import FORMULA_CATALOG


router = APIRouter(
    prefix="/api/formulas",
    tags=["Formulas"],
)


@router.get("/")
def get_all_formulas():
    return FORMULA_CATALOG


@router.get("/{formula_id}")
def get_formula(formula_id: str):
    formula = next(
        (
            item
            for item in FORMULA_CATALOG
            if item.id == formula_id
        ),
        None,
    )

    if formula is None:
        raise HTTPException(
            status_code=404,
            detail="Formula not found",
        )

    return formula