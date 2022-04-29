
import { BaseView } from "./base";


export class PriceResponse extends BaseView
{
    constructor(apiResponse) {
        super();

        this.avgVolume         = null;
        this.beta              = null;
        this.dailyRange        = null;
        this.dividend          = null;
        this.eps               = null;
        this.last              = null;
        this.marketCap         = null;
        this.nextEarningDate   = null;
        this.oneYearReturn     = null;
        this.open              = null;
        this.prevClose         = null;
        this.ratio             = null;
        this.revenue           = null;
        this.sharesOutstanding = null;
        this.volume            = null;
        this.weekRange         = null;

        this._initProperties(apiResponse);
    }
}