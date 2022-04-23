import { HomePageElements } from "./form-elements";
import { ApiWrapper } from "../../classes/api-wrapper";
import { CryptoSearchResponse } from "../../views/crypto-search-response";



export class TickerSelect
{
    static initCryptoSelect() {
        $(HomePageElements.Inputs.TICKER).select2({
            ajax: {
                url: ApiWrapper.endpoints.SEARCH_CRYPTO,
                data:  function(parms) {
                    return {q: parms.term}
                },
                processResults: TickerSelect.processCryptoSearchApiResponse,
            },
        });
    }


    /**
     * Process the api crypto search response data for select2
     * @param {Array} response - the api response for crypto search
     * @returns the formatted select2 data for crypto symbols
     */
    static processCryptoSearchApiResponse(response) {
        const cryptoTickers = [];

        for (const cryptoSymbol of response.data) {
            const cryptoResponse = new CryptoSearchResponse(cryptoSymbol);

            cryptoTickers.push({
                id: cryptoResponse.ticker,
                text: cryptoResponse.name,
            });
        }

        return {results: cryptoTickers}
    }
}