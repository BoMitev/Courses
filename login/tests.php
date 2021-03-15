<?php 
session_start();
$username = $_SESSION['username'];
if (isset($username)) {
$id = $_GET['id']; 
if ($id) {
	$sql = "SELECT * FROM questions WHERE testid = '$id' ORDER BY id ASC"; 
	$res = mysqli_query($connect, $sql) or die(mysqli_error()); 
if (!$_POST['proveri']) { 
	$sql = "SELECT * FROM tests WHERE id = '$id'"; 
	$raw = mysqli_query($connect, $sql) or die(mysqli_error()); 
	$data = mysqli_fetch_array($raw);
	echo "
	<br><div class='post'>
	<h2 class='title'>$data[ime]</h2>
	<div class='text' style='text-align:left'><br>
	<form name='test' method='POST'>"; 
	$vapros = 1; 
	while ($row = mysqli_fetch_array($res)) { 
	echo "$vapros. $row[vapros]"; 
	echo "<br><input name='$row[id]' type='radio' value='a'>".$row['a']; 
	echo "<br><input name='$row[id]' type='radio' value='b'>".$row['b']; 
	echo "<br><input name='$row[id]' type='radio' value='c'>".$row['c']."<br><br>"; 
	$vapros++; 
	} 
	echo "<br><input type='button' onclick='javascript: history.back(-1);' name='back' value='Назад'> 
	<input type='submit' name='proveri' value='Провери'> <input type='reset' name='reset' value='Наново'><br>"; 
	echo "</form></div></div>"; 
} else { 
	$veren = 0; 
	$gre6en = 0; 
	$i = 0; 
		echo "
		<br><div class='post'>
		<h2 class='title'>Провери</h2>
		<div class='text' style='text-align:left'><br>
		";
		while($row = mysqli_fetch_array($res)) { 
		$id = $row[id]; 
		$otg = $_POST[$id]; 
		$verniq = $row['otg']; 
		if ($row['otg'] == $otg) { 
		$i++; 
		$veren++; 
		echo "<span class='true'>Върпос $i: Вярно!</span><br>"; 
		} else { 
		$i++; 
		echo "<span class='false'>Върпос $i: Грешно!<br>"; 
		$gre6en++; 
		} } 
	echo "<br>Верни отговори: ".$veren; 
	echo "<br>Грешни отговори: ".$gre6en;
	$all = $veren + $gre6en; 
	$koef = $veren/$all; 
	$koef = $koef*100; 
	$koef = round($koef); 
	echo "<br>Вашият резултат е $koef%"; 
	$ocenka = 2+$veren/$all;
	$ocenka = round($ocenka, 2);
	echo "<br>Оценка: $ocenka</div></div>";
} 
} else { 
$sql = "SELECT * FROM tests"; 
$res = mysqli_query($connect, $sql) or die(mysqli_error()); 
$broitestove = mysqli_num_rows($res);
if ($broitestove == NULL){
 echo "
 	<div class='post'>
	<h2 class='title'>Няма добавени тестове</h2>
	<div class='text' style='text-align:center'><br>
	<img src='images/warning.png' alt='warning' width='250'><br>
	Няма добавени тестове.
	</div></div>
 ";
}else{

	while($row = mysqli_fetch_array($res)) { 
	echo "
	<div class='post'>
	<h2 class='title'>Тестове</h2>
	<div class='text' style='text-align:left'><br>
	<a href='index.php?page=tests&id=$row[id]' style='font-size:13px;'>$row[ime]</a><br> 
	<span style='font-size:10px;'>$row[opisanie]</span>
	</div></div>"; 
	} 
}
} 
}else{
echo"<div class='post'>
<h2 class='title'>Регистрирай се</h2>
<div class='text' style='text-align:center'><br>
<img src='images/warning.png' alt='warning' width='250'><br>
Само регистрирани потребители имат достъп до тази страница.<br>
</div>
</div>";
} 
?>