const { createClient, print } = require('redis');

const client = createClient()
    .on('connect', () =>{
        console.log('Redis client connected to the server');
    })
    .on('error', (err) => {
        console.log(`Redis client not connected to the server: ${err}`);
    })

client.subscribe('holberton school channel');

client.on('message', (channel, message) => {
    console.log(message);
    if (message === 'KILL_SERVER') {
        client.unsubscribe('holberton school channel');
        client.quit();
    }
})
