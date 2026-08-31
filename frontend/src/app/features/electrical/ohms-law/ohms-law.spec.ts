import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OhmsLaw } from './ohms-law';

describe('OhmsLaw', () => {
  let component: OhmsLaw;
  let fixture: ComponentFixture<OhmsLaw>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [OhmsLaw],
    }).compileComponents();

    fixture = TestBed.createComponent(OhmsLaw);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
