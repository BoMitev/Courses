
<?
include "config.php";
if ($_POST['submit']){
$username = htmlspecialchars($_POST['username']);
$name = htmlspecialchars($_POST['name']);
$icq = htmlspecialchars($_POST['icq']);
$skype = htmlspecialchars($_POST['skype']);
$password = $_POST['password'];
$password2 = $_POST['password2'];
$email = $_POST['email'];
$avatar = $_POST['avatar'];
$pol = $_POST['pol'];
$signature = htmlspecialchars($_POST['signature']);
$date = date('d/m/Y');
$sql = "SELECT * FROM users WHERE username='$username'";
$result = mysqli_query($connect, $sql);
$broi = mysqli_num_rows($result);
if ($username == NULL || $password == NULL || $password2 == NULL || $email == NULL) {
echo "Попълни всички полета.";
}else{
if ($broi == 1){
echo "Това потребителско име е заето.";
}else{
if ($password != $password2) {
echo "Паролите не съвпадат";
}else{
	$password = md5($password);
	if (!strstr("$email", "@") || !strstr("$email", ".")) {
	echo "Невалиден email адрес.";
	}else{
	$sql = mysqli_query($connect, "INSERT INTO users (username, password, email, date, name, avatar, icq, skype, pol, signature) VALUES ('$username', '$password', '$email', '$date', '$name', '$avatar', '$icq', '$skype', '$pol', '$signature')");
	echo "
	<meta http-equiv='Content-Type' content='text/html; charset=windows-1251'>
	Успещна регистрация!
	<meta http-equiv='refresh' content='1; URL=index.php'>
	";
	}
}
}
}
}