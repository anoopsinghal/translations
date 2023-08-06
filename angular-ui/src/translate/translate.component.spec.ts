import { TestBed } from '@angular/core/testing';
import { TranslateComponent } from './translate.component';

describe('TranslateComponent', () => {
  beforeEach(() =>
    TestBed.configureTestingModule({
      declarations: [TranslateComponent],
    })
  );

  it('should create the translate', () => {
    const fixture = TestBed.createComponent(TranslateComponent);
    const translate = fixture.componentInstance;
    expect(translate).toBeTruthy();
  });

  it(`should have as title 'angular-ui'`, () => {
    const fixture = TestBed.createComponent(TranslateComponent);
    const translate = fixture.componentInstance;
    expect(translate.title).toEqual('angular-ui');
  });

  it('should render title', () => {
    const fixture = TestBed.createComponent(TranslateComponent);
    fixture.detectChanges();
    const compiled = fixture.nativeElement as HTMLElement;
    expect(compiled.querySelector('.content span')?.textContent).toContain(
      'angular-ui translate is running!'
    );
  });
});
