<?
include "config.php";
$results = mysqli_query($connect, "SELECT * FROM indexmsg LIMIT 1");
$broi = mysqli_num_rows($results);
$row = mysqli_fetch_assoc($results);
if (empty($row['text'])) {
	echo "
	<div class='post'>
	<h2 class='title'>Добре Дошли</h2>
	<div class='text' style='text-align:center'>
	<p>
	Няма начално съобщение
	</p>
	</div>
	</div>";
}else{
echo "
<div class='post' style='height:auto;'>
<h2 class='title'>$row[title]</h2>
<p class='posted'>Добавил <a href='?page=profile&amp;user=$row[avtor]'>$row[avtor]</a>, добавена на $row[date]</p>
<div class='text'>
$row[text]
</div>
</div>
";
}
?>