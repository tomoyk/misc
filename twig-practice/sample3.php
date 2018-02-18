<?php

require_once 'vendor/autoload.php';

$loader = new Twig_Loader_Filesystem('templates');
$twig = new Twig_Environment($loader, [
  'debug' => true, 
  'auto_reload' => true, 
  'strict_variables' => true
]);

if(isset($_GET['a'])){

  echo $twig->render('_base.html', array('title' => 'Top'));

}else{

  echo $twig->render('_mini.html', array('title' => 'Mini'));

}
  
