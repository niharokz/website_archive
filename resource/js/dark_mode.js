let darkMode = localStorage.getItem('darkMode'); 
var checkbox = document.querySelector('input[name=theme]');
if(darkMode!='enabled') {
 document.documentElement.setAttribute('data-theme', 'light')
 checkbox.checked = true
} else {
 document.documentElement.setAttribute('data-theme', 'dark')
 checkbox.checked = false 
}
checkbox.addEventListener('change', function() {
 if(this.checked) {
  trans()
  document.documentElement.setAttribute('data-theme', 'light')
  localStorage.setItem('darkMode', null);
 } else {
  trans()
  document.documentElement.setAttribute('data-theme', 'dark')
  localStorage.setItem('darkMode', 'enabled');
  }
})
let trans = () => {
 document.documentElement.classList.add('transition');
 window.setTimeout(() => {
  document.documentElement.classList.remove('transition')
 }, 1000)
}
