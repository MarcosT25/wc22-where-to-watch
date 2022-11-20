function getFormData(form) {
    return {
        people: form['people'].value,
        party: form['party'].value,
        budget: form['budget'].value,
        food: form['food'].value,
        watch: form['watch'].value,
        transport: form['transport'].value
    }
}

function sendData() {
    event.preventDefault();
    let url = "http://localhost:5000/get-data";

    const form = document.forms["myForm"];
    const data = getFormData(form);
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
            let result = document.getElementById("result");
            result.innerHTML = JSON.stringify(d);
            // TODO mudar a classe de um elemento para pop up
        }).catch((e) => {
            console.log(e);
        })
}
