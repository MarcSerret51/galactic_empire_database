let errorArray = [];
/**
 * @summary. Checks if a string is alphanumeric
 * @description. Check if a string is alphanumeric using a regex
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
function lengthChecker(toValidate) {
    if (toValidate.length > 2 && toValidate.length < 50) {
        return true;
    } else {
        errorArray.push("Name lenght error");
        return false;
    }
}
function sendRebelToServer(name, planet) {
    $.post('/addRebel', { "name": name, "planet": planet })
        .done(function (result) {
            console.log("Uploaded!!!!");
        }).fail(function (result) {
            console.log("Upload fail");
        });
}
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
    validateForm();
});