
import { HomePageElements } from "./form-elements";
import { ApiWrapper } from "../../classes/api-wrapper";
import { TickerSearchResponse } from "../../views/ticker-search-response";

export class TickerSearchInput
{
    /** Initialize the select2 library for crypto searches */
    static initSearchInput() {
        $(HomePageElements.Inputs.TICKER).select2({
            theme: 'bootstrap4',
            minimumInputLength: 1,
            ajax: {
                url: ApiWrapper.endpoints.SEARCH,
                data:  TickerSearchInput._createDataQuery,
                processResults: TickerSearchInput._processApiSearchResults,
            },
        });
    }

    /** Create the api 'q' query for the api request */
    static _createDataQuery(parms) {
        return {q: parms.term};
    }

    static _processApiSearchResults(apiResponse) {
        const stockTickers = [];

        console.log(apiResponse);

        for (const stockSymbolObject of apiResponse.data) {
            const stockView = new TickerSearchResponse(stockSymbolObject);

            stockTickers.push({
                id: stockView.tag,
                text: stockView.name,
            });
        }

        return {results: stockTickers}
    }
}