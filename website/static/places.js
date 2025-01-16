function initAutocomplete() {
    // Access the input element
    const input = document.getElementById('autocomplete');

    // Ensure the element exists
    if (!input) {
        console.error('Element with ID "autocomplete" not found.');
        return;
    }
    // Create a new Autocomplete instance
    const autocomplete = new google.maps.places.Autocomplete(input, {
        types: ['establishment'],
        componentRestrictions: { country: 'us' },
        fields: ['place_id', 'geometry', 'name', 'url'],
        strictBounds: false
    });

    // Add a listener for the place_changed event
    autocomplete.addListener('place_changed', () => {
        const place = autocomplete.getPlace();
        if (place.geometry) {
            // Place details
            let shop = place.name
            let url = place.url

             // Send the shop name to the server via an AJAX request
            fetch('/save_note', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ note: shop.concat("#",url,"#",'0')})
            }).then((_res) => {
                window.location.href = "/";
            });
        }
    });

}
initAutocomplete()