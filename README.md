# Delphi_Python_OpenCV

![](image.png)

---

## 概要
- Delphi Community Edition<br>
	* 引用:<br>
		[フリーランスの開発者、スタートアップ企業、学生、趣味のプログラマーは、**無料** のDelphi Community Editionで、開発スキルを共有しよう。](https://www.embarcadero.com/jp/products/delphi/starter)
		

- Delphi に GetIt から [Delphi4Python_Expoter](https://github.com/Embarcadero/Delphi4PythonExporter) という Package をインストール
	- 今のところ英語環境でないとインストールできない
	[https://twitter.com/ht_deko/status/1533268729722978304](https://twitter.com/ht_deko/status/1533268729722978304)

- Delphi で GUI を設計
- Python_Expoter を使い Python コードに変換
- Python の開発環境は任意<br>
	僕の好みは Jupyter-notebook<br>
	ということで、最終的には **/notebook/Delphi_Python_OpenCV.ipynb** です
- Embarcadero から出ている [delphifmx の仕様は x86 or x64](https://github.com/Embarcadero/DelphiFMX4Python) だけなので、**Raspberry pi** でやれない。**やりたい！**


## 仕様
- GUI で設計、元画像＋処理済み画像を並べる
- OpenCV の画像処理
	- Opitical Flow
	- [ORB (Oriented FAST and Rotated Brief)](https://ichi.pro/orb-no-gaiyo-oriented-fast-and-rotated-brief-72709114183887)

- Device 選択
	- 動画ファイル .. OpenDialog 使って読み込めるようにした
	- USB Web Camera

---

## 課題
- Delphi, Python のコンポーネントの仕様が明らかでないので、相互変換はメモリ渡しができなくて、ファイル渡しにした
- OpenCV の画像処理例が僅かで、今のところ 2つである<br>
	※[引用元](https://github.com/JimmyHHua/opencv_tutorials)は100個をはるかに越えるサンプルがある

