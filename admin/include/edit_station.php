<? 
session_start();
$username = $_SESSION['username'];
$query = "SELECT * FROM users WHERE username='$username'";
$res = mysqli_query($connect, $query);
$data = mysqli_fetch_assoc($res);
if ($data['admin'] == 1) {
?>
<script type="text/javascript" src="../lessons/tiny_mce/tiny_mce.js"></script>
<script type="text/javascript">
// O2k7 skin (silver)
	tinyMCE.init({
		// General options
		mode : "exact",
		elements : "elm4",
		theme : "advanced",
		skin : "o2k7",
		skin_variant : "silver",
		plugins : "pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template,inlinepopups,autosave",

		// Theme options
		theme_advanced_buttons1 : "bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,formatselect,fontselect,fontsizeselectcut,copy,paste,pastetext,pasteword",
		theme_advanced_buttons2 : "bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,image,code,|,insertdate,inserttime,preview,|,forecolor,backcolor",
		theme_advanced_buttons3 : "tablecontrols,hr,removeformat,visualaid,|,sub,sup,|,search,replacecharmap,|,iespell,media,|,print,|,ltr,rtl,|,fullscreen,|,insertlayer,moveforward,movebackward,absolute",
		theme_advanced_buttons4 : "",
		theme_advanced_toolbar_location : "top",
		theme_advanced_toolbar_align : "left",
		theme_advanced_statusbar_location : "bottom",
		theme_advanced_resizing : true,

		// Example content CSS (should be your site CSS)
		content_css : "css/content.css",

		// Drop lists for link/image/media/template dialogs
		template_external_list_url : "lists/template_list.js",
		external_link_list_url : "lists/link_list.js",
		external_image_list_url : "lists/image_list.js",
		media_external_list_url : "lists/media_list.js",

		// Replace values for the template plugin
		template_replace_values : {
			username : "Some User",
			staffid : "991234"
		}
	});
</script>
<?
$id = $_GET['id'];
if ($id) {
$sql = "SELECT * FROM lessons WHERE id='$id'";
$result = mysqli_query($connect, $sql);
$row = mysqli_fetch_assoc($result);
	if ($_POST['submit']) {
	$title = htmlspecialchars($_POST['title']);
	$opisanie = htmlspecialchars($_POST['opisanie']);
	$text = $_POST['text'];
	$avtor = $_SESSION['username'];
	$kategoria = $_POST['kategoria'];
	$zaqvka = "UPDATE lessons SET title='$title', kategoria='$kategoria', text='$text', avtor='$avtor' WHERE id='$id'";
	mysqli_query($connect, $zaqvka);
	echo "
	<div class='post'>
	<h2 class='title'>Админ панел</h2>
	<p class='posted'>Логнат като $username.</p>
	<div class='text'>
	<p>Статията е редактирана. <a href='index.php?page=editstation'>Назад</a></p>
	</div>
	</div>";
	}
	else {
	echo "
	<div class='post'>
	<h2 class='title'>Админ панел</h2>
	<p class='posted'>Логнат като $username.</p>
	<div class='text'>
	<p><a href='javascript:history.go(-1);' title='Назад'><img src='images/back.png' alt='back'></a></p>
	<form method='post' action='?page=editstation&amp;id=$id'>
	<table width='80%'>
	<tr><td>
	Заглавие:</td><td><input type='text' name='title' value='$row[title]'></td></tr>";
	$query = "SELECT * FROM cats";
	$res = mysqli_query($connect, $query);
	echo "<tr><td>Категория:</td><td><select name='kategoria'>";
	while($kat = mysqli_fetch_assoc($res)) {
	if ($kat['id'] == $row['kategoria'])
	{
	$select = "selected='selected'";
	}else{
	$select = "";
	}
	echo "<option value='$kat[id]' $select>$kat[kategoria]</option>";
	}
	echo "</select></td></tr>";
	echo"<tr><td>Статия:</td><td><textarea name='text' id='elm4' cols='80' rows='20'>$row[text]</textarea></td></tr> 
	<tr><td></td><td><input type='submit' name='submit' value='Редактирай' style='background:#fff;border:1px dashed #000;color:red;font-weight:bold'>
	</td></tr></table>
	</form>
	</div>
	</div>";
}
}
else {
echo "
<div class='post'>
<h2 class='title'>Админ панел</h2>
<p class='posted'>Логнат като $username.</p>
<div class='text'>
<p>
<a href='javascript:history.go(-1);' title='Назад'><img src='images/back.png' alt='back'></a><br>
[ <a href='?page=addstation' title='Добави нова статия'>Добави нова статия</a> ]</p>
<table style='width:600px;'>";

$kategorii = mysqli_query($connect, "SELECT * FROM cats");
while($rows = mysqli_fetch_assoc($kategorii)){
echo "<tr><td colspan='3'>» <b>$rows[kategoria]</b></td></tr>";
$res = mysqli_query($connect, "SELECT * FROM lessons WHERE kategoria='$rows[id]'");
while($data = mysqli_fetch_assoc($res)) {
	echo "
	<tr>
	<td></td>
	<td></td>
	<td style='border-bottom:1px dotted black;'> • $data[title]</td>
	<td style='text-align:right;border-bottom:1px dotted black;'>
	[ <a href='?page=editstation&amp;id=$data[id]'><img src='images/edit.png' alt='edit' width='12'></a> ]
	[ <a href='?page=deletestation&amp;id=$data[id]' OnClick=\"return confirm('Сигурни ли сте, че искате да изтриете този урок?')\"><img src='images/delete.png' alt='delete' width='12'></a> ]</td>
	</tr>";
}

}
echo "
</table>
</div>
</div>";
}
}else{
	echo "<h2>Нямаш достъп до тази страница.</h2>";
} 
?>