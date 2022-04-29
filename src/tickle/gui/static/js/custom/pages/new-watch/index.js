
import { HomePageElements } from "./form-elements";
import { WatchCreationInterface } from "./form-submission";
import { ApiWrapper } from "../../classes/api-wrapper";
import { TickerSearchInput } from "./ticker-search";
import { PageAlert } from "../../classes/page-alert";
import { Utilities } from "../../classes/utilities";
import { PriceResponse } from "../../views/price-response";

/**********************************************************
Main logic
**********************************************************/
$(document).ready(function() {
    addEventListners();
    TickerSearchInput.initSearchInput();
    PageAlert.init();
});


/**
 * Add the page event handlers
 */
function addEventListners() {
    $(HomePageElements.Buttons.SUBMIT).on('click', handleFormSubmission);
    $(HomePageElements.Inputs.TICKER).on('change', fetchTickerPrice);
}

/** 
 * Submit watch to the api 
 */
async function handleFormSubmission() {
    if (!HomePageElements.validateForm()) {
        return;
    }

    HomePageElements.spinSubmitButton();

    const formInterface = new WatchCreationInterface();
    const watchModel = formInterface.getWatchModel();

    const apiResponse = await ApiWrapper.postWatch(watchModel);
    if (apiResponse.ok) {
        showSuccessfulRequest();
    }
    else {
        console.error(await apiResponse.text());
    }

    HomePageElements.resetSubmitButton();
}

/**
 * Show the success alert and reset the form
 */
function showSuccessfulRequest() {
    Utilities.jumpToPageTop();
    PageAlert.setNormalText('Success! Be sure to check your email for the alert.');
    PageAlert.show();
    HomePageElements.resetForm();
    TickerSearchInput.reset();
}


async function fetchTickerPrice() {
    HomePageElements.toggleCurrentTickerPriceValue(false);
    HomePageElements.setCurrentTickerPriceValue('');
    const tag = HomePageElements.getTagValue();
    const apiResponse = await ApiWrapper.getPrice(tag);

    if (apiResponse.ok) {
        const apiResponseData = await apiResponse.json();
        const priceData = new PriceResponse(apiResponseData.data);
        HomePageElements.setCurrentTickerPriceValue(priceData.last);
        HomePageElements.toggleCurrentTickerPriceValue(true);
    }
    else {
        console.error(await apiResponse.text());
    }
}