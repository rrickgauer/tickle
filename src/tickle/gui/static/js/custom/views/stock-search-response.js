
import { BaseView } from "./base";


export class StockSearchResponse extends BaseView
{
    constructor(apiResponse) {
        super();

        this.assetType = null;
        this.countryCode = null;
        this.isActive = null;
        this.name = null;
        this.openFIGIComposite = null;
        this.permaTicker = null;
        this.ticker = null;

        this._initProperties(apiResponse);
    }
}