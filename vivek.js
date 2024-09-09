const spawner = require('child_process').spawn;


// string

const data_to_pass_in = "introduce team learnet and its each team member along with our project idea";
// const data_to_pass_in = "how to login to site";
console.log("---------enterting the input chain--------")
const python_process = spawner('python',['./vivek.py', JSON.stringify(data_to_pass_in)]);

python_process.stdout.on('data', data =>{
    console.log("output:  ", data.toString());
}
)






