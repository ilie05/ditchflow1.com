const socket = io(`http://${document.domain}:${location.port}/sensor`);
socket.on('connect', function () {
    console.log("Connected")
});

socket.on('sensor_notification', function (data) {
    let card = $(`.cards-container [itemid=${data.id}]`);
    if (!card.length) return;

    $(card).find('li.sName').text(`Sensor Name: ${data.name}`);
    $(card).find('li.sWater').text(`Water Level: ${data.water} inches`);
    $(card).find('li.sBattery').text(`Battery Voltage: ${data.battery} V`);
    $(card).find('li.sTemperature').text(`Temperature: ${data.temperature} °F`);
    $(card).find('li.sFloat').text(`Float: ${data.float ? 'UP' : 'DOWN'}`);
    $(card).find('li.sLastSeen').text(`Last seen: ${data.last_update}`);

    $(card).find('.card-front').removeClass('offline-indicator');
});