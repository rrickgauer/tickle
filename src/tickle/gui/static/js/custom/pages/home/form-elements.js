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

}

HomePageElements.Inputs = {
    TICKER     : '#form-watch-input-ticker',
    PRICE      : '#form-watch-input-price',
    WATCH_TYPE : '[name="form-watch-input-watch-type"]',
    EMAIL      : '#form-watch-input-email',
}


HomePageElements.Buttons = {
    SUBMIT: '#form-watch-button-submit',
}

HomePageElements.spinnerButton = new SpinnerButton(HomePageElements.Buttons.SUBMIT);




