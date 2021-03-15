<?
session_start();
include "config.php";
$username = $_SESSION['username'];
$user = $_GET['user'];
if (!$user) { 
echo "
		<div class='post'>
			<h2 class='title'>Грешка</h2>
					<div class='text'>
					<p>Няма такъв потребител</p>
					</div>
		</div>
";
}else{
$zaqvka = "SELECT * FROM users WHERE username = '$user'";
$res = mysqli_query($connect, $zaqvka);
$row = mysqli_fetch_assoc($res);
$query = mysqli_query($connect, "SELECT * FROM lessons WHERE avtor='$user'");
$stations = mysqli_num_rows($query);
if	($row['name'] == NULL)
	{
		$row['name'] = "Няма зададено";
	}
if ($row['avatar'] == NULL)
	{
		$row['avatar'] = "images/noavatar.gif";
	}
if ($row['icq'] == NULL)
	{
		$row['icq'] = "Няма зададено";
	}
if ($row['skype'] == NULL)
	{
		$row['skype'] = "Няма зададено";
	}
if ($row['pol'] == NULL)
	{
		$row['pol'] = "Няма зададено";
	}
if($row['signature'] == NULL)
	{
		$row['signature'] = "Няма зададено";
	}
if ($row['admin'] == 1){
	$row['admin'] = "Администратор";
}else{
	$row['admin'] = "Потребител";
}
echo "<div class='post'>
			<h2 class='title'>Профил на $row[username] </h2>
					<div class='text'>
					<br>
					<table width='100%'>
					  <tr>
						<td rowspan='10' style='width:25%;text-align:center'><img src='$row[avatar]' alt='avatar' width='120' height='120'></td>
						<td style='width:75%'><b>Потребител:</b> $row[username]</td>
					  </tr>
					  <tr>
						<td><b>Имейл:</b> $row[email]</td>
					  </tr>
					  <tr>
						<td><b>Регистриран на:</b> $row[date]</td>
					  </tr>
					  <tr>
						<td><b>Име:</b> $row[name]</td>
					  </tr>
					  <tr>
						<td><b>ICQ:</b> $row[icq]</td>
					  </tr>
					  <tr>
						<td><b>Skype:</b> $row[skype]</td>
					  </tr>
					  <tr>
						<td><b>Пол:</b> $row[pol]</td>
					  </tr>
					  <tr>
						<td><b>Права:</b> $row[admin]</td>
					  </tr>
					  <tr>
						<td><b>Добавени Статии:</b> $stations</td>
					  </tr>
					  <tr>
						<td><b>Подпис:</b> $row[signature]</td>
					  </tr>
					</table><p>";
					if ($row['username'] == $username) {
						echo "[<a href='?page=profile_edit'>Редактирай профила си!</a>]";
					}
					echo"</p>
					</div>
		</div>
";

}
?>