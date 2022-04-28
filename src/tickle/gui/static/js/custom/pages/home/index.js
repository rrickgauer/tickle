
import { HomePageElements } from "./form-elements";
import { WatchCreationInterface } from "./form-submission";
import { ApiWrapper } from "../../classes/api-wrapper";
import { TickerSearchInput } from "./ticker-search";

/**********************************************************
Main logic
**********************************************************/
$(document).ready(function() {
    addEventListners();
    TickerSearchInput.initSearchInput();
});


/**
 * Add the page event handlers
 */
function addEventListners() {
    $(HomePageElements.Buttons.SUBMIT).on('click', handleFormSubmission);
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
 * Show the success alert
 */
function showSuccessfulRequest() {

    console.log('successful post');

}