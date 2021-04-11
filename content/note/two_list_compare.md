---
title : "Two List Comparer : Union, Join, Intersection"
subtitle : "Compare two lists, remove duplicates, check unions and intersections, unique sets, based on vanilla javascript"
date : 2020-12-06
showInHome : "No"
meta : '
<link rel="stylesheet" type="text/css" media="screen" href="/extra.css" /> 
<script src="/two_list_compare.js"></script>
'
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


