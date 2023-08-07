import { Component } from '@angular/core';
import { FormControl } from '@angular/forms';
import { TranslateService } from './translate.service';

@Component({
  selector: 'translate-root',
  templateUrl: './translate.component.html',
  styleUrls: ['./translate.component.css'],
  providers: [TranslateService],
})
export class TranslateComponent {
  title = 'angular-ui';

  englishText = new FormControl();
  frenchText = new FormControl({ value: '', disabled: true });
  germanText = new FormControl({ value: '', disabled: true });
  spanishText = new FormControl({ value: '', disabled: true });

  constructor(private tservice: TranslateService) {}

  getTranslations() {
    var eValue = this.englishText.value;

    var fValue = this.tservice.getTranslations('en', eValue, 'fr');
    this.frenchText.setValue(fValue);

    var gValue = this.tservice.getTranslations('en', eValue, 'de');
    this.germanText.setValue(gValue);

    var sValue = this.tservice.getTranslations('en', eValue, 'es');
    this.spanishText.setValue(sValue);
  }
}
