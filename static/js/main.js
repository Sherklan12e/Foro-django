///alert


let alertButton = document.querySelector('[close]');
let alert = document.getElementById(['alert']);


if (alertButton) {
    alertButton.addEventListener('click', () => {
    alert.classList.toggle('hidden')
})
}
//websocket stuff

const roomId = JSON.parse(document.getElementById('json-roomid').textContent)
const userName = JSON.parse(document.getElementById('json-username').textContent)

const chatSocket = new WebSocket(
    'ws://' + windows.location.host + '/ws/' + roomId + '/'

)
chatSocket.onmessage = function (e){
    console.log('onmessage')
}
chatSocket.onclose = function (e) {
    console.log('onclose')
}
chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);

    if (data.username == userName){
        document.querySelector('#chat-body').innerHTML +=

        `<li class="flex justify-end">
            <div class="rounded-lg relative max-w-xl px-4 py-2 font-mono bg-sky-500 text-sky-50">
                <span class="block">
                    ${data.message}

                </span>
            </div>
        </li>
        `
    }else{
        `
        <li class="flex justify-start">
            <div class=" rounded-lg relative max-w-xl px-4 py-2 font-mono bg-sky-500 text-sky-50">
                <span class="block">
                ${data.username} ${data.message}

                </span>
            </div>

        </li>
        
        `
    }


}
document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function (e) {
    if (e.keyCode == 13){
        document.querySelector('#chat-message-submit').click();

    }
}
document.querySelector('#chat-message-submit').onclick = function (e) {
    e.preventDefault()
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;

    chatSocket.send(JSON.stringify({
        'message':message,
        'username':userName,
        'room':roomId
    }))
    messageInputDom.value = '';
    return false
}