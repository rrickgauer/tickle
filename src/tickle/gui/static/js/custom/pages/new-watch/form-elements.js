import { SpinnerButton } from "../../classes/spinner-button";

export class HomePageElements 
{
    // get the current value of the ticker text input 
    static getTagValue() {
        return $(HomePageElements.Inputs.TICKER).val();
    }

    static getSelectedSymbolText() {
        const eSelectedOption = $(`${HomePageElements.Inputs.TICKER}`).find(':selected').text();    
        return eSelectedOption;
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

    // enable or disable the submit button
    static toggleSubmitButtonDisabled(setToDisabled) {
        if (setToDisabled) {
            $(HomePageElements.Buttons.SUBMIT).prop('disabled', true);
        } else {
            $(HomePageElements.Buttons.SUBMIT).prop('disabled', false);
        }
    }

    static spinSubmitButton() {
        HomePageElements.spinnerButton.showSpinner();
    }

    static resetSubmitButton() {
        HomePageElements.spinnerButton.reset();
    }

    /** 
     * Validates the form. 
     * Returns true if all inputs have a valid value. 
     */
    static validateForm() {
        return $(HomePageElements.form)[0].reportValidity();
    }

    static resetForm() {
        $(HomePageElements.form)[0].reset();
    }

    static setCurrentTickerPriceValue(price) {
        $(HomePageElements.Elements.CURRENT_TICKER_PRICE_VALUE).text(price);
    }

    static toggleCurrentTickerPriceValue(show) {
        if (show) {
            $(HomePageElements.Elements.CURRENT_TICKER_PRICE_CONTAINER).removeClass('d-none');
        } else {
            $(HomePageElements.Elements.CURRENT_TICKER_PRICE_CONTAINER).addClass('d-none');
        }
    }

}

HomePageElements.Inputs = {
    TICKER     : '#form-watch-input-ticker',
    PRICE      : '#form-watch-input-price',
    WATCH_TYPE : '[name="form-watch-input-watch-type"]',
    EMAIL      : '#form-watch-input-email',
}

HomePageElements.form = '#form-watch-new',


HomePageElements.Buttons = {
    SUBMIT: '#form-watch-button-submit',
}

HomePageElements.spinnerButton = new SpinnerButton(HomePageElements.Buttons.SUBMIT);



HomePageElements.Elements = {
    CURRENT_TICKER_PRICE_CONTAINER: '#form-watch-ticker-price-container',
    CURRENT_TICKER_PRICE_VALUE: '#form-watch-ticker-price-value',
}


