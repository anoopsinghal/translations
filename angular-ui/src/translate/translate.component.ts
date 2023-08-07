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

  getTranslation(
    fromLang: string,
    fromStr: string,
    toLang: string,
    textControl: FormControl
  ) {
    this.tservice
      .getTranslations(fromLang, fromStr, toLang)
      .subscribe((jsontext) => {
        console.log(jsontext);
        console.log(typeof jsontext);

        var ttext = JSON.parse(JSON.stringify(jsontext)).toStr;

        textControl.setValue(ttext);
      });
  }

  getTranslations() {
    var eValue = this.englishText.value;

    this.getTranslation('en', eValue, 'fr', this.frenchText);
    this.getTranslation('en', eValue, 'de', this.germanText);
    this.getTranslation('en', eValue, 'es', this.spanishText);
  }
}
