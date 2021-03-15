<?
session_start();
include "config.php";
$username = $_SESSION['username'];
$query = "SELECT * FROM users WHERE username='$username'";
$res = mysqli_query($connect, $query);
$data = mysqli_fetch_assoc($res);
if ($data['username']==$username) {
	if ($data['pol'] == "мъж"){
		$a = "selected";
	}elseif ($data['pol'] == "жена"){
		$b = "selected";
	}
	if ($_POST['submit']) {
	$name = htmlspecialchars($_POST['name']);
	$avatar = $_POST['avatar'];
	$icq = htmlspecialchars($_POST['icq']);
	$skype = $_POST['skype'];
	$pol = $_POST['pol'];
	$signature = htmlspecialchars($_POST['signature']);
	$zaqvka = "UPDATE users SET name='$name', avatar='$avatar', icq='$icq', skype='$skype', pol='$pol', signature='$signature' WHERE username='$username'";
	mysqli_query($connect, $zaqvka);
	echo "
	<div class='post'>
	<h2 class='title'> Редактиране на профил </h2>
	<div class='text'>
	<p>Профила е обновен. <a href='index.php'>Назад</a></p>
	</div>
	</div>
	";
	}else{
	echo "
	<div class='post'>
	<h2 class='title'>Редактиране на профил </h2>
	<div class='text'>
	<form method='post' action='?page=profile_edit'>
	<table>
	<tr><td><b>Име: </b></td><td style='font-size:10px;'><input type='text' name='name' value='$data[name]' size='30'><br>Вашето име.</td></tr>
	<tr><td><b>Аватар: </b></td><td style='font-size:10px;'><input type='text' name='avatar' value='$data[avatar]' size='30'><br>URL адрес до картинката.</td></tr>
	<tr><td><b>ICQ: </b></td><td style='font-size:10px;'><input type='text' name='icq' value='$data[icq]' size='30'><br>ICQ номер.</td></tr>
	<tr><td><b>Skype: </b></td><td style='font-size:10px;'><input type='text' name='skype' value='$data[skype]' size='30'><br>Скайп името ви.</td></tr>
	<tr><td><b>Пол: </b></td><td style='font-size:10px;'>
	<select name='pol'>
	<option value=''>-- Избери --</option>
	<option $a value='мъж'>Мъж</option>
	<option $b value='жена'>Жена</option>
	</select><br>Вашият пол.</td></tr>
	<tr><td><b>Подпис: </b></td><td style='font-size:10px;'><textarea name='signature' cols='40' rows='7'>$data[signature]</textarea><br>Забранени са всякакъв вид HTML, CSS и BB кодове.</td></tr>
	<tr><td></td><td><input type='submit' name='submit' value='Редактирай' style='background:#fff;border:1px dashed #000;color:red;font-weight:bold'></td></tr>
	</table>
	</form>
	</div>
	</div>
	";
	}
	}else{
		echo "<h2>Нямаш достъп до тази страница.</h2>";
	}
