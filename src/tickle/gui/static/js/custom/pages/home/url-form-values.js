
import { UrlParser } from "../../classes/url-parser";

export class UrlFormValues
{
    constructor() {
        this.tickerType = null;
        this.ticker     = null;
        this.price      = null;
        this.watchType  = null;

        this._getValuesFromUrl();
    }

    _getValuesFromUrl = () => {
        this.tickerType = UrlParser.getPathValue(UrlFormValues.PathIndex.TICKER_TYPE);
        this.ticker     = UrlParser.getPathValue(UrlFormValues.PathIndex.TICKER);
        this.price      = UrlParser.getPathValue(UrlFormValues.PathIndex.PRICE);
        this.watchType  = UrlParser.getPathValue(UrlFormValues.PathIndex.WATCH_TYPE);
    }


}


UrlFormValues.PathIndex = {
    TICKER_TYPE: 1,
    TICKER: 2,
    PRICE: 3,
    WATCH_TYPE: 4,
}