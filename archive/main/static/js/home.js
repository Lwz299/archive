var file = document.getElementById("sel-file");
var display = document.getElementById("display");
var x
var reader = new FileReader();
file.addEventListener("change", function() {
        var url = URL.createObjectURL(file.files[0])
            //display.setAttribute("type", file.files[0].type);
        display.setAttribute("src", url);




    })
    ////////set size of ifrmae content////////