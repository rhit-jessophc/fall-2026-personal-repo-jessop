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
        sendCommand("LED on");
    };
    document.querySelector("#LEDoff").onclick = () => {
        sendCommand("LED off");
    };


    document.querySelector("#gOpen").onclick = () => {
        sendCommand("GRIPPER OPEN");
    };
    document.querySelector("#gClose").onclick = () => {
        sendCommand("GRIPPER CLOSE");
    };

    document.querySelector("#FLASH").onclick = () => {
      let numFlash = document.querySelector("#numFlash").value;
      let posFlash = document.querySelector("#perFlash").value;
      sendCommand(`FLASH ${numFlash} ${posFlash}`);
      
    }

}


main();