
import { Utilities } from "./utilities";

export class ApiWrapper
{
    static async searchForCrypto(query) {
        const url = Utilities.createUrlWithParms(ApiWrapper.endpoints.SEARCH_CRYPTO, {q: query});
        const response = await fetch(url);
        return response;
    }
}



ApiWrapper.url = '/api';


ApiWrapper.endpoints = {
    SEARCH_CRYPTO: `${ApiWrapper.url}/search/tickers/crypto`,
}


ApiWrapper.methods = {
    POST: 'POST',
    GET: 'GET',
    PUT: 'PUT',
    DELETE: 'DELETE',
    PATCH: 'PATCH',
}
