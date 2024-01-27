var users = [
    {
        email: "ryan@uci.edu",
        password: "ryaniscool",
        name: "Ryan",
        age: 19,
        gender: "Male",
        orientation: "Straight",
        major: "Computer Science",
        pfp: image
    },
    {
        email: "tae@uci.edu",
        password: "silentsniper",
        name: "Tae",
        age: 18,
        gender: "Male",
        orientation: "Straight",
        major: "Biology",
        pfp: image
    }
]

function login() {
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var user = users.find(u => u.email == email && u.password == password);
    if (user) 
    {
        var intent = new Intent(this, MainActivity.class);
        startActivity(intent);
        finish();
    } 
    else 
    {
        Toast.makeText(this, "Invalid email or password", Toast.LENGTH_LONG).show();
    }
}