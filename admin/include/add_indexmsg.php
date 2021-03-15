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
$id = (int)$_GET['id'];
if ($id) {
$sql = "SELECT * FROM indexmsg WHERE id='$id'";
$result = mysqli_query($connect, $sql);
$row = mysqli_fetch_assoc($result);
	if ($_POST['submit']) {
	$title = htmlspecialchars($_POST['title']);
	$date = date('d/m/Y');
	$text = $_POST['text'];
	$avtor = $_SESSION['username'];
	$zaqvka = "UPDATE indexmsg SET title='$title', text='$text', date='$date', avtor='$avtor' WHERE id='$id'";
	mysqli_query($connect, $zaqvka);
	echo "
	<div class='post'>
	<h2 class='title'>Админ панел</h2>
	<p class='posted'>Логнат като $username.</p>
	<div class='text'>
	<p>Съобщението е редактирано. <a href='index.php'>Назад</a></p>
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
	<form method='post' action='?page=addindexmsg&amp;id=$id'>
	<table width='80%'>
	<tr><td>Заглавие:</td><td><input type='text' name='title' value='$row[title]'></td></tr>
	<tr><td>Съобщение:</td><td><textarea name='text' id='elm4' cols='80' rows='20'>$row[text]</textarea></td></tr> 
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
<p><a href='javascript:history.go(-1);' title='Назад'><img src='images/back.png' alt='back'></a></p>
<table style='width:600px;border-bottom:1px dotted black;'>";
$query = "SELECT * FROM indexmsg";
$res = mysqli_query($connect, $query);
while($data = mysqli_fetch_assoc($res)) {
	echo "
	<tr><td>$data[title]</td><td style='text-align:right'>
	[ <a href='?page=addindexmsg&amp;id=$data[id]'><img src='images/edit.png' alt='edit' width='12'></a> ]
	</td></tr>";
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