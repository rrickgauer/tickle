
import { HomePageElements } from "./form-elements";
import { UrlFormValues } from "./url-form-values";


const m_urlFormValues = new UrlFormValues();


/**********************************************************
Main logic
**********************************************************/
$(document).ready(function() {
    addEventListners();
    // console.log(m_urlFormValues);
});

// add the page event handlers
function addEventListners() {
    $(HomePageElements.Inputs.TICKER_TYPE).on('change', updateTickerTypeLink);
    $(HomePageElements.Inputs.TICKER).on('keyup', handleTickerInputChange);
    $(HomePageElements.Inputs.PRICE).on('keyup', handlePriceInputChange);
    $(HomePageElements.Inputs.WATCH_TYPE).on('change', handlePriceInputChange);
    $(HomePageElements.Inputs.EMAIL).on('keyup', handleEmailInputChange);
}


// user changed the watch type value
function updateTickerTypeLink() {
    const radioValue = HomePageElements.getTickerTypeValue();
    const newUrl = `${window.location.pathname}/${radioValue}`;

    HomePageElements.setNextPageUrlValue(newUrl);
}

// change in ticker input
function handleTickerInputChange() {
    const tickerValue = HomePageElements.getTickerValue();
    if (tickerValue.length == 0) {
        HomePageElements.toggleNextPageButtonDisabled(true);
        return;
    }

    const newUrl = `${window.location.pathname}/${tickerValue}`;
    HomePageElements.setNextPageUrlValue(newUrl);
    HomePageElements.toggleNextPageButtonDisabled(false);
}

// change in price input
function handlePriceInputChange() {
    const priceValue = HomePageElements.getPriceValue();
    if (priceValue.length == 0) {
        HomePageElements.toggleNextPageButtonDisabled(true);
        return;
    }

    const watchTypeValue = HomePageElements.getWatchTypeValue();
    const newUrl = `${window.location.pathname}/${priceValue}/${watchTypeValue}`;
    HomePageElements.setNextPageUrlValue(newUrl);
    HomePageElements.toggleNextPageButtonDisabled(false);
}

// change in email input
function handleEmailInputChange() {
    const emailValue = HomePageElements.getEmailValue();
    if (emailValue.length == 0) {
        HomePageElements.toggleSubmitButtonDisabled(true);
        return;
    }

    HomePageElements.toggleSubmitButtonDisabled(false);
}