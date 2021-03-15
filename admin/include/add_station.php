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
if ($_POST['submit']) {
$title = htmlspecialchars($_POST['title']);
$text = $_POST['text'];
$avtor = $_SESSION['username'];
$kategoria = $_POST['kategoria'];
$sql = "INSERT INTO lessons (title, kategoria, text, avtor) VALUES ('$title', '$kategoria', '$text', '$avtor')";
mysqli_query($connect, $sql);
echo "
<div class='post'>
<h2 class='title'>Админ панел</h2>
<p class='posted'>Логнат като <? echo $username ?>.</p>
<div class='text'>
<p>Статията е добавена. <a href='index.php'>Начало</a></p>
</div>
</div>
";
}
else {
?>
<div class='post'>
<h2 class='title'>Админ панел</h2>
<p class='posted'>Логнат като <? echo $username ?>.</p>
<div class='text'>
<p><a href='javascript:history.go(-1);' title='Назад'><img src='images/back.png' alt='back'></a></p>
<form method="post" action="?page=addstation">
<table width="80%">
<tr><td>
Заглавие:</td><td><input type="text" name="title"></td></tr>
<?
$query = "SELECT * FROM cats";
$result = mysqli_query($connect, $query);
echo "<tr><td>Категория:</td><td><select name='kategoria'>";
while($row = mysqli_fetch_assoc($result)) {
echo "<option value='$row[id]'>$row[kategoria]</option>";
}
echo "</select></td></tr>";
?>
<tr><td>Статия:</td><td><textarea id="elm4" name="text" rows="20" cols="80"></textarea></td></tr> 
<tr><td></td><td><input type="submit" name="submit" value="Добави статия" style="background:#fff;border:1px dashed #000;color:red;font-weight:bold"></td></tr></table>
</form>
</div>
</div>
<?
} 
}else{
	echo "<h2>Нямаш достъп до тази страница.</h2>";
} 
?>