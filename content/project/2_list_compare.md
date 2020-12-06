---
title : "Two List Comparer : Union, Join, Intersection"
subtitle : "Compare two lists, remove duplicates, check unions and intersections, unique sets, based on vanilla javascript"
showInHome : Yes
date : 2020-12-06T21:42:31Z

---


<div class ="grid align-center">    
 <div class="cell -6of12"> 
  <p>List 1</p>
  <textarea id="textbox1" name="textarea1" placeholder="List 1 paste here"></textarea><br> 
  <button value="Remove Duplicate" onclick="unique('textbox1')" type="button">Remove Duplicates</button>   
 </div>    
 <div class="cell -6of12">    
  <p>List 2</p>
  <textarea id="textbox2" name="textarea2" placeholder="List 2 paste here"></textarea><br>
  <button value="Remove Duplicate" onclick="unique('textbox2')" type="button">Remove Duplicates</button>   
 </div>    
</div>

<div class ="grid">    
 <button type="button" value="Compare List" onclick="getText()"> Compare both list </button>  
</div>

<div class ="grid align-center" id="divMsg" style="display:none">    
 <div class="cell -6of12">    
  <p>Only in List 1</p>
  <textarea id="textbox3" name="textarea3" placeholder=""></textarea>    
  <p>List 1 (and) List 2</p>
  <textarea id="textbox5" name="textarea5" placeholder=""></textarea>    
 </div>
 <div class="cell -6of12">    
  <p>Only in List 2</p>
  <textarea id="textbox4" name="textarea4" placeholder=""></textarea>    
  <p>List 1 (or) List 2</p>
  <textarea id="textbox6" name="textarea6" placeholder=""></textarea>    
 </div>    
</div>

<script> 
    function getText() {
    var text1 = document.getElementById("textbox1").value;
    const array1 = text1.split('\n');
    var text2 = document.getElementById("textbox2").value;
    const array2 = text2.split('\n');
    var array3 = array1.filter(function(obj) { return array2.indexOf(obj) == -1; });
    var array4 = array2.filter(function(obj) { return array1.indexOf(obj) == -1; });
    var array5 = array2.filter(function(obj) { return array1.indexOf(obj) != -1; });
    var array6 = array3 + ',' + array4;
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
</script>
