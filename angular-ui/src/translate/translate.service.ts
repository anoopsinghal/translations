import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, tap } from 'rxjs/operators';
import { Observable, of } from 'rxjs';
import { environment } from 'src/environment/environment';

@Injectable()
export class TranslateService {
  translateUrl!: string;

  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
    }),
  };

  constructor(private http: HttpClient) {
    this.translateUrl = environment.translationServerAPIURL;
  }

  getTranslations(
    fromLang: string,
    fromStr: string,
    toLang: string
  ): Observable<any> {
    var json = { fromLang: fromLang, fromStr: fromStr, toLang: toLang };

    return this.http.post<JSON>(this.translateUrl, json, this.httpOptions).pipe(
      tap((_) => this.log('returned from server')),
      catchError(this.handleError<JSON>('translate'))
    );
  }

  /**
   * Handle Http operation that failed.
   * Let the app continue.
   *
   * @param operation - name of the operation that failed
   * @param result - optional value to return as the observable result
   */
  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead

      // TODO: better job of transforming error for user consumption
      this.log(`${operation} failed: ${error.message}`);

      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }

  /** Log a HeroService message with the MessageService */
  private log(message: string) {
    console.log(message);
  }
}
