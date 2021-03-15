<? 
session_start();
$username = $_SESSION['username'];
$query = "SELECT * FROM users WHERE username='$username'";
$res = mysqli_query($connect, $query);
$data = mysqli_fetch_assoc($res);
if ($data['admin'] == 1) {
$id = $_GET['id'];
if ($id) {
$sql = "SELECT * FROM users WHERE id='$id'";
$result = mysqli_query($connect, $sql);
$row = mysqli_fetch_assoc($result);
	if ($_POST['submit']) {
	$admin = $_POST['admin'];
	$zaqvka = "UPDATE users SET admin='$admin' WHERE id='$id'";
	mysqli_query($connect, $zaqvka);
	echo "
	<div class='post'>
	<h2 class='title'>Админ панел</h2>
	<p class='posted'>Логнат като $username.</p>
	<div class='text'>
	<p><a href='javascript:history.go(-1);' title='Назад'><img src='images/back.png' alt='back'></a></p>
	<p>Правата са обновени. <a href='index.php'>Назад</a></p>
	</div>
	</div>
	";
	}else{
	echo "
	<div class='post'>
	<h2 class='title'>Админ панел</h2>
	<p class='posted'>Логнат като $username.</p>
	<div class='text'>
	<p><a href='javascript:history.go(-1);' title='Назад'><img src='images/back.png' alt='back'></a></p>
	<form method='post' action='?page=addadmin&amp;id=$id'>
	<table>
	<tr><td><b>Потребител: </b></td><td>$row[username]</td></tr>
	<tr><td><b>Имейл: </b></td><td>$row[email]</td></tr>
	<tr><td><b>Права: </b></td><td>";
	if ($row['admin'] == 1){
	$admin = "selected='selected'";
	}else{
	$user = "selected='selected'";
	}
	echo"<select name='admin'>
	<option value='' $user>Потребител</option>
	<option value='1' $admin>Администраторски права</option>
	</select>
	</td></tr>
	<tr><td></td><td><input type='submit' name='submit' value='Редактирай' style='background:#fff;border:1px dashed #000;color:red;font-weight:bold'></td></tr>
	</table>
	</form>
	</div>
	</div>
	";
	}
}
else {
echo "
<div class='post'>
<h2 class='title'>Админ панел</h2>
<p class='posted'>Логнат като $username.</p>
<div class='text'>
<p><a href='javascript:history.go(-1);' title='Назад'><img src='images/back.png' alt='back'></a></p>
<table style='width:600px;'>
";
$query = "SELECT * FROM users ORDER BY id";
$res = mysqli_query($connect, $query);
$broi = mysqli_num_rows($res);
while($data = mysqli_fetch_assoc($res)) {
	echo "
	<tr>
	<td style='border-bottom:1px dotted black;'>$data[username]</td>
	<td style='text-align:right;border-bottom:1px dotted black;'>
	[ <a href='?page=addadmin&amp;id=$data[id]'><img src='images/edit.png' alt='Добави права' width='12'></a> ]
	</td>
	</tr>";
}
echo "
</table>
<br>
Имаме общо <b>$broi</b> регистрирани потребителя.
</div>
</div>";
}
}else{
	echo "<h2>Нямаш достъп до тази страница.</h2>";
}

?>