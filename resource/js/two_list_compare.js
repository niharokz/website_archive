
function getText() {
    var text1 = document.getElementById("textbox1").value;
    const array1 = text1.split('\n');
    var text2 = document.getElementById("textbox2").value;
    const array2 = text2.split('\n');
    var array3 = array1.filter(function(obj) { return array2.indexOf(obj) == -1; });
    var array4 = array2.filter(function(obj) { return array1.indexOf(obj) == -1; });
    var array5 = array2.filter(function(obj) { return array1.indexOf(obj) != -1; });
    var array6 = array3 + ',' + array4 + ',' + array5;
    document.getElementById("textbox3").value = array3.toString().split(',').join("\r\n");
    document.getElementById("textbox4").value = array4.toString().split(',').join("\r\n");
    document.getElementById("textbox5").value = array5.toString().split(',').join("\r\n");
    document.getElementById("textbox6").value = array6.toString().split(',').join("\r\n");
    document.getElementById('divMsg').style.display = 'flex';
}
function unique(textbox) {
    var text = document.getElementById(textbox).value;
    const array = text.split('\n');
    var uniquearray = array.filter(function(item, pos) { return array.indexOf(item) == pos; });
    document.getElementById(textbox).value = uniquearray.toString().split(',').join("\r\n");
}

