let BASE_URL="http://127.0.0.1:8000/"
res_p = document.getElementById('textResultp')
function postImage(img){
    // var myHeaders = new Headers();
    // myHeaders.append("Content-Type", "application/json");

    const formData = new FormData();

    formData.append('image', img);

    const requestOptions = {
      method: 'POST',
      body: formData,
      // If you add this, upload won't work
      // headers: {
      //   'Content-Type': 'multipart/form-data',
      // }
    };

    fetch(BASE_URL+"ai_vis_detect/post_img/", requestOptions)
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
var loadFile = function(event) {
    var image = document.getElementById('output');
    image.src = URL.createObjectURL(event.target.files[0]);
    imgurl = event.target.files[0]
    console.log(imgurl)

    postImage(imgurl);
};
