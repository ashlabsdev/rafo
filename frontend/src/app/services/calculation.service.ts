import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

import {
  CalculationRequest,
  CalculationResponse,
} from '../core/models/calculation.model';


@Injectable({
  providedIn: 'root',
})
export class CalculationService {

  private readonly apiUrl = 'http://127.0.0.1:8000/api/calculate';

  constructor(
    private readonly http: HttpClient,
  ) {}

  calculateOhmsLaw(
    request: CalculationRequest,
  ): Observable<CalculationResponse> {

    return this.http.post<CalculationResponse>(
      `${this.apiUrl}/electrical-ohms-law`,
      request,
    );
  }
}