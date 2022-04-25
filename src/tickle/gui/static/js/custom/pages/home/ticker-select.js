import { HomePageElements } from "./form-elements";
import { ApiWrapper } from "../../classes/api-wrapper";
import { CryptoSearchResponse } from "../../views/crypto-search-response";
import { StockSearchResponse } from "../../views/stock-search-response";


export class TickerSelect
{
    /** Initialize the select2 library for crypto searches */
    static initCryptoSelect() {
        $(HomePageElements.Inputs.TICKER).select2({
            theme: 'bootstrap4',
            minimumInputLength: 1,
            ajax: {
                url: ApiWrapper.endpoints.SEARCH_CRYPTO,
                data:  TickerSelect._createDataQuery,
                processResults: TickerSelect._processCryptoSearchApiResponse,
            },
        });
    }


    /**
     * Process the api crypto search response data for select2
     * @param {Array} apiResponse - the api response for crypto search
     * @returns the formatted select2 data for crypto symbols
     */
    static _processCryptoSearchApiResponse(apiResponse) {
        const cryptoTickers = [];

        for (const cryptoSymbol of apiResponse.data) {
            const cryptoResponse = new CryptoSearchResponse(cryptoSymbol);

            cryptoTickers.push({
                id: cryptoResponse.ticker,
                text: cryptoResponse.name,
            });
        }

        return {results: cryptoTickers}
    }

    /** Initialize the select input for stock search */
    static initStocksSelect() {
        $(HomePageElements.Inputs.TICKER).select2({
            theme: 'bootstrap4',
            minimumInputLength: 1,
            ajax: {
                url: ApiWrapper.endpoints.SEARCH_STOCKS,
                data:  TickerSelect._createDataQuery,
                processResults: TickerSelect._processStockSearchApiResponse,
            },
        });
    }
    
    /** Process the stock search results */
    static _processStockSearchApiResponse(apiResponse) {
        const stockTickers = [];

        for (const stockSymbolObject of apiResponse.data) {
            const stockView = new StockSearchResponse(stockSymbolObject);

            stockTickers.push({
                id: stockView.ticker,
                text: stockView.name,
            });
        }

        return {results: stockTickers}
    }


    /** Create the api 'q' query for the api request */
    static _createDataQuery(parms) {
        return {q: parms.term};
    }
}