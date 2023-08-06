import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';

import { TranslateModule } from './translate/translate.module';


platformBrowserDynamic().bootstrapModule(TranslateModule)
  .catch(err => console.error(err));
