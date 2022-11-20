function sendData() {
    event.preventDefault();
    let url = "http://localhost:5000/get-data";
    let input = document.forms["myForm"]["budget"].value;
    let data = { "input": input }
    let options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }
    let fetchRes = fetch(
        url,
        options);
    fetchRes.then(res =>
        res.json()).then(d => {
            let result = document.createElement("p");
            result.innerHTML = JSON.stringify(d);
            document.querySelector("body").appendChild(result);
            // TODO mudar a classe de um elemento para pop up
        }).catch((e) => {
            console.log(e);
        })
}