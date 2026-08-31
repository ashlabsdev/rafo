from pydantic import BaseModel


class FormulaVariable(BaseModel):
    symbol: str
    name: str
    unit: str


class FormulaOperation(BaseModel):
    id: str
    name: str
    formula: str


class Formula(BaseModel):
    id: str
    name: str
    category: str
    description: str
    variables: list[FormulaVariable]
    operations: list[FormulaOperation]