const spawner = require('child_process').spawn;

// string
const data_to_pass_in = "what is machine learning, explain in 50 words";

console.log("data send to python script:" , data_to_pass_in);

const python_process = spawner('python',['./vivek.py', JSON.stringify(data_to_pass_in)]);

python_process.stdout.on('data', data =>{
    console.log("data recieved from python script: ", data.toString());
}
)






