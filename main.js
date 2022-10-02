function getCityInfo() {
    let random = Math.floor(Math.random() * 3) + 1;
    let random2 = Math.floor(Math.random() * 8);
    console.log(random);
    console.log(random2);
    fetch("howdyHack2022/Jsons/Summary/" + random.toString(10) + ".json")
    .then(response => {
        return response.json();
    })
    .then(data => {
        let name = document.getElementById("Name")
        name.innerHTML = data.Name
    });
    fetch("howdyHack2022/Jsons/Hotels/" + random.toString(10) + ".json")
    .then(response => {
        return response.json();
    })
    .then(data => {
        let hotels = document.getElementById("Hotels")
        let hotels1 = document.getElementById("Hotels1")
        hotels.innerHTML = data.Item[random2]
        hotels1.innerHTML = data.Address[random2]
    });
    fetch("howdyHack2022/Jsons/Activities/" + random.toString(10) + ".json")
    .then(response => {
        return response.json();
    })
    .then(data => {
        let act = document.getElementById("Activities")
        let act1 = document.getElementById("Activities1")
        act.innerHTML = data.Item[random2]
        act1.innerHTML = data.Address[random2]
    });
}