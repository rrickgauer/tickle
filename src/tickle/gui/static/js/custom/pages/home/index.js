
import { HomePageElements } from "./form-elements";
import { UrlFormValues } from "./url-form-values";
import { TickerSelect } from "./ticker-select";
import { TickerTypes } from "../../domain/enums";
import { WatchCreationInterface } from "./form-submission";
import { ApiWrapper } from "../../classes/api-wrapper";


const m_urlFormValues = new UrlFormValues();


/**********************************************************
Main logic
**********************************************************/
$(document).ready(function() {
    addEventListners();
    initTickerSelect();
});


/**
 * Add the page event handlers
 */
function addEventListners() {
    $(HomePageElements.Inputs.TICKER_TYPE).on('change', updateTickerTypeLink);
    $(HomePageElements.Inputs.TICKER).on('change', handleTickerInputChange);
    $(HomePageElements.Inputs.PRICE).on('keyup', handlePriceInputChange);
    $(HomePageElements.Inputs.WATCH_TYPE).on('change', handlePriceInputChange);
    $(HomePageElements.Inputs.EMAIL).on('keyup', handleEmailInputChange);
    $(HomePageElements.Buttons.SUBMIT).on('click', handleFormSubmission);
}


/**
 * User changed the watch type value
 */
function updateTickerTypeLink() {
    const radioValue = HomePageElements.getTickerTypeValue();
    const newUrl = `${window.location.pathname}/${radioValue}`;

    HomePageElements.setNextPageUrlValue(newUrl);
}


/**
 * Change in ticker input
 */
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


/**
 * Change in price input
 */
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

/**
 * Change in email input
 */
function handleEmailInputChange() {
    const emailValue = HomePageElements.getEmailValue();
    if (emailValue.length == 0) {
        HomePageElements.toggleSubmitButtonDisabled(true);
        return;
    }

    HomePageElements.toggleSubmitButtonDisabled(false);
}

/**
 * Initialize the select2 library
 */
function initTickerSelect() {
    if (m_urlFormValues.tickerType == null) {
        return;
    } 
    else if (m_urlFormValues.ticker != null) {
        return;
    }

    const tickerType = parseInt(m_urlFormValues.tickerType);

    if (tickerType == TickerTypes.CRYPTO) {
        TickerSelect.initCryptoSelect();
    }
    else {
        TickerSelect.initStocksSelect();
    }
}

/** 
 * Submit watch to the api 
 */
async function handleFormSubmission() {
    HomePageElements.spinSubmitButton();

    const formInterface = new WatchCreationInterface();
    const watchModel = formInterface.getWatchModel();

    const apiResponse = await ApiWrapper.postWatch(watchModel);
    if (apiResponse.ok) {
        console.log('success');
        console.log(await apiResponse.json());

        showSuccessfulRequest();
    }
    else {
        console.error(await apiResponse.text());
    }

    HomePageElements.resetSubmitButton();
}

/**
 * Show the success alert
 */
function showSuccessfulRequest() {
    $('#section-form').addClass('d-none');
    $('#section-body-top').addClass('d-none');
    $('#section-watch-created').removeClass('d-none');
}