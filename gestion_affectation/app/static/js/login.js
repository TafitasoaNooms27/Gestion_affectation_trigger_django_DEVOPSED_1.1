$(document).ready(()=>{
	user = getSession()
	role = location.pathname.split('/')
	if (user.username == 'bda') {
		$("#current-user").text(user.username.toUpperCase())
		if(role[1] != 'bda' || role[3] == 'login') {
			location.assign('http://127.0.0.1:8000/bda/gestion_affectation/home/')
		}
	} else if (user.username == 'admin') {
		$("#current-user").text(user.username.toUpperCase())
		if(role[1] != 'administration'){
			location.assign('http://127.0.0.1:8000/administration/gestion_affectation/audit_employe/')
		}
	} else {
		if(role[3] != 'login'){
			location.assign('http://127.0.0.1:8000/bda/gestion_affectation/login/')
		}
	}
})

$('#loginbtn').click(()=>{
	username = $("input[name='username']").val()
	password = $('input[name="password"]').val()
	if (username == 'bda' && password == 'bda1') {
		setSession(username, password)
		location.reload()
	} else if (username == 'admin' && password == 'admin') {
		setSession(username, password)
		location.reload()
	} else {
		$("#alertlogin").text("Mot de passe ou nom d'utilisateur invalid!")
	}
})

$("input[name='username']").focus(()=>{
	$("#alertlogin").text("")
})

$("input[name='password']").focus(()=>{
	$("#alertlogin").text("")
})

$("#deconnexion").click(()=>{
	dropSession()
	location.reload()
})

$("#deconnexion_").click(()=>{
	dropSession()
	location.reload()
})

function getSession() {
	username = sessionStorage.getItem('username')
	password = sessionStorage.getItem('password')
	return {username: username, password: password}
}

function setSession(username, password) {
	sessionStorage.setItem('username', username)
	sessionStorage.setItem('password', password)
}

function dropSession() {
	sessionStorage.removeItem('username')
	sessionStorage.removeItem('password')
}