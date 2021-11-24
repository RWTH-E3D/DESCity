"""
DESCity: District Energy Simulation of CityGML Building models
Contact:
M.Sc. Avichal Malhotra: malhotra@e3d.rwth-aachen.de

www.e3d.rwth-aachen.de
Mathieustr. 30
52074 Aachen
"""

# import of libraries
import os
import sys
import PySide2
from PySide2 import QtWidgets, QtGui
import gui_funct as gf
import webbrowser

# setting environment variable for PySide2
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path



# positions and dimensions of window
posx = 200
posy = 50
width = 700
height = 950
sizefactor = 0
sizer = True

pypath = os.path.dirname(os.path.realpath(__file__))        # path of script

"""Label Descriptions"""
DESCity = 'The District Energy Simulation of CityGML Building Models (DESCity)'
CityATB = 'The CityGML Analysis Toolbox (CityATB) can be used for the analysis, validate and to search building(s) and city quarters using user defined coordinates and attributes.'
CityBIT = 'The CityGML Building Interpolation Tool (CityBIT) can be used to interpolate building geometries for unavailable building models based on estmations and approximations.'
CityLDT = 'The CityGML Levels of Detail Transformation'
CityGTV = 'The CityGML Geometrical Transformation and Validation Tool (CityGTV) can be used to transform and validate building geometries.'
CityEnrich = ''
TeaserPlus = ''

global parent_path
path_parent = os.path.dirname(os.getcwd())

class mainWindow(QtWidgets.QWidget):
    def __init__(self):
        #initiate the parent
        super(mainWindow,self).__init__()

        self.initUI()


    def initUI(self):
        global posx, posy, width, height, sizefactor, sizer

        # setup of gui / layout
        if sizer:
            posx, posy, width, height, sizefactor = gf.screenSizer(self,posx, posy, width, height, app)
            sizer = False
        gf.windowSetup(self, posx, posy, width, height, pypath, 'The District Energy Simulation of CityGML Building Models (DESCity)')

        # Setting main layout
        self.vbox = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.vbox)

        self.Font_b = QtGui.QFont()
        self.Font_b.setBold(True)

        self.Font_i = QtGui.QFont()
        self.Font_i.setItalic(True)

        # Loading banner
        gf.load_banner(self, os.path.join(pypath, r'pictures\e3dHeader.png'), sizefactor)
        # self.lbl_descity = QtWidgets.QLabel(DESCity)
        # self.vbox.addWidget(self.lbl_descity)
        """
        Data availability and processing
        """
        self.tGrid = QtWidgets.QVBoxLayout()

        self.box_data = QtWidgets.QGroupBox('Data availability and pre-processing')
        self.tGrid.addWidget(self.box_data)

        self.grid_data = QtWidgets.QGridLayout()
        self.box_data.setLayout(self.grid_data)

        """CityATB"""
        self.box_atb = QtWidgets.QGroupBox('CityATB')
        self.grid_data.addWidget(self.box_atb)

        self.vboxgrid_atb = QtWidgets.QGridLayout()
        self.box_atb.setLayout(self.vboxgrid_atb)

        self.lbl_atb = QtWidgets.QLabel(CityATB)
        self.lbl_atb.setWordWrap(True)
        self.vboxgrid_atb.addWidget(self.lbl_atb, 0, 0, 1, 2)

        self.btn_atb_tool = QtWidgets.QPushButton('CityATB')
        self.vboxgrid_atb.addWidget(self.btn_atb_tool, 0, 2, 1, 1)

        """CityBIT"""
        self.box_bit = QtWidgets.QGroupBox('CityBIT')
        self.grid_data.addWidget(self.box_bit)

        self.vboxgrid_bit = QtWidgets.QGridLayout()
        self.box_bit.setLayout(self.vboxgrid_bit)

        self.lbl_bit = QtWidgets.QLabel(CityBIT)
        self.lbl_bit.setWordWrap(True)
        self.vboxgrid_bit.addWidget(self.lbl_bit, 0, 0, 1, 2)

        self.btn_bit_tool = QtWidgets.QPushButton('CityBIT')
        self.vboxgrid_bit.addWidget(self.btn_bit_tool, 0, 2, 1, 1)

        """CityLDT"""
        self.box_ldt = QtWidgets.QGroupBox('CityLDT')
        self.grid_data.addWidget(self.box_ldt)

        self.vboxgrid_ldt = QtWidgets.QGridLayout()
        self.box_ldt.setLayout(self.vboxgrid_ldt)

        self.lbl_ldt = QtWidgets.QLabel(CityBIT)
        self.lbl_ldt.setWordWrap(True)
        self.vboxgrid_ldt.addWidget(self.lbl_ldt, 0, 0, 1, 2)

        self.btn_ldt_tool = QtWidgets.QPushButton('CityLDT')
        self.vboxgrid_ldt.addWidget(self.btn_ldt_tool, 0, 2, 1, 1)

        self.vbox.addLayout(self.tGrid)

        """
        Enrichment
        """
        self.mGrid = QtWidgets.QVBoxLayout()

        self.box_enrichment = QtWidgets.QGroupBox('Enrichment')
        self.mGrid.addWidget(self.box_enrichment)

        self.grid_enrich = QtWidgets.QGridLayout()
        self.box_enrichment.setLayout(self.grid_enrich)

        """CityGTV"""
        self.box_gtv = QtWidgets.QGroupBox('CityGTV')
        self.grid_enrich.addWidget(self.box_gtv)

        self.vboxgrid_gtv = QtWidgets.QGridLayout()
        self.box_gtv.setLayout(self.vboxgrid_gtv)

        self.lbl_gtv = QtWidgets.QLabel(CityBIT)
        self.lbl_gtv.setWordWrap(True)
        self.vboxgrid_gtv.addWidget(self.lbl_gtv, 0, 0, 1, 2)

        self.btn_gtv_tool = QtWidgets.QPushButton('CityGTV')
        self.vboxgrid_gtv.addWidget(self.btn_gtv_tool, 0, 2, 1, 1)

        """CityEnrich"""
        self.box_enrich = QtWidgets.QGroupBox('CityEnrich')
        self.grid_enrich.addWidget(self.box_enrich)

        self.vboxgrid_enrich = QtWidgets.QGridLayout()
        self.box_enrich.setLayout(self.vboxgrid_enrich)

        self.lbl_enrich = QtWidgets.QLabel(CityBIT)
        self.lbl_enrich.setWordWrap(True)
        self.vboxgrid_enrich.addWidget(self.lbl_enrich, 0, 0, 1, 2)

        self.btn_enrich_tool = QtWidgets.QPushButton('CityEnrich')
        self.vboxgrid_enrich.addWidget(self.btn_enrich_tool, 0, 2, 1, 1)

        self.vbox.addLayout(self.mGrid)

        """
        Simulation
        """
        self.m1Grid = QtWidgets.QVBoxLayout()

        self.box_simulate = QtWidgets.QGroupBox('Simulation')
        self.m1Grid.addWidget(self.box_simulate)

        self.grid_simulate = QtWidgets.QGridLayout()
        self.box_simulate.setLayout(self.grid_simulate)

        """TEASER+"""
        self.box_tplus = QtWidgets.QGroupBox('TEASER+')
        self.grid_simulate.addWidget(self.box_tplus)

        self.vboxgrid_tplus = QtWidgets.QGridLayout()
        self.box_tplus.setLayout(self.vboxgrid_tplus)

        self.lbl_tplus = QtWidgets.QLabel(CityBIT)
        self.lbl_tplus.setWordWrap(True)
        self.vboxgrid_tplus.addWidget(self.lbl_tplus, 0, 0, 1, 2)

        self.btn_tplus_tool = QtWidgets.QPushButton('TEASER+')
        self.vboxgrid_tplus.addWidget(self.btn_tplus_tool, 0, 2, 1, 1)

        self.vbox.addLayout(self.m1Grid)


        """Lower grid with About, HomePage and Exit"""
        self.grid_lower = QtWidgets.QGridLayout()


        self.btn_about = QtWidgets.QPushButton('About')
        self.grid_lower.addWidget(self.btn_about, 0, 0, 1, 1)

        self.btn_homepage = QtWidgets.QPushButton('E3D Homepage')
        self.grid_lower.addWidget(self.btn_homepage, 0, 1, 1, 1)

        self.btn_exit = QtWidgets.QPushButton('Exit')
        self.grid_lower.addWidget(self.btn_exit, 0, 3, 1, 1)

        self.vbox.addLayout(self.grid_lower)

        self.btn_atb_tool.clicked.connect(self.func_CityATB)
        self.btn_ldt_tool.clicked.connect(self.func_CityLDT)
        self.btn_bit_tool.clicked.connect(self.func_CityBIT)
        self.btn_gtv_tool.clicked.connect(self.func_CityGTV)
        self.btn_enrich_tool.clicked.connect(self.func_CityEnrich)
        self.btn_tplus_tool.clicked.connect(self.func_TEASERPlus)
        self.btn_homepage.clicked.connect(self.func_E3D)
        self.btn_exit.clicked.connect(self.func_exit)

        sys.path.append('../')

    def func_CityATB(self):
        self.close()
        self.target_CityATB= './CityATB/'
        os.chdir(self.target_CityATB)
        os.system('python ./main.py')
        # os.chdir(self.path_parent)

    def func_CityLDT(self):
        self.close()
        self.target_CityLDT= './CityLDT/'
        os.chdir(self.target_CityLDT)
        os.system('python ./main.py')
        # os.chdir(self.path_parent)

    def func_CityBIT(self):
        self.close()
        target_CityBIT= './CityBIT/'
        os.chdir(target_CityBIT)
        # self.hide()
        os.system('python ./main.py')
        # os.chdir(self.path_parent)


    def func_CityGTV(self):
        self.close()
        self.target_CityGTV= './CityGTV/'
        os.chdir(self.target_CityGTV)
        os.system('python ./CityGTVmain.py')
        # os.chdir(self.path_parent)

    def func_CityEnrich(self):
        self.close()
        self.target_CityEnrich= './CityEnrich/'
        os.chdir(self.target_CityEnrich)
        os.system('python ./enrich_main.py')
        # os.chdir(self.path_parent)

    def func_TEASERPlus(self):
        self.close()
        self.target_TEASERPlus= './TEASERPlus/'
        os.chdir(self.target_TEASERPlus)
        os.system('python ./main.py')

    def func_E3D(self):
        webbrowser.open('https://www.e3d.rwth-aachen.de/')

    def func_exit(self):
        gf.close_application(self)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    app.setStyleSheet("QLabel{font-size: 8pt;} QPushButton{font-size: pt;} QRadioButton{font-size: 10pt;} QGroupBox{font-size: 10pt;} QComboBox{font-size: 10pt;} QLineEdit{font-size: 10pt;}")
    widget = mainWindow()
    widget.show()
    sys.exit(app.exec_())