
import { BaseView } from "./base";


export class CryptoSearchResponse extends BaseView
{
    constructor(apiResponse) {
        super();

        this.ticker = null;
        this.name = null;
        this.baseCurrency = null;
        this.quoteCurrency = null;

        this._initProperties(apiResponse);
    }
}
