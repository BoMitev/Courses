<?
session_start();
include "config.php";
$query = mysqli_query($connect, "SELECT * FROM users WHERE username='$username'");
$data = mysqli_fetch_assoc($query);
if ($data['avatar'] == NULL)
	{
		$data['avatar'] = "images/noavatar.gif";
	}
$usernumber = mysqli_query($connect, "SELECT * FROM users");
$usernum = mysqli_num_rows($usernumber);
if ($username) {
echo "
		<h2 style='background: url(images/img06.png) repeat-x'>Добре дошъл, $username</h2>";
		echo "
		<img src='$data[avatar]' style='border: 3px double #afafaf;' alt='Няма зададен аватар' width='120' height='120'>
		<p>
		<img src='images/profile.png' width='12' height='12' alt='profile'> <a href='index.php?page=profile&amp;user=$username'>Профил</a><br>
		<img src='images/users.png' width='12' height='12' alt='users'> <a href='index.php?page=users'>Потребители</a><br>
		<img src='images/exit.png' width='12' height='12' alt='exit'> <a href='index.php?page=logout'>Излез</a>
		</p>";
		if ($data['admin'] == 1) {
		echo "
		<p><img src='images/adminpanel.png' width='12' height='12' alt='adminpanel'> <a href='./admin'>Админ панел</a><p>
		";
		}
}else{
if (!$_POST['submit']){
echo "
	<h2 style='background: url(images/img06.png) repeat-x'>Потребителски панел</h2>
	<form method='post' action='index.php?page=login'>
	<table style='width:100%;padding-bottom: 3px;color:#000;'>
	<tr><td>Потребител:</td></tr>
	<tr><td>";
	?>
	<input type="text" class="user" name="username" size="18" value="Потребител" onblur="if(this.value=='') this.value='Потребител';" onfocus="if(this.value=='Потребител') this.value='';">
	<?
	echo "</td></tr>
	<tr><td>Парола:</td></tr>
	<tr><td>"; ?>
	<input type="password" class="pass" name="password" size="18" value="Парола" onblur="if(this.value=='') this.value='Парола';" onfocus="if(this.value=='Парола') this.value='';">
	<? 
	echo "</td><td><tr><td><input style='cursor: url(\"images/link.cur\"), text;' type='submit' name='submit' value='Влез'></td></tr>
	<tr><td><a href='index.php?page=register'>Регистрирай се!</a></td></tr>
	<tr><td style='font-size:11px;'>Имаме <a href='index.php?page=users' style='text-decoration:underline'><b>$usernum</b></a> регистрирани потребителя.</td></tr>
	</table>
	</form>
	";
}else{
$username = $_POST['username'];
$password = md5($_POST['password']);
if ($username == NULL || $password == NULL) {
	echo "Попълни всички полета.";
}else{
	$sql = "SELECT * FROM users WHERE username='$username'";
	$result = mysqli_query($connect, $sql);
	$broi = mysqli_num_rows($result);
	$row = mysqli_fetch_assoc($result);
	if ($broi == 0){
	echo "
	<h2>Грешка</h2>
	<p><center>Няма такъв потребител.</center></p>";
	}else{
		if ($password == $row['password']){
		$_SESSION['username'] = $row['username'];
		echo "<meta http-equiv='refresh' content='0; URL=index.php'>";
		}else{
		echo "Грешна парола.";
	}
	}
}
}
}
?>