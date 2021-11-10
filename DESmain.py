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

# setting environment variable for PySide2
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


# positions and dimensions of window
posx = 275
posy = 100
width = 650
height = 700
sizefactor = 0
sizer = True

pypath = os.path.dirname(os.path.realpath(__file__))        # path of script


class mainWindow(QtWidgets.QWidget):
    def __init__(self):
        #initiate the parent
        super(mainWindow,self).__init__()
        self.initUI()


    def initUI(self):
        global posx, posy, width, height, sizefactor, sizer

        # setup of gui / layout
        if sizer:
            posx, posy, width, height, sizefactor = gf.screenSizer(self, posx, posy, width, height, app)
            sizer = False
        gf.windowSetup(self, posx, posy, width, height, pypath, 'DESCity')

        # Setting main layout
        self.vbox = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.vbox)

        # Loading banner
        gf.load_banner(self, os.path.join(pypath, r'pictures\e3dHeader.png'), sizefactor)


        # Data availability and processing
        self.tGrid = QtWidgets.QVBoxLayout()

        self.box_data = QtWidgets.QGroupBox('Data availability and pre-processing')
        self.tGrid.addWidget(self.box_data)

        self.grid_data = QtWidgets.QGridLayout()
        self.box_data.setLayout(self.grid_data)

        self.box_atb = QtWidgets.QGroupBox('CityATB')
        self.grid_data.addWidget(self.box_atb)


        self.box_bit = QtWidgets.QGroupBox('CityBIT')
        self.grid_data.addWidget(self.box_bit)


        self.box_ldt = QtWidgets.QGroupBox('CityLDT')
        self.grid_data.addWidget(self.box_ldt)

        self.vbox.addLayout(self.tGrid)

        # Data availability and processing
        self.mGrid = QtWidgets.QVBoxLayout()

        self.box_enrichment = QtWidgets.QGroupBox('Enrichment')
        self.mGrid.addWidget(self.box_enrichment)

        self.grid_enrich = QtWidgets.QGridLayout()
        self.box_enrichment.setLayout(self.grid_enrich)

        self.box_gtv = QtWidgets.QGroupBox('CityGTV')
        self.grid_enrich.addWidget(self.box_gtv)

        self.box_enrich = QtWidgets.QGroupBox('CityEnrich')
        self.grid_enrich.addWidget(self.box_enrich)

        self.vbox.addLayout(self.mGrid)

        # Data availability and processing
        self.m1Grid = QtWidgets.QVBoxLayout()

        self.box_simulate = QtWidgets.QGroupBox('Simulation')
        self.m1Grid.addWidget(self.box_simulate)

        self.grid_simulate = QtWidgets.QGridLayout()
        self.box_simulate.setLayout(self.grid_simulate)

        self.box_tplus = QtWidgets.QGroupBox('TEASER+')
        self.grid_simulate.addWidget(self.box_tplus)

        self.vbox.addLayout(self.m1Grid)

        self.grid_lower = QtWidgets.QGridLayout()
        self.vbox.addLayout(self.grid_lower)

        self.btn_about = QtWidgets.QPushButton('About')
        self.grid_lower.addWidget(self.btn_about, 0, 0, 1, 1)

        self.btn_homepage = QtWidgets.QPushButton('e3D Homepage')
        self.grid_lower.addWidget(self.btn_homepage, 0, 1, 1, 1)

        self.btn_homepage = QtWidgets.QPushButton('Exit')
        self.grid_lower.addWidget(self.btn_homepage, 0, 2, 1, 1)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    widget = mainWindow()
    widget.show()
    sys.exit(app.exec_())