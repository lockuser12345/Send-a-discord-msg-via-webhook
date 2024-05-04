// Your webhook url
const webhookUrl = 'YOUR_WEBHOOK_URL';

// What you would like to send
const message = {
    content: 'Your message here'
};


fetch(webhookUrl, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(message),
})
.then(response => {
    if (!response.ok) {
        throw new Error('Failed to send message');
    }
    console.log('Message sent successfully');
})
.catch(error => {
    console.error('Error:', error);
});
