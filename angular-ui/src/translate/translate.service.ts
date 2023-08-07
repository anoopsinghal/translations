import { Injectable } from '@angular/core';

@Injectable()
export class TranslateService {
  getTranslations(fromLang: string, fromStr: string, toLang: string): string {
    var json = { fromLang: fromLang, fromStr: fromStr, toLang: toLang };
    return fromStr;
  } // stub
}
