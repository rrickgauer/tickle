

export class HomePageElements 
{
    // get the value of the currently selected watch type radio input
    static getTickerTypeValue() {
        return $(`${HomePageElements.Inputs.TICKER_TYPE}:checked`).val();
    }

    // get the current value of the ticker text input 
    static getTickerValue() {
        return $(HomePageElements.Inputs.TICKER).val();
    }

    static getPriceValue() {
        return $(HomePageElements.Inputs.PRICE).val();
    }

    static getWatchTypeValue() {
        return $(`${HomePageElements.Inputs.WATCH_TYPE}:checked`).val();
    }

    static getEmailValue() {
        return $(HomePageElements.Inputs.EMAIL).val();
    }

    // enable or disable the next page button
    static toggleNextPageButtonDisabled(setToDisabled) {
        if (setToDisabled) {
            $(`.${HomePageElements.Buttons.NEXT_PAGE}`).addClass('disabled');
        } else {
            $(`.${HomePageElements.Buttons.NEXT_PAGE}`).removeClass('disabled');
        }
    }

    // enable or disable the submit button
    static toggleSubmitButtonDisabled(setToDisabled) {
        if (setToDisabled) {
            $(HomePageElements.Buttons.SUBMIT).addClass('disabled');
        } else {
            $(HomePageElements.Buttons.SUBMIT).removeClass('disabled');
        }
    }
    
    // set the destination url value of the next page link button
    static setNextPageUrlValue(url) {
        $(`.${HomePageElements.Buttons.NEXT_PAGE}`).attr('href', url);
    }
    

}


HomePageElements.Inputs = {
    TICKER_TYPE: '[name="form-watch-input-ticker-type"]',
    TICKER     : '#form-watch-input-ticker',
    PRICE      : '#form-watch-input-price',
    WATCH_TYPE : '[name="form-watch-input-watch-type"]',
    EMAIL      : '#form-watch-input-email',
}


HomePageElements.Buttons = {
    NEXT_PAGE: 'btn-next-page',
    SUBMIT: '#form-watch-button-submit',
}




