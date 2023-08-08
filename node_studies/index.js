const axios = require('axios'); // this semicolon is optional 
axios.get('http://api.open-notify.org/astros.json')
    .then(response => {
    console.log(response.data);
    })
    .catch(error => {
        console.log(error);
    });
    