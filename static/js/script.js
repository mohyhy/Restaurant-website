let menu = document.querySelector('#menu-bars');
let navbar = document.querySelector('.navbar');
const sign_in_btn = document.querySelector("#sign-in-btn")
const sign_up_btn = document.querySelector("#sign-up-btn")
const sign_in_btn2 = document.querySelector("#sign-in-btn2")
const sign_up_btn2 = document.querySelector("#sign-up-btn2")
const cont = document.querySelector(".container")



menu.onclick = () =>{
  menu.classList.toggle('fa-times');
  navbar.classList.toggle('active');
}

let section = document.querySelectorAll('section');
let navLinks = document.querySelectorAll('header .navbar a');

window.onscroll = () =>{

  menu.classList.remove('fa-times');
  navbar.classList.remove('active');

  section.forEach(sec =>{

    let top = window.scrollY;
    let height = sec.offsetHeight;
    let offset = sec.offsetTop - 150;
    let id = sec.getAttribute('id');

    if(top >= offset && top < offset + height){
      navLinks.forEach(links =>{
        links.classList.remove('active');
        document.querySelector('header .navbar a[href*='+id+']').classList.add('active');
      });
    };

  });

}

document.querySelector('#search-icon').onclick = () =>{
  document.querySelector('#search-form').classList.toggle('active');
}

document.querySelector('#close').onclick = () =>{
  document.querySelector('#search-form').classList.remove('active');
}







var cart_btn = document.querySelector('#cartbtn');
var cart_side = document.querySelector(".cart-sidebar")
var close_cart  = document .querySelector(".close-icon")
var cover = document.querySelector(".cover")


cart_btn.onclick = () => {
  cover.style.right = "0";
  cart_side.style.right = "0";
  $('html, body'). css({ overflow: 'hidden'});
}

close_cart.onclick = () => {
  cover.style.right = "-400%";
  cart_side.style.right = "-400px";
  $('html, body'). css({ overflow: 'auto'});
}
  


