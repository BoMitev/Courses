<?
session_start();
include "config.php";
$username = $_SESSION['username'];
$zaqvka = "SELECT * FROM users ORDER BY id";
$res = mysqli_query($connect, $zaqvka);
$usernum = mysqli_num_rows($res);
echo "
<div class='post'>
	<h2 class='title'>Потребители</h2>
		<div class='text' style='text-align:left;padding-left:15px;'>
		<p>Имаме общо <b>$usernum</b> регистрирани потребителя.</p>
<table style='width:98%;text-align:center;'>
<tr>
<td style='border:1px solid #afafaf;font-weight:bold'>Потребител</td>
<td style='border:1px solid #afafaf;font-weight:bold'>E-mail</td>
<td style='border:1px solid #afafaf;font-weight:bold'>Регистриран на</td>
<td style='border:1px solid #afafaf;font-weight:bold'>Права</td>
</tr>";
while ($row = mysqli_fetch_assoc($res)) {
	if ($row['admin'] == 1){
		$row['admin'] = "<span style='font-weight:bold;color:red;'>Администратор</span>";
	}else{
		$row['admin'] = "Потребител";
	}
	echo "
	<tr>
	<td style='text-align:left;border:1px solid #afafaf;text-transform:capitalize'><a href='index.php?page=profile&amp;user=$row[username]'>$row[username]</a></td>
	<td style='border:1px solid #afafaf;'>$row[email]</td>
	<td style='border:1px solid #afafaf;'>$row[date]</td>
	<td style='border:1px solid #afafaf;'>$row[admin]</td>
	</tr>";
}
echo "</table></div><div class='foot'></div></div>";
?>