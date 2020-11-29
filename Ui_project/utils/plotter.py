from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PySide2.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout
from PySide2.QtCore import QTimer, QThread
import numpy as np
from concurrent.futures import ThreadPoolExecutor

MAXIMUM_POINTS = 50
UPDATE_INTERVAL = 250 #in milliseconds

class Plotter(FigureCanvasQTAgg):
    def __init__(self, xtitle=None, ytitle=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.axes.autoscale(enable=True)
        super().__init__(fig)
        self._createDialog()

        self._needsUpdating = False

        self.updateTimer = QTimer()
        self.updateTimer.setSingleShot(False)
        self.updateTimer.setInterval(UPDATE_INTERVAL)
        self.updateTimer.timeout.connect(self._updateFigure)
        self.updateThread = QThread()
        self.updateThread.started.connect(self._refreshFigure)

        self.xdata = list(range(MAXIMUM_POINTS))
        self.ydata = [0] * MAXIMUM_POINTS

        #The following lines may not be correct
        self.xtitle = xtitle
        self.ytitle = ytitle
        self.xtitle("SAMPLE X")

        # self._plot_ref = None
        self._showDialog()
        self.updateTimer.start()

    def _updateFigure(self):
        if self._needsUpdating:
            self.updateThread.start()

    def _refreshFigure(self):
        # if self._plot_ref is None:
        #     self._plot_ref, = self.axes.plot(self.xdata, self.ydata, 'r', marker='o', markersize=12)
        # else:
        #     self._plot_ref.set_xdata(self.xdata)
        #     self._plot_ref.set_ydata(self.ydata)
        self.axes.cla()
        self.axes.plot(self.xdata, self.ydata, 'r', marker='o', markersize=12)

        if self.xtitle is not None:
            self.axes.xtitle(self.xtitle)

        if self.ytitle is not None:
            self.axes.ytitle(self.ytitle)

        self.draw()
        self._needsUpdating = False

    def _createDialog(self):
        self.plotDialog = QDialog()
        self.plotDialog.setWindowTitle("Processing Plot")
        dialogButtons = QDialogButtonBox(QDialogButtonBox.Close)
        dialogButtons.clicked.connect(self._closeDialog)
        layout = QVBoxLayout()
        self.toolbar = NavigationToolbar(self, self.plotDialog)
        layout.addWidget(self.toolbar)
        layout.addWidget(self)
        layout.addWidget(dialogButtons)
        self.plotDialog.setLayout(layout)


    def _closeDialog(self):
        self.plotDialog.close()

    def _showDialog(self):
        self.plotDialog.show()

    def addNewData(self, x, y):
        #Check data validity
        x = np.array(x).flatten()
        y = np.array(y).flatten()
        if x.size != y.size:
            print("Problem with adding new values to the plot, x and y should have the same length")
            return
        #TODO: Add other validation conditions

        #Add data to class
        length = x.shape[0]
        self.xdata = self.xdata[-(MAXIMUM_POINTS-length):] + x.tolist()
        self.ydata = self.ydata[-(MAXIMUM_POINTS-length):] + y.tolist()

        #flag it for updates
        self._needsUpdating = True

    def __del__(self):
        self.plotDialog.close()
        while not self.updateThread.isFinished():
            pass



