<?
include "config.php";
function shortText($text, $lenght){
$text = explode(" ",$text);
$newText = "";
$i = 0;
for ($i = 0;$i < count($text);$i++){
if (strlen($newText) > $lenght ){
$newText .= " ...";
break;
}
$newText .= " ".$text[$i];
}
return $newText;
} 

$kat = (int)$_GET['kat'];
$page = (int)$_GET['p'];
if ($page == 0 || $page == NULL || $page < 0)
{
	$page = 1;
}
$pp = 10;
$start = ($page*$pp) - $pp;
$query = mysqli_query($connect, "SELECT * FROM `lessons`");
$less = mysqli_num_rows($query);
$tot = ceil($less / $pp);

if($kat == NULL){
$result = mysql_query("SELECT * FROM `lessons` ORDER BY `id` DESC LIMIT $start,$pp") or die (mysql_error());
}else{
$result = mysql_query("SELECT * FROM `lessons` WHERE kategoria='$kat' ORDER BY `id` DESC ") or die (mysql_error());
}
$broi = mysql_num_rows($result);
if ($broi == NULL) {
echo "
<br><div class='post'>
<h2 class='title'>Грешка</h2>
<div class='text' style='text-align:center'><br>
<img src='images/warning.png' alt='warning' width='250'><br>
Няма добавени статии към тази категория.<br>
</div>
</div>";
}else{
while($data = mysql_fetch_assoc($result)) {
$sql = "SELECT kategoria FROM cats WHERE id='$data[kategoria]'";
$res = mysql_query($sql) or die (mysql_error());
$row = mysql_fetch_assoc($res);
echo "
<br><div class='post' >
<h2 class='title'>$data[title]</h2>
<p class='posted'>Добавил <a href='?page=profile&amp;user=$data[avtor]'>$data[avtor]</a>, категория $row[kategoria]</p>
<div class='text'>";
echo shortText($data['text'], 800);
echo "<br><a href='?page=lessons_more&amp;id=$data[id]'><img src='images/more.png' alt='more'> Пълен текст</a> 
</div>
</div>
";
}


if (!$kat){
echo "<div class='post' style='text-align:center;'>";
$prev = $page - 1;
$next = $page + 1;
if ($page == 1){
echo "Предишна ";
}else{
echo "<span class='page'><a href='?page=lessons&amp;p=$prev' style='text-decoration: none;color: #000;'>Предишна</a></span> ";
}
if ($page >= $tot)
{
echo " Следваща";
}else{
echo " <span class='page'><a href='?page=lessons&amp;p=$next' style='text-decoration: none;color: #000;'>Следваща</a></span>";
}
print "
<br>
Страница $page от $tot
<br></div>";
}
}
?>