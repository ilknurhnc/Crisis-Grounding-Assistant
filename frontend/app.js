const saveProfileButton = document.getElementById("saveProfileButton");
const sendButton = document.getElementById("sendButton");

const profileStatus = document.getElementById("profileStatus");
const responseBox = document.getElementById("responseBox");

function splitInput(value) {
    return value
        .split(",")
        .map(item => item.trim())
        .filter(item => item.length > 0);
}

saveProfileButton.addEventListener("click", async () => {
    const profile = {
        calming_colors: splitInput(document.getElementById("colorsInput").value),
        safe_phrases: splitInput(document.getElementById("phrasesInput").value),
        helpful_activities: splitInput(document.getElementById("activitiesInput").value),
        triggers: splitInput(document.getElementById("triggersInput").value)
    };

    profileStatus.innerHTML = "Saving profile...";

    try {
        const response = await fetch("http://localhost:8000/profile/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(profile)
        });

        const data = await response.json();

        if (!response.ok) {
            profileStatus.innerHTML = `Error: ${JSON.stringify(data)}`;
            return;
        }

        profileStatus.innerHTML = data.message;

    } catch (error) {
        console.error("Profile save error:", error);
        profileStatus.innerHTML = "Could not connect to the API.";
    }
});

sendButton.addEventListener("click", async () => {
    const message = document.getElementById("messageInput").value.trim();

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

        if (!response.ok) {
            responseBox.innerHTML = `<p>API error: ${JSON.stringify(data)}</p>`;
            return;
        }

        responseBox.innerHTML = `
            <p><strong>Your message:</strong> ${data.input_message}</p>
            <p><strong>Support:</strong> ${data.support_message}</p>
        `;

    } catch (error) {
        console.error("Check-in error:", error);
        responseBox.innerHTML = "Could not connect to the API.";
    }
});