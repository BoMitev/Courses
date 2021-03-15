<?php 
include "config.php"; 
$vapros = $_GET['vapros']; 
$edit = $_GET['edit']; 
if ($edit) { // ako sme izbrali redaktirane na test 
if ($_POST['submit']) { 
$ime = $_POST['ime']; 
$opisanie = $_POST['opisanie'];	
$sql = "UPDATE tests SET ime = '$ime', opisanie = '$opisanie' WHERE id = '$edit'"; 
$res = mysql_query($sql) or die (mysql_error()); 
echo "Теста е редактиран успешно"; 
echo "<br><input type='button' onclick='javascript: history.go(-2);' name='back' value='Назад'>"; 
} 
else { 
$sql = "SELECT * FROM tests WHERE id = '$edit'"; 
$res = mysql_query($sql); 
$row = mysql_fetch_array($res); 
echo "<form name='edittest' method='POST'> 
Заглавие: <input type='text' name='ime' value='$row[ime]'><br> 
Въведете описание към теста:<br> 
<textarea name='opisanie' cols='40' rows='5' class='form_elements_text'>$row[opisanie]</textarea><br> 
<input type='submit' name='submit' value='Редактирай'></form> 
"; 
} 
} 
?>