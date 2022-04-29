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

    static async getPrice(tag) {
        const url = Utilities.createUrlWithParms(ApiWrapper.endpoints.PRICES, {tag: tag});
        const response = await fetch(url);
        return response;
    }
}



ApiWrapper.url = '/api';


ApiWrapper.endpoints = {
    SEARCH: `${ApiWrapper.url}/search/tickers`,
    WATCHES: `${ApiWrapper.url}/watches`,
    PRICES:  `${ApiWrapper.url}/prices`,
}


ApiWrapper.methods = {
    POST: 'POST',
    GET: 'GET',
    PUT: 'PUT',
    DELETE: 'DELETE',
    PATCH: 'PATCH',
}
