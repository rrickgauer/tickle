
/*
Need to retrieve all the values and create a new Watch object.
Send it to the api
*/

import { HomePageElements } from "./form-elements";
import { Watch } from "../../domain/models/watch";

export class WatchCreationInterface
{
    constructor() {
        this.symbol    = null;
        this.tag       = null;
        this.price     = null;
        this.watchType = null;
        this.email     = null;

        this._initPropertyValues();
    }

    /** Set the object's property values */
    _initPropertyValues = () => {
        this.symbol    = HomePageElements.getSelectedSymbolText();
        this.tag       = HomePageElements.getTagValue();
        this.price     = HomePageElements.getPriceValue();
        this.watchType = HomePageElements.getWatchTypeValue();
        this.email     = HomePageElements.getEmailValue();
    }

    /** Transform the object's properties into a Watch domain model */
    getWatchModel = () => {
        const watch = new Watch();

        watch.tag        = this.tag;
        watch.symbol     = this.symbol;
        watch.price      = this.price;
        watch.watch_type = this.watchType;
        watch.email      = this.email;

        return watch;
    }
}

