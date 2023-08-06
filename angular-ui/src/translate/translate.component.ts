import { Component } from '@angular/core';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'translate-root',
  templateUrl: './translate.component.html',
  styleUrls: ['./translate.component.css'],
})
export class TranslateComponent {
  title = 'angular-ui';

  englishText = new FormControl();
  frenchText = new FormControl({ value: '', disabled: true });
  germanText = new FormControl({ value: '', disabled: true });
  spanishText = new FormControl({ value: '', disabled: true });

  getTranslations() {
    this.frenchText.setValue(this.englishText.value);
    this.germanText.setValue(this.englishText.value);
    this.spanishText.setValue(this.englishText.value);
  }
}
