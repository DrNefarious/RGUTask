// api url
const api_url = 
      "http://127.0.0.1:5000/scores";
  
// Defining async function
async function getapi(url) {
    
    // Storing response
    const response = await fetch(url);
    
    // Storing data in form of JSON
    var data = await response.json();
    console.log(data);
}
// Calling that async function
getapi(api_url);