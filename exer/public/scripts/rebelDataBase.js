let errorArray = [];
/**
 * @summary. Checks if a string is alphanumeric
 * @description. Check if a string is alphanumeric (spaces allowed) using a regex
 * @param {string} toValidate String to check 
 * 
 * @returns {boolean} true if string is alphanumeric or false otherwise
 */
function alphanumericChecker(toValidate) {
    const regex = /^[A-Za-z0-9 ]+$/;
    if (toValidate.match(regex)) {
        return true;
    }
    else {
        errorArray.push("Name should be alphanumeric");
        return false;
    }
}
/**
 * @summary. Checks if a string length is between 2 and 50
 * @param {string} toValidate String to check 
 * @returns {boolean} true if string is correct or false otherwise
 */
function lengthChecker(toValidate) {
    if (toValidate.length > 2 && toValidate.length < 50) {
        return true;
    } else {
        errorArray.push("Name lenght error");
        return false;
    }
}
/**
 * @summary. Sends a request to upload the rebel
 * @description Sends a request with the rebel name and the planet name to the server...
 * @param {string} name name of the rebel to add
 * @param {string} planet name of the planet to add
 * @returns {boolean} true if string is correct or false otherwise
 */
function sendRebelToServer(name, planet) {
    $.get('/addRebel', {"name": name, "planet": planet})
    .done(function (result) {
        if (result.includes("PERMERROR")){
            console.error("Permission error, try again later");
        } else if (result.includes("FIELDERROR")) {
            console.error("Please fill the two fields");
        } else if (result.includes("CONFIGERROR")){
            console.error("Config file not found, try again later");
        } 
        else {
           console.log("Uploaded!!!!");
        }
        }).fail(function (result) {
            console.log(result)
            console.log("Upload fail");
        });
}
/**
 * WIP
 */
function validateForm() {
    errorArray = [];
    let name = $("#rName").val().trim();
    let planet = $("#rPlanet").val().trim();
    console.log(name);
    if (alphanumericChecker(name) && lengthChecker(name)) {
        console.log("bien");
        sendRebelToServer(name, planet);
    } else {
        console.log(errorArray);
        console.log("mal");
    }
}
$(document).ready(function () {
});