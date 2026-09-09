import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

import {
  CalculationRequest,
  CalculationResponse,
} from '../core/models/calculation.model';


@Injectable({
  providedIn: 'root',
})
export class CalculationService {

  private readonly apiUrl =
  `${environment.apiUrl}/api/calculate`;

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