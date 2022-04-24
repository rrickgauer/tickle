import { Utilities } from "./utilities";



export class ApiWrapper
{
    static async postWatch(watch) {
        const data = Utilities.toUrlSearchParms(watch);
        
        const response = await fetch(ApiWrapper.endpoints.WATCHES, {
            method: ApiWrapper.methods.POST,
            body: data,
        });

        return response;
    }
}



ApiWrapper.url = '/api';


ApiWrapper.endpoints = {
    SEARCH_CRYPTO: `${ApiWrapper.url}/search/tickers/crypto`,
    SEARCH_STOCKS: `${ApiWrapper.url}/search/tickers/stocks`,
    WATCHES: `${ApiWrapper.url}/watches`,
}


ApiWrapper.methods = {
    POST: 'POST',
    GET: 'GET',
    PUT: 'PUT',
    DELETE: 'DELETE',
    PATCH: 'PATCH',
}
