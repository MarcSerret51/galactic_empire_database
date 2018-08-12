let errorArray = [];
/**
 * @summary. Checks if a string is alphanumeric
 * @description. Check if a string is alphanumeric (spaces allowed) using a regex
 * @param {string} toValidate String to check 
 * 
 * @returns {boolean} true if string is alphanumeric or false otherwise
 */
function alphanumericChecker(toValidate) {
    if (toValidate.length === 0) {
        return true;                        // Contar   el campo vacio como correcto para que pete en la length y se muestre su mensaje de error.
    }
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
        errorArray.push("Lenght must be between 2 and 50");
        return false;
    }
}
/**
 * @summary. Sends a request to upload the rebel
 * @description Sends a request with the rebel name and the planet name to the server and prints the errors
 * @param {string} name name of the rebel to add
 * @param {string} planet name of the planet to add
 * @returns {boolean} true if string is correct or false otherwise
 */
function sendRebelToServer(name, planet) {
    $.get('/addRebel', {"name": name, "planet": planet})
    .done(function (result) {
        $("#console").empty();
        if (result.includes("PERMERROR")){
            let text = $("<p class='text-danger'></p>").text("Permission error, try again later");
            $("#console").append(text);
        } else if (result.includes("FIELDERROR")) {
            let text = $("<p class='text-danger'></p>").text("Please fill the two fields");
            $("#console").append(text);
        } else if (result.includes("CONFIGERROR")){
            let text = $("<p class='text-danger'></p>").text("Config file not found, try again later");
            $("#console").append(text);
        } 
        else {
           let text = $("<p class='text-primary'></p>").text("Rebel uploaded");
            $("#console").append(text);
        }
        }).fail(function (result) {
            $("#console").empty();
            let text = $("<p class='text-danger'></p>").text("Something went wrong, try again later");
            $("#console").append(text);
        });
}
/**
 * @summary. Validates all and launch the AJAX request and prints the errors
 */
function validateForm() {
    errorArray = [];
    let name = $("#rName").val().trim();
    let planet = $("#rPlanet").val().trim();
    if (alphanumericChecker(name) && lengthChecker(name) && alphanumericChecker(planet) && lengthChecker(planet)) {
        sendRebelToServer(name, planet);
    } else {
        $("#console").empty();
        errorArray.forEach(function(error, index, array){
            let text = $("<p class='text-danger'></p>").text(error);
            $("#console").append(text);
        });
        
    }
}
$(document).ready(function () {
});