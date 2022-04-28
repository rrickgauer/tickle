
import { BaseView } from "./base";


export class TickerSearchResponse extends BaseView
{
    constructor(apiResponse) {
        super();

        this.country = null;
        this.exchange = null;
        this.id_ = null;
        this.name = null;
        this.pair_type = null;
        this.symbol = null;
        this.tag = null;

        this._initProperties(apiResponse);
    }
}