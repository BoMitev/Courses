<?
	if(!$_SESSION['username']) {
?>
<div class='post' style='width:860px;'>
<h2 class='title'>Регистрирай се</h2>
<div class='text'>
<form method="post" action="?page=access">
	<fieldset>
	<legend>Тези полета са задължителни!</legend>
	<table class="register">
	<tr><td>Потребител: <span style="color:red;font-weight:bold">*</span></td><td><input type="text" name="username"></td></tr>
	<tr><td>Парола: <span style="color:red;font-weight:bold">*</span></td><td><input type="password" name="password"></td></tr>
	<tr><td>Повтори: <span style="color:red;font-weight:bold">*</span></td><td><input type="password" name="password2"></td></tr>
	<tr><td>E-mail: <span style="color:red;font-weight:bold">*</span></td><td><input type="text" name="email"></td></tr>
	</table>
	</fieldset>
	<fieldset>
	<legend>Тези полета НЕ са задължителни!</legend>
	<table class="register">
	<tr><td>Име:</td><td style="font-size:10px;"><input type="text" name="name"><br>Вашето име.</td></tr>
	<tr><td>Аватар:</td><td style="font-size:10px;"><input type="text" name="avatar"><br>URL адрес до картинката.</td></tr>
	<tr><td>ICQ:</td><td style="font-size:10px;"><input type="text" name="icq"><br>ICQ номер.</td></tr>
	<tr><td>Skype:</td><td style="font-size:10px;"><input type="text" name="skype"><br>Скайп името ви.</td></tr>
	<tr><td>Пол:</td><td style="font-size:10px;">
	<select name="pol">
	<option value="">-- Избери --</option>
	<option value="мъж">Мъж</option>
	<option value="жена">Жена</option>
	</select><br>Вашият пол.
	</td></tr>
	<tr><td>Подпис:</td><td style="font-size:10px;"><textarea name='text' cols='40' rows='10' style="background:#fff;border:1px solid #afafaf;"></textarea><br>Забранени са всякакъв вид HTML, CSS и BB кодове.</td></tr>
	<tr><td><input type="submit" name="submit" value="Регистрирай се" style="background:#fff;border:1px dashed #000;color:red;font-weight:bold"></td></tr>
	</table>
	</fieldset>
</form>
</div>
</div>
<?
}else{
	echo "
	<div style='width:860px;'>
	<div class='post'>
		<h2 class='title'>Грешка!</h2>
		<div class='text' style='text-align:center'>
			<br>
			<img src='images/warning.jpg' alt='warning' width='250'><br>
			Вече сте регистриран<br>
		</div>
	</div>
	</div>
	";
}
?>