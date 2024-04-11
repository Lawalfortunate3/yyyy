
var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:', productId, 'Action:', action)
		console.log('USER:', user)

		if (user == 'AnonymousUser'){ 
			addCookieItem(productId, action)
		}else{
			updateUserOrder(productId, action)
		}
	})
}

function updateUserOrder(productId, action){
	console.log('User is authenticated, sending data...')

		var url = '/update_item/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'productId':productId, 'action':action})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
		    location.reload()
		});
}

function addCookieItem(productId, action){
	console.log('User is not authenticated')

	if (action == 'add'){
		if (cart[productId] == undefined){
		cart[productId] = {'quantity':1}

		}else{
			cart[productId]['quantity'] += 1
		}
	}

	if (action == 'remove'){
		cart[productId]['quantity'] -= 1

		if (cart[productId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[productId];
		}
	}
	console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	
	location.reload()
}






/....NAVBAR CLICK TO DROP.../   
                    
// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
if (!event.target.matches('.dropbtn')) {
var dropdowns = document.getElementsByClassName("dropdown-content");
for (var i = 0; i < dropdowns.length; i++) {
var openDropdown = dropdowns[i];
if (openDropdown.style.display === "block") {
openDropdown.style.display = "none";
}
}
}
}


const bar = document.getElementById('bar');
const close = document.getElementById('close');
const nav = document.getElementById('navbar');

if (bar) {
bar.addEventListener('click', () => {
nav.classList.add('active');
})
}

if (close) {
close.addEventListener('click', () => {
nav.classList.remove('active');
})
} 

/...SPRODUCT HTML, CLICK TO CHANGE INAGE SAMPLE.../ 

var mainimg = document.getElementById ('mainimg');
var smallimg = document.getElementsByClassName ('small-img');

smallimg[0].onclick = function() {
mainimg.src = smallimg[0].src;
}
smallimg[1].onclick = function() {
mainimg.src = smallimg[1].src;
}
smallimg[2].onclick = function() {
mainimg.src = smallimg[2].src;
}
smallimg[3].onclick = function() {
mainimg.src = smallimg[3].src;
}