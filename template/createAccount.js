function checkEmail(event) {
    event.preventDefault();
    const emailInput = document.getElementById('emailInput');
    const passwordInput = document.getElementById('passwordInput');
    const email = emailInput.value;
    const password = passwordInput.value;

    // Check if email is in userData.json
    // You can use AJAX or fetch to make a request to the server and check the email

    // Assuming you have a function called checkEmailInUserData(email) that returns a promise
    checkEmailInUserData(email)
        .then((exists) => {
            if (exists) {
                alert('Account already exists');
            } else {
                // Add the email and password to userData.json
                // You can use AJAX or fetch to make a request to the server and add the data

                // Assuming you have a function called addUserToUserData(email, password) that returns a promise
                addUserToUserData(email, password)
                    .then(() => {
                        alert('Account created successfully');
                        // Redirect to profileeditor.html or any other desired page
                        window.location.href = 'profileeditor.html';
                    })
                    .catch((error) => {
                        console.error('Error adding user to userData.json:', error);
                    });
            }
        })
        .catch((error) => {
            console.error('Error checking email in userData.json:', error);
        });
}

function checkEmailInUserData(email) {
    // Implement your logic to check if the email exists in userData.json
    // You can use AJAX or fetch to make a request to the server and check the email
    // Return a promise that resolves with a boolean indicating if the email exists or not

    // Example implementation using fetch:
    return fetch('../backend/userData.json')
        .then((response) => response.json())
        .then((userData) => {
            var existingEmails = userData.find(u => u.email === email);
            return existingEmails;
        })
        .catch((error) => {
            console.error('Error fetching userData.json:', error);
            throw error;
        });
}

function addUserToUserData(email, password) {
    // Implement your logic to add the email and password to userData.json
    // You can use AJAX or fetch to make a request to the server and add the data
    // Return a promise that resolves when the data is successfully added

    // Example implementation using fetch:
    return fetch('../backend/userData.json', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
    })
        .then((response) => {
            if (!response.ok) {
                throw new Error('Failed to add user to userData.json');
            }
        })
        .catch((error) => {
            console.error('Error adding user to userData.json:', error);
            throw error;
        });
}