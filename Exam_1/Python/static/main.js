async function sendCommand(command) {
    let response = await fetch(`/api/${command}`);
    let replyText = await response.text();
    console.log(replyText);

    document.querySelector("#replyText").innerHTML = replyText;

    return replyText;
}

