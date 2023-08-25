let BASE_URL="https://9376-103-25-231-104.ngrok-free.app/"
let textBox = document.getElementById('textInput')
let res_p = document.getElementById('textResultp')
// let button = document.getElementById('button')

// button.addEventListener("click",submit())

function submit(){
    let textInp = textBox.value
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    console.log("clicked")
    var raw = JSON.stringify({
        "text": textInp
    });

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    fetch(BASE_URL+"ai_vis_detect/post/", requestOptions)
        .then(response => response.json())
        .then(result => {
            if(result>0.5){
                res_p.innerText="It is made by an AI"
            }
            else{
                res_p.innerText="Human Generated"
            }
        })
        .catch(error => console.log('error', error));
}