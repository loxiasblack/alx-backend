const { createClient, print } = require('redis');



const client = createClient()
    .on('connect', () =>{
        console.log('Redis client connected to the server');
    })
    .on('error', (err) => {
        console.log(`Redis client not connected to the server: ${err}`);
    })


const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, print);
}

const displaySchoolValue = (schoolName) => {
    client.get(schoolName, (err, reply) => {
        console.log(reply);
    });
}

displaySchoolValue('Holberton');
setNewSchool('Holberton', '100');
displaySchoolValue('Holberton');
