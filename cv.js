
    var myName = {
        fName: "Roy", lName: "Zion"
    } 
console.log(myName.fName + ' ' + myName.lName);

var imgs = ["photos/Shefa2.png",
            "photos/Shefa3.jpeg",
            "photos/Shefa4.jpeg",
            "photos/Shefa5.jpg",
            "photos/Shefa6.JFIF",
            "photos/Shefa7.JFIF",
            "photos/Shefa8.JFIF",
            "photos/Shefa9.JPG",
            "photos/Shefa10.JFIF"];  
    var i=0;        

function StopMotion() {
setTimeout( () => {
    document.getElementById("SMimg").src= imgs[i];
    i++;
    if (i<imgs.length) {
        StopMotion(); 
        }
    else {
        i=0;
        }
    }, 800); 
}
