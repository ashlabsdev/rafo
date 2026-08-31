import { Routes } from '@angular/router';

import { OhmsLaw } from './features/electrical/ohms-law/ohms-law';

export const routes: Routes = [
  {
    path: 'electrical/ohms-law',
    component: OhmsLaw,
  },
  {
    path: '',
    redirectTo: 'electrical/ohms-law',
    pathMatch: 'full',
  },
];