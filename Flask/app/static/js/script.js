window.onload = function(){
    setTimeout(function(){
        alert("Hello Uday!!")
    }, 5000);
};


document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.getElementById("loginForm");
    const messageDiv = document.getElementById("message");

    loginForm.addEventListener("submit", function (e) {
        e.preventDefault(); // Prevent the default form submission

        // Create FormData object to gather form data
        const formData = new FormData(loginForm);

        fetch(loginForm.action, {
            method: "POST",
            body: formData,
        })
            .then((response) => response.text())
            .then((data) => {
                if (data === "No user found") {
                    messageDiv.textContent = data; // Display the error message
                } else {
                    // Replace the current page content with the response (successful login)
                    document.open();
                    document.write(data);
                    document.close();
                }
            })
            .catch((error) => {
                console.error("Error:", error);
                messageDiv.textContent = "An error occurred. Please try again.";
            });
    });
});
