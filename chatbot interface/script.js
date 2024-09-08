document.getElementById('send-btn').addEventListener('click', function() {
    const userInput = document.getElementById('user-input').value;
    const chatOutput = document.getElementById('chat-output');
    
    if (userInput.trim() !== "") {
        const message = `Hello, ${userInput}!`;
        const messageElement = document.createElement('p');
        messageElement.textContent = message;
        chatOutput.appendChild(messageElement);
        
        // Clear input
        document.getElementById('user-input').value = '';
        
        // Scroll to bottom of chat
        chatOutput.scrollTop = chatOutput.scrollHeight;
    }
});