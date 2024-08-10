document.getElementById('trading-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const ticker = document.getElementById('ticker').value;

    fetch('/predict/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ ticker: ticker })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = 'Prediction: ' + (data.prediction === 1 ? 'BUY' : 'SELL');
    })
    .catch(error => console.error('Error:', error));
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
