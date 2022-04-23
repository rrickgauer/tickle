


export class ApiWrapper
{

}



ApiWrapper.url = '/api';


ApiWrapper.endpoints = {
    SEARCH_CRYPTO: `${ApiWrapper.url}/search/tickers/crypto`,
    SEARCH_STOCKS: `${ApiWrapper.url}/search/tickers/stocks`,
}


ApiWrapper.methods = {
    POST: 'POST',
    GET: 'GET',
    PUT: 'PUT',
    DELETE: 'DELETE',
    PATCH: 'PATCH',
}
