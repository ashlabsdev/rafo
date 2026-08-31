export interface CalculationRequest {
  operation: string;
  values: Record<string, number>;
}

export interface CalculationResponse {
  formula: string;
  result: number;
  unit: string;
  steps: string[];
}