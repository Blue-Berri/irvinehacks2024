
function login() {
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var user = users.find(u => u.email == email && u.password == password);
    if (user) 
    {
        return "submit";
    } 
    else 
    {
        Toast.makeText(this, "Invalid email or password", Toast.LENGTH_LONG).show();
        return "reset"
    }
}