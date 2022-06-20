unit main;

interface

uses
  System.SysUtils, System.Types, System.UITypes, System.Classes, System.Variants,
  FMX.Types, FMX.Controls, FMX.Forms, FMX.Graphics, FMX.Dialogs, FMX.Objects,
  FMX.Menus, FMX.StdCtrls, FMX.Effects;

type
  TMainForm = class(TForm)
    StyleBook1: TStyleBook;
    ImageRaw: TImage;
    ImageArranged: TImage;
    Timer1: TTimer;
    MainMenu1: TMainMenu;
    MenuItem1: TMenuItem;
    MenuExit: TMenuItem;
    Splitter1: TSplitter;
    Menu_Seperator: TMenuItem;
    MenuItem2: TMenuItem;
    MenuIMovie: TMenuItem;
    MenuUsbWeb: TMenuItem;
    MenuItem3: TMenuItem;
    MenuOpen: TMenuItem;
    OpenDialog1: TOpenDialog;
    MenuOpticalFlow: TMenuItem;
    MenuORB: TMenuItem;
    TextRaw: TText;
    ShadowEffect1: TShadowEffect;
    TextArranged: TText;
    ShadowEffect2: TShadowEffect;
    procedure Timer1Timer(Sender: TObject);
    procedure FormClose(Sender: TObject; var Action: TCloseAction);
    procedure MenuExitClick(Sender: TObject);
    procedure Menu_SelectorClick(Sender: TObject);
    procedure MenuOpenClick(Sender: TObject);

  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  MainForm: TMainForm;

implementation

{$R *.fmx}



procedure TMainForm.FormClose(Sender: TObject; var Action: TCloseAction);
begin
//
end;

procedure TMainForm.MenuExitClick(Sender: TObject);
begin
    close;
end;



procedure TMainForm.MenuOpenClick(Sender: TObject);
begin
    OpenDialog1.Execute;
end;

procedure TMainForm.Menu_SelectorClick(Sender: TObject);
begin
    (Sender as TMenuItem).IsChecked := True;
end;

procedure TMainForm.Timer1Timer(Sender: TObject);
begin
//
end;

end.
