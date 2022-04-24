
/*


Need to retrieve all the values and create a new Watch object.
Send it to the api


*/


import { UrlFormValues } from "./url-form-values";
import { HomePageElements } from "./form-elements";
import { Watch } from "../../domain/models/watch";

export class WatchCreationInterface
{
    constructor() {
        this.tickerType = null;
        this.ticker     = null;
        this.price      = null;
        this.watchType  = null;
        this.email      = null;

        this._initPropertyValues();
    }

    /** Set the object's property values */
    _initPropertyValues = () => {
        const urlValues = new UrlFormValues();
        this.tickerType = urlValues.tickerType;
        this.ticker     = urlValues.ticker;
        this.price      = urlValues.price;
        this.watchType  = urlValues.watchType;

        this.email = HomePageElements.getEmailValue();
    }

    /** Transform the object's properties into a Watch domain model */
    getWatchModel = () => {
        const watch = new Watch();

        watch.ticker_type = this.tickerType;
        watch.ticker      = this.ticker;
        watch.price       = this.price;
        watch.watch_type  = this.watchType;
        watch.email       = this.email;

        return watch;
    }
}

