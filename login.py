import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class login(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Login")
     
        # Definindo o ícone da janela (caminho relativo ou absoluto).
        # self.set_default_icon_from_file('../../_static/favicon.png')
        
        
       
        self.set_default_size(700 / 2, 400 / 2)  # dimensao da tela
        self.set_position(Gtk.WindowPosition.CENTER) # posição de inicializacao da tela
        self.set_border_width(10) # definindo uma borda

        #interface
        grid = Gtk.Grid.new()
        grid.set_row_spacing(10)
        self.add(grid)

        #entry login
        self.login_txt = Gtk.Entry.new()
        self.login_txt.set_placeholder_text('Login')

        #entry senha
        self.senha_txt = Gtk.Entry.new()
        self.senha_txt.set_placeholder_text('Senha')

        #botao entrar
        self.entrar_btn = Gtk.Button.new_with_label('Entrar')
     #   self.entrar_btn.connect('clicked', self.login)
        self.set_focus(self.entrar_btn)

        #botao cadastrar
        self.cadastrar_btn = Gtk.Button.new_with_label('Cadastrar')
     #   self.cadastrar_btn.connect('clicked', self.login)
        self.set_focus(self.cadastrar_btn)

        #adicionar widget na tela
        grid.add(self.login_txt)
        grid.attach_next_to(self.senha_txt, self.login_txt, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(self.entrar_btn, self.senha_txt, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(self.cadastrar_btn, self.entrar_btn, Gtk.PositionType.BOTTOM, 1, 2)


        # sqlite

    def login(self, widget):
        #confere o login e senha no bd, caso ok vai para tela 3
'''
        
        # Escondendo a janela.
        # self.set_visible(False)
        self.hide()

        # Exibindo a outra janela e passando pra ela LoginWin(Gtk.Window).
        # Isso porque vamos precisar exibir essa janela de novo.
        Index(parent=self).show_all()
'''   
    def cadastro(self, widget):
        # vai para a tela 2


win = login()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
