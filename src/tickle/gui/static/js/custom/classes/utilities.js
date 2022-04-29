

export class Utilities
{
    /**************************************************
     * Create a URL with search params appended to
     * 
     * example.com?name=Ryan&age=26
     * 
     * @param {string} endpoint - the base url to use
     * @param {Object} nativeObject - the JS object to turn into a URLSearchParams object
     * 
     * @returns string
     *************************************************/
    static createUrlWithParms(endpoint, nativeObject) {
        const data = Utilities.toUrlSearchParms(nativeObject);
        const url = `${endpoint}?${data.toString()}`;
        return url;
    }


    /**
     * Transform a native JavaScript object into a URLSearchParams object
     * @param {object} nativeObject - the native object
     * @returns {URLSearchParams} the url parms object
     */
    static toUrlSearchParms(nativeObject) {
        const urlSearchParms = new URLSearchParams();

        for (const key in nativeObject) {
            urlSearchParms.append(key, nativeObject[key]);
        }

        return urlSearchParms
    }

    /**
     * Jump to the top of the page
     */
    static jumpToPageTop() {
        $('html,body').scrollTop(0);
    }
}