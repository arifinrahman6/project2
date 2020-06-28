// Connect to websocket
var socket = io();

socket.on('connect', () => {
    document.getElementById('chat').onsubmit = function() { 
        var today = new Date();
        var date = today.getDate() + '/' + (today.getMonth()+1) + '/' + today.getFullYear();
        var time = today.getHours() + ":" + today.getMinutes();
        var date_time = date+' '+time;

        const message = document.getElementById('message').value;
        socket.emit('send message', {'message': message, 'datetime': date_time});
    };
});

socket.on('receive message', data => {
    const li = document.createElement('li');
    li.innerHTML = data.message + ', ' + data.datetime + ', ' + data.name;
    document.querySelector('ul').append(li);
});

window.onbeforeunload = function () {
    return "Do you really want to close?";
};