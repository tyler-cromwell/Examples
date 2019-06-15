/*
 * Updates the display box with the text
 * of the given verse using the AJAX technique
 * to retrieve the text without reloading
 * the page.
 */
function updateDisplay(verse) {
    // Construct file name
    verse = verse.replace(" ", "");
    verse = verse.toLowerCase();
    var url = verse + '.txt';

    fetch(url).then(function(response) {
        response.text().then(function(text) {
            poemDisplay.textContent = text;
        });
    });
};


// Grab <select> and <pre> tags
var verseChoose = document.querySelector('select');
var poemDisplay = document.querySelector('pre');


/*
 * Add an event handler that
 * fires on each dropdown selection.
 */
verseChoose.onchange = function() {
    var verse = verseChoose.value;
    updateDisplay(verse);
};


// Set initial state
verseChoose.value = 'Verse 1';  // Set dropdown selection
updateDisplay('Verse 1');       // Update display box
