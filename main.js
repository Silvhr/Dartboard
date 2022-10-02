function displayHotels() {
    fetch("howdyHack2022/Jsons/Buffalo/Hotels.json")
    .then(response => {
        return response.json();
    })
    .then(data => {
        let hotels = document.getElementById("Hotels")
        hotels.innerHTML = data.Address[0]
        // console.log(data.Address[0]);
    });
    
    //   axios({
    //     method: 'get',
    //     url: 'http://localhost:3001/',
    //   })
    //   .then(function (response) {
    //     let savedNum = document.getElementById("savedNum")
    //     savedNum.innerHTML = response.data.length
    //   });
}