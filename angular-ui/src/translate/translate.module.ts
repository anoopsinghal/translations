import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule } from '@angular/forms';

import { TranslateComponent } from './translate.component';

@NgModule({
  declarations: [TranslateComponent],
  imports: [BrowserModule, ReactiveFormsModule],
  providers: [],
  bootstrap: [TranslateComponent],
})
export class TranslateModule {}
