import { Component } from '@angular/core';
import {
  FormBuilder,
  ReactiveFormsModule,
} from '@angular/forms';

import { CalculationService } from '../../../services/calculation.service';
import {
  CalculationRequest,
  CalculationResponse,
} from '../../../core/models/calculation.model';


@Component({
  selector: 'app-ohms-law',
  imports: [ReactiveFormsModule],
  templateUrl: './ohms-law.html',
  styleUrl: './ohms-law.css',
})
export class OhmsLaw {

  calculationResult: CalculationResponse | null = null;

  calculationError: string | null = null;

  isCalculating = false;


  readonly calculatorForm;


  constructor(
    private readonly formBuilder: FormBuilder,
    private readonly calculationService: CalculationService,
  ) {

    this.calculatorForm = this.formBuilder.group({
      operation: ['calculate-current'],

      voltage: [null],
      current: [null],
      resistance: [null],
    });
  }


  get selectedOperation(): string {
    return this.calculatorForm.value.operation ?? '';
  }


  calculate(): void {

    this.calculationResult = null;
    this.calculationError = null;

    const formValue = this.calculatorForm.value;

    const values: Record<string, number> = {};

    if (this.selectedOperation === 'calculate-voltage') {
      values['current'] = Number(formValue.current);
      values['resistance'] = Number(formValue.resistance);
    }

    if (this.selectedOperation === 'calculate-current') {
      values['voltage'] = Number(formValue.voltage);
      values['resistance'] = Number(formValue.resistance);
    }

    if (this.selectedOperation === 'calculate-resistance') {
      values['voltage'] = Number(formValue.voltage);
      values['current'] = Number(formValue.current);
    }


    const request: CalculationRequest = {
      operation: this.selectedOperation,
      values,
    };


    this.isCalculating = true;


    this.calculationService
      .calculateOhmsLaw(request)
      .subscribe({

        next: (response) => {
          this.calculationResult = response;
          this.isCalculating = false;
        },

        error: (error) => {
          this.calculationError =
            error?.error?.detail ??
            'Unable to calculate the result.';

          this.isCalculating = false;
        },

      });
  }
}