let darkMode = localStorage.getItem('darkMode'); 
if(darkMode!='enabled') {
  document.documentElement.setAttribute('data-theme', 'light');
  document.getElementById("theme").innerHTML = "dark-mode";
 } else {
  document.documentElement.setAttribute('data-theme', 'dark');
  document.getElementById("theme").innerHTML = "light-mode";
}
function change_theme(){
  if(document.getElementById("theme").innerHTML == "dark-mode"){
    document.documentElement.setAttribute('data-theme', 'dark')
    localStorage.setItem('darkMode', 'enabled');
    document.getElementById("theme").innerHTML = "light-mode";
  } else {
    document.documentElement.setAttribute('data-theme', 'light')
    localStorage.setItem('darkMode', null);
    document.getElementById("theme").innerHTML = "dark-mode";
  }
}
