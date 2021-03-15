<?php 
include "config.php"; 
if (!$_POST['submit']) { 
echo "Въведете заглавие на теста:<br>"; 
echo "<form name='test' method='POST' action=''> 
<input type='text' name='ime' size='52'><br> 
Въведете описание към теста:<br> 
<textarea name='opisanie' cols='40' rows='5' class='form_elements_text'></textarea><br>
<input type='submit' name='submit' value='Добавяне'> 
</form> 
можете да добавите въпроси към тях от <a href='addvapros.php'>ТУК</a>"; 
} 
else { 
$ime = $_POST['ime']; 
$ime = trim(strip_tags(addslashes($ime))); //slagame malko za6tita 
$opisanie = $_POST['opisanie']; 
$opisanie = trim(strip_tags(addslashes($opisanie))); // tuk sa6to 
$query = "INSERT INTO tests (ime, opisanie) VALUES ('$ime', '$opisanie')"; 
$res = mysql_query($query) or die (mysql_error()); //dobavqme testa 
if ($res) { echo "Теста е добавен успешно. Можете да добавите въпроси към него от <a href='addvapros.php'>тук</a>"; } 
} 
?>