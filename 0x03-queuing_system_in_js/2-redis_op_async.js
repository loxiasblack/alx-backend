const { createClient, print } = require('redis');
const { promisify } = require('util');

const client = createClient()
    .on('connect', () =>{
        console.log('Redis client connected to the server');
    })
    .on('error', (err) => {
        console.log(`Redis client not connected to the server: ${err}`);
    })
    
const asyncGet = promisify(client.get).bind(client);

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, print);
}


const displaySchoolValue = async (schoolName) => {
    await asyncGet(schoolName)
            .then((reply) => {
                console.log(reply);
            })
            .catch((err) => {
                console.log(err)});
}

(async () => {
    await displaySchoolValue('Holberton');        
    setNewSchool('Holberton', '100');
    await displaySchoolValue('Holberton');
})();
