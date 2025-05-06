function updateData() {
    fetch('/get_data')
        .then(response => response.json())
        .then(data => {
            document.getElementById('temperature').innerText = data.temperature.toFixed(2);
            document.getElementById('power').innerText = data.power.toFixed(2);
            tempChart.data.labels.push(data.timestamp);
            tempChart.data.datasets[0].data.push(data.temperature);
            powerChart.data.labels.push(data.timestamp);
            powerChart.data.datasets[0].data.push(data.power);
            if (tempChart.data.labels.length > 60) {
                tempChart.data.labels.shift();
                tempChart.data.datasets[0].data.shift();
            }
            if (powerChart.data.labels.length > 60) {
                powerChart.data.labels.shift();
                powerChart.data.datasets[0].data.shift();
            }
            tempChart.update();
            powerChart.update();
        });
}

setInterval(updateData, 1000);

document.getElementById('saveButton').addEventListener('click', function() {
    fetch('/save_data', {method: 'POST'})
        .then(response => response.text())
        .then(text => console.log(text));
});