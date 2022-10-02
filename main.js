function displayHotels() {
    fetch("howdyHack2022/Jsons/Buffalo/Hotels.json")
    .then(response => {
        return response.json();
    })
    .then(data => {
        let hotels = document.getElementById("Hotels")
        hotels.innerHTML = data.Address[0]
    });
    
}