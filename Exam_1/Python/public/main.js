async function sendCommand(command) {
    let response = await fetch(`/api/${command}`);
    let replyText = await response.text();
    console.log(replyText);

    document.querySelector("#replyText").innerHTML = replyText;

    return replyText;
}

function main() {
    console.log("Hello JavaScript");
    // document.querySelector("#reset").innerHTML = "Hello";



    document.querySelector("#LEDon").onclick = () => {
        sendCommand("led/on");
    };
    document.querySelector("#LEDoff").onclick = () => {
        sendCommand("led/off");
    };

    document.querySelector("#FLASH").onclick = () => {
      let numFlash = document.querySelector("#numFlash").value;
      let perFlash = document.querySelector("#perFlash").value;
      sendCommand(`flash/${numFlash}/${perFlash}`);
      
    }

}


main();