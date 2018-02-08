<?php

class Pencil {

  // Field (Property)
  public $color = "black";
  public $hardness = "HB";
  protected $protect = "this is protected";
  private $secret = "this is private";
  
  function __construct() {
    echo "called Pencil()\n";
  }

  function getColor() {
    echo $this->hardness."\n";
    echo $this->protect."\n";
    echo $this->secret."\n";
  }

}

class Note {

  public $size = "A4";

  function __construct() {
    echo "called Note()\n";
  }

  public function getSize(){
    echo $this->size."\n";
  }

}

class CampusNote extends Note {

  protected $line = "A";
  public $size = "B5";

}

echo "=== debug ===\n";

// Dynamicな呼び出し
$pen = new Pencil();
$pen->color = "yellow";
$pen->getColor();

// Staticな呼び出し
// Pencil::getColor();
// インスタンスを作成しないと$thisが使えないのでエラーになる

echo "test: ".$pen->hardness."\n";
// echo "test: ".$pen->protect."\n";
// echo "test: ".$pen->secret."\n";

$note = new Note();
$note->getSize();
// Note::getSize();

$cnote = new CampusNote();
$cnote->getSize();
// $cnote->line;
