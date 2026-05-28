const sendButton = document.getElementById("sendButton");
const messageInput = document.getElementById("messageInput");
const responseBox = document.getElementById("responseBox");

sendButton.addEventListener("click", async () => {
    const message = messageInput.value;

    responseBox.innerHTML = "Loading...";

    try {
        const response = await fetch("http://localhost:8000/checkin/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        const data = await response.json();

        responseBox.innerHTML = `
            <p><strong>Your message:</strong> ${data.input_message}</p>
            <p><strong>Support:</strong> ${data.support_message}</p>
        `;

    } catch (error) {
        console.error(error);
        responseBox.innerHTML = "Could not connect to the API.";
    }
});