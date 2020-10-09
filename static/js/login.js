let persona = { userId: "", name: "", accessToken: "", picture: "", email: "",status:"" };

let fotoPersona=document.getElementById("fotoPersona");
let nombrePersona=document.getElementById("nombrePersona");
let emailPersona=document.getElementById("emailPersona");


window.fbAsyncInit = function () {
  FB.init({
    appId: "387976615701026",
    cookie: true,
    xfbml: true,
    version: "v8.0",
  });
};

function logIn() {
  FB.login(
    function (response) {
      if (response.status == "connected") {
        persona.status=response.status;
        persona.userId = response.authResponse.userID;
        persona.accessToken = response.authResponse.accessToken;
        FB.api("/me?fields=id,name,email,picture.type(large)", function (
          userData
        ) {
          nombrePersona.innerHTML = userData.name;
          emailPersona.innerHTML = userData.email;
          fotoPersona = userData.picture.data.url;
        });
        console.log(persona.status);
      }
    },
    { scope: "public_profile,email" }
  );
}
