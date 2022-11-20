function getFormData(form) {
    return {
        people: form['people'].value,
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
            let url = window.location.href;
            url = url.replace('index', d.lugar);
            console.log(url);
            window.location.href = url;
        }).catch((e) => {
            console.log(e);
        })
}
