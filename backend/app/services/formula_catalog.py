from app.schemas.formula import (
    Formula,
    FormulaOperation,
    FormulaVariable,
)


FORMULA_CATALOG = [
    Formula(
        id="electrical-ohms-law",
        name="Ohm's Law",
        category="Electrical Fundamentals",
        description=(
            "Calculate voltage, current, or resistance "
            "using Ohm's Law."
        ),
        variables=[
            FormulaVariable(
                symbol="V",
                name="Voltage",
                unit="V",
            ),
            FormulaVariable(
                symbol="I",
                name="Current",
                unit="A",
            ),
            FormulaVariable(
                symbol="R",
                name="Resistance",
                unit="Ω",
            ),
        ],
        operations=[
            FormulaOperation(
                id="calculate-voltage",
                name="Calculate Voltage",
                formula="V = I × R",
            ),
            FormulaOperation(
                id="calculate-current",
                name="Calculate Current",
                formula="I = V / R",
            ),
            FormulaOperation(
                id="calculate-resistance",
                name="Calculate Resistance",
                formula="R = V / I",
            ),
        ],
    )
]