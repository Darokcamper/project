var tempCtx = document.getElementById('tempChart').getContext('2d');
var tempChart = new Chart(tempCtx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Temperature',
            data: [],
            borderColor: 'red',
            fill: false
        }]
    },
    options: {
        scales: {
            x: {
                type: 'time',
                time: {
                    unit: 'second'
                }
            }
        }
    }
});

var powerCtx = document.getElementById('powerChart').getContext('2d');
var powerChart = new Chart(powerCtx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Power Consumption',
            data: [],
            borderColor: 'blue',
            fill: false
        }]
    },
    options: {
        scales: {
            x: {
                type: 'time',
                time: {
                    unit: 'second'
                }
            }
        }
    }
});