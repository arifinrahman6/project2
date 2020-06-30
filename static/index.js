// last_channel = localStorage.getItem('last_channel')
// if(last_channel != null) {
//     localStorage.removeItem('last_channel');
//     window.location.replace(last_channel);
// }

// channels = {{ channels }};
// channels.array.forEach(channel => {
//     li = document.createElement('li');
//     li.innerHTML = '<a href="{{ url_for(\'channel\', channel_name=channel) }}">{{ channel }}</a>';
//     document.querySelector('ul').append(li);
// });




// // Connect to websocket
// var socket = io();

// socket.on('connect', () => {
//     document.getElementById('channel_form').onsubmit = function() { 
//         const new_channel = document.getElementById('new_channel').value;
//         socket.emit('create channel', new_channel);
//     };
// });

// socket.on('add channel', new_channel => {
//     const li = document.createElement('li');
//     li.innerHTML = new_channel;
//     document.querySelector('ul').append(li);
// });