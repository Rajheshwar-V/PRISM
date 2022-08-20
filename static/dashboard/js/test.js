const button = document.querySelector(".submit1");
button.addEventListener("click", async function () {
  const base64_1 = document.getElementById("imgdis1").src;
  let image1;
  const base64_2 = document.getElementById("imgdis2").src;
  let image2;
  const base64_3 = document.getElementById("imgdis3").src;
  let image3;
  try {
    await fetch(base64_1)
      .then(async (res) => {
        console.log(res);
        return await res.blob();
      })
      .then((blob) => {
        image1 = blob;
      });
  } catch (error) {
    console.log(error);
    alert("Unable to upload file");
    alert("File upload success");

  }

  
  const file = new File([image1], "filename1.jpeg");
        const fields = new FormData();
        fields.append("image1", file);
        fields.append("name1", document.getElementById("name1").value);
        fields.append("type1", document.getElementById("type1").value);
        fields.append("comments", document.getElementById("w3review").value);
        const API_URL = "/save-study/";
        await fetch(API_URL, {
          method: "POST",
          body: fields,
          headers: {
            "Access-Control-Allow-Origin": "*",
            "X-CSRFToken": document.querySelector(
              "#signup-form input[name=csrfmiddlewaretoken]"
            ).value,
          },
        })
          .then(() => {
            alert("File upload success");
          })
          .catch((err) => {
            console.log(err);
            alert("File upload success");

          });
});
