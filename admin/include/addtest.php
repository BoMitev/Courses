<?php 
session_start();
$username = $_SESSION['username'];
$query = "SELECT * FROM users WHERE username='$username'";
$res = mysqli_query($connect, $query);
$data = mysqli_fetch_assoc($res);
if ($data['admin'] == 1) {
if (!$_POST['submit']) { 
echo "
	<div class='post'>
	<h2 class='title'>Админ панел</h2>
	<p class='posted'>Логнат като $username.</p>
	<div class='text'>
	<p><a href='javascript:history.go(-1);' title='Назад'><img src='images/back.png' alt='back'></a></p>
Въведете заглавие на теста:<br>"; 
echo "<form name='test' method='POST' action=''> 
<input type='text' name='ime' size='52'><br> 
Въведете описание към теста:<br> 
<textarea name='opisanie' cols='40' rows='5' class='form_elements_text'></textarea><br>
<input type='submit' name='submit' value='Добавяне'> 
</form> 
</div>
</div>"; 
} 
else { 
$ime = $_POST['ime']; 
$ime = trim(strip_tags(addslashes($ime))); //slagame malko za6tita 
$opisanie = $_POST['opisanie']; 
$opisanie = trim(strip_tags(addslashes($opisanie))); // tuk sa6to 
$query = "INSERT INTO tests (ime, opisanie) VALUES ('$ime', '$opisanie')"; 
$res = mysqli_query($connect, $query); //dobavqme testa 
if ($res) { echo "
<div class='post'>
	<h2 class='title'>Админ панел</h2>
	<p class='posted'>Логнат като $username.</p>
	<div class='text'>
Теста е добавен успешно. Можете да добавите въпроси към него от <a href='?page=addvapros'>тук</a>
</div></div>"; } 
}
}else{
	echo "<h2>Нямаш достъп до тази страница.</h2>";
}  
?>