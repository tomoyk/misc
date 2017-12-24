# 実験6回目(通信の基礎)のメモ

## pを連打しなくて良い方法

ファイル`imagelib`にある`void createFrame()`の内部を以下に変更する。

	w[fcnt].setImage(p, s);
	
	// added
	if(originalMode){
	  print("PSNR for " + w[fcnt].getTitle());
	  getPSNR(original, w[fcnt].pimage);
	}
	
	fcnt++;

また、`imagelib`の先頭に`boolean originalMode = true;`を追加しておくことで不要な場合には`false`に設定することにより、この機能を無効化することが出来る。

## コインの面積をコインに表示する

ファイル`imagelib`の内部に以下の関数を追加する。

	// added
	PImage printSize(PImage photo) {
	
	  PImage img = photo.get();
	  image(img, 0.0, 0.0);
	
	  for (int i = 0; i < min(maxRegions, labelRegions.length); i++) {
	    Region rr = (Region)labelRegions[i];
	    // println(String.format("%6d  %7.1f %7.1f", rr.npix, rr.centx, rr.centy));
	
	    // display
	    textSize(16);
	    int txt_x = int(rr.centx);
	    int txt_y = int(rr.centy);
	    String txt = String.format("%6d", rr.npix);
	    // println("debug::"+txt+" "+txt_x+" "+txt_y);
	    fill(255, 0, 0);
	    text(txt, txt_x-20, txt_y);
	  }
	
	  return img;
	}

さらに、ファイル`drawInfo()`内の`void drawInfo()`にある以下のコードをコメントアウトする。

	if (original != null) image(original, border, border);

加えて`ex6`内の`void doex7()`内にあるコードを以下に変更する。

	void doex7(){
	  // ...
	  PImage p2 = labeling(p1, 100);
	
	  // added
	  printSize(original);
	
	  printLabel();
	  // ...
	}

