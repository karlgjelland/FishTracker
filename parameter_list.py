from PyQt5 import QtCore, QtGui, QtWidgets
from image_manipulation import ImageProcessor
import iconsLauncher as uiIcons

class ParameterList(QtWidgets.QToolBar):
    def __init__(self, playback_manager, sonar_processor, sonar_viewer, fish_manager, detector, tracker):
        super().__init__()
        self.playback_manager = playback_manager
        self.sonar_viewer = sonar_viewer
        self.sonar_processor = sonar_processor
        self.fish_manager = fish_manager
        self.detector = detector
        self.tracker = tracker

        self.setOrientation(QtCore.Qt.Vertical)

        btn_size = QtCore.QSize(30,30)

        #self.image_controls_label = QtWidgets.QLabel(self)
        #self.image_controls_label.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        #self.image_controls_label.setText("Image options")

        #self.verticalLayout = QtWidgets.QVBoxLayout()
        #self.verticalLayout.setObjectName("verticalLayout")
        #self.verticalLayout.setSpacing(5)
        #self.verticalLayout.setContentsMargins(7,7,7,7)

        #self.distance_tick = QtWidgets.QCheckBox("Distance compensation")
        #self.distance_tick.setChecked(False)
        #self.distance_tick.stateChanged.connect(self.playback_manager.setDistanceCompensation)
        #self.distance_tick.stateChanged.connect(self.playback_manager.refreshFrame)

        #self.contrast_tick = QtWidgets.QCheckBox("Automatic contrast")
        #self.contrast_tick.setChecked(False)
        #self.contrast_tick.stateChanged.connect(self.sonar_processor.setAutomaticContrast)
        #self.contrast_tick.stateChanged.connect(self.playback_manager.refreshFrame)

        #self.gamma_layout = QtWidgets.QVBoxLayout()
        #self.gamma_layout.setObjectName("gammaLayout")
        #self.gamma_layout.setSpacing(5)
        #self.gamma_layout.setContentsMargins(0,0,0,0)

        #self.gamma_label = QtWidgets.QLabel("Gamma", self)
        #self.gamma_label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        #self.gamma_label.setMinimumWidth(50)

        self.show_echogram_detections_btn = QtWidgets.QPushButton()
        self.show_echogram_detections_btn.setObjectName("showEchogramDetections")
        self.show_echogram_detections_btn.setFlat(True)
        self.show_echogram_detections_btn.setCheckable(True)
        self.show_echogram_detections_btn.setChecked(False)
        self.show_echogram_detections_btn.clicked.connect(self.showEchogramDetectionsChanged)
        self.show_echogram_detections_btn.setToolTip("Show detections\nOverlay the results from detector to Echogram")
        self.show_echogram_detections_btn.setIcon(QtGui.QIcon(uiIcons.FGetIcon("detections")))
        self.show_echogram_detections_btn.setIconSize(btn_size)

        self.show_echogram_tracks_btn = QtWidgets.QPushButton()
        self.show_echogram_tracks_btn.setObjectName("showTracks")
        self.show_echogram_tracks_btn.setFlat(True)
        self.show_echogram_tracks_btn.setCheckable(True)
        self.show_echogram_tracks_btn.setChecked(True)
        self.show_echogram_tracks_btn.clicked.connect(self.showEchogramTracksChanged)
        self.show_echogram_tracks_btn.setToolTip("Show tracks\nOverlay the results from tracker to Echogram")
        self.show_echogram_tracks_btn.setIcon(QtGui.QIcon(uiIcons.FGetIcon("tracks")))
        self.show_echogram_tracks_btn.setIconSize(btn_size)


        self.gamma_value = QtWidgets.QLabel("1.0", self)
        self.gamma_value.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop)
        self.gamma_value.setMinimumWidth(30)
        self.gamma_value.setToolTip("Gamma")

        self.gamma_slider = QtWidgets.QSlider(QtCore.Qt.Vertical)
        self.gamma_slider.setMinimum(10)
        self.gamma_slider.setMaximum(40)
        self.gamma_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.gamma_slider.setTickInterval(1)
        self.gamma_slider.setValue(20)
        self.gamma_slider.valueChanged.connect(self.gammaSliderChanged)
        self.gamma_slider.valueChanged.connect(self.playback_manager.refreshFrame)
        self.gamma_slider.setMinimumHeight(100)
        self.gamma_slider.setToolTip("Gamma\nGamma value for Sonar View")

        #self.gamma_layout.addWidget(self.gamma_value)
        #self.gamma_layout.addWidget(self.gamma_slider)

        #self.bgsub_tick = QtWidgets.QCheckBox("BG Subtraction")
        #self.bgsub_tick.setChecked(False)
        #self.bgsub_tick.stateChanged.connect(self.detector.setShowBGSubtraction)
        #self.bgsub_tick.stateChanged.connect(self.playback_manager.refreshFrame)

        self.bgsub_btn = QtWidgets.QPushButton(self)
        self.bgsub_btn.setObjectName("subtractBackground")
        self.bgsub_btn.setFlat(True)
        self.bgsub_btn.setCheckable(True)
        self.bgsub_btn.setIcon(QtGui.QIcon(uiIcons.FGetIcon("background_subtraction")))
        self.bgsub_btn.setIconSize(btn_size)
        self.bgsub_btn.clicked.connect(self.detector.setShowBGSubtraction)
        self.bgsub_btn.clicked.connect(self.playback_manager.refreshFrame)
        self.bgsub_btn.setToolTip("Background subtraction\nShow background subtraction used in detector")
  
        self.measure_btn = QtWidgets.QPushButton(self)
        self.measure_btn.setObjectName("measureDistance")
        self.measure_btn.setFlat(True)
        self.measure_btn.setCheckable(True)
        self.measure_btn.setIcon(QtGui.QIcon(uiIcons.FGetIcon("measure")))
        self.measure_btn.setIconSize(btn_size)
        if self.sonar_viewer is not None:
            self.measure_btn.clicked.connect(self.sonar_viewer.measureDistance)
            self.sonar_viewer.MyFigureWidget.measure_toggle.append(self.toggleMeasureBtn)
        self.measure_btn.setToolTip("Measure distance\nDraw a line in Sonar View to measure a distance between two points")

        #self.colormap_tick = QtWidgets.QCheckBox("Use colormap")
        #self.colormap_tick.setChecked(True)
        #self.colormap_tick.stateChanged.connect(self.sonar_processor.setColorMap)
        #self.colormap_tick.stateChanged.connect(self.playback_manager.refreshFrame)
        #self.colormap_tick.setToolTip("Color map\nColor Sonar View with a blue colormap")

        self.colormap_btn = QtWidgets.QPushButton(self)
        self.colormap_btn.setObjectName("setColormap")
        self.colormap_btn.setFlat(True)
        self.colormap_btn.setCheckable(True)
        self.colormap_btn.setChecked(True)
        self.colormap_btn.setIcon(QtGui.QIcon(uiIcons.FGetIcon("colormap")))
        self.colormap_btn.setIconSize(btn_size)
        self.colormap_btn.clicked.connect(self.sonar_processor.setColorMap)
        self.colormap_btn.clicked.connect(self.playback_manager.refreshFrame)
        self.colormap_btn.setToolTip("Color map\nColor Sonar View with a blue colormap")

        self.show_detections_btn = QtWidgets.QPushButton()
        self.show_detections_btn.setObjectName("showDetections")
        self.show_detections_btn.setFlat(True)
        self.show_detections_btn.setCheckable(True)
        self.show_detections_btn.setChecked(False)
        self.show_detections_btn.clicked.connect(self.showDetectionsChanged)
        self.show_detections_btn.setToolTip("Show detections\nOverlay the results from detector to Sonar View")
        self.show_detections_btn.setIcon(QtGui.QIcon(uiIcons.FGetIcon("detections")))
        self.show_detections_btn.setIconSize(btn_size)
        #self.show_detections_checkbox.setEnabled(False)
        #self.detector.state_changed_event.append(lambda: self.show_detections_checkbox.setEnabled(self.detector.mog_ready))

        self.show_detection_size_btn = QtWidgets.QPushButton()
        self.show_detection_size_btn.setObjectName("showDetectionSize")
        self.show_detection_size_btn.setFlat(True)
        self.show_detection_size_btn.setCheckable(True)
        self.show_detection_size_btn.setChecked(True)
        self.show_detection_size_btn.clicked.connect(self.tracker.setShowTrackingSize)
        self.show_detection_size_btn.clicked.connect(self.playback_manager.refreshFrame)
        #self.show_detection_size_btn.setEnabled(False)
        self.show_detection_size_btn.setToolTip("Show detection size\nShow also the length of the detection")
        self.show_detection_size_btn.setIcon(QtGui.QIcon(uiIcons.FGetIcon("det_size")))
        self.show_detection_size_btn.setIconSize(btn_size)

        #self.show_tracks_checkbox = QtWidgets.QCheckBox("Show tracks")
        #self.show_tracks_checkbox.setChecked(False)
        #self.show_tracks_checkbox.stateChanged.connect(self.showTracksChanged)
        #self.show_tracks_checkbox.setToolTip("Show tracks\nOverlay the results from tracker to Sonar View")

        self.show_tracks_btn = QtWidgets.QPushButton()
        self.show_tracks_btn.setObjectName("showTracks")
        self.show_tracks_btn.setFlat(True)
        self.show_tracks_btn.setCheckable(True)
        self.show_tracks_btn.setChecked(True)
        self.show_tracks_btn.clicked.connect(self.showTracksChanged)
        self.show_tracks_btn.setToolTip("Show tracks\nOverlay the results from tracker to Sonar View")
        self.show_tracks_btn.setIcon(QtGui.QIcon(uiIcons.FGetIcon("tracks")))
        self.show_tracks_btn.setIconSize(btn_size)

        #self.show_tracks_checkbox.setEnabled(False)
        #self.tracker.state_changed_event.append(lambda: self.show_tracks_checkbox.setEnabled(self.detector.mog_ready))

        #self.show_trackingIDs_checkbox = QtWidgets.QCheckBox("Show tracking IDs")
        #self.show_trackingIDs_checkbox.setChecked(True)
        #self.show_trackingIDs_checkbox.stateChanged.connect(self.tracker.setShowTrackingIDs)
        #self.show_trackingIDs_checkbox.stateChanged.connect(self.playback_manager.refreshFrame)
        #self.show_trackingIDs_checkbox.setEnabled(False)
        #self.show_trackingIDs_checkbox.setToolTip("Show track IDs\nShow also the IDs of the tracked fish")

        self.show_trackingIDs_btn = QtWidgets.QPushButton()
        self.show_trackingIDs_btn.setObjectName("showTrackID")
        self.show_trackingIDs_btn.setFlat(True)
        self.show_trackingIDs_btn.setCheckable(True)
        self.show_trackingIDs_btn.setChecked(True)
        self.show_trackingIDs_btn.clicked.connect(self.tracker.setShowTrackingIDs)
        self.show_trackingIDs_btn.clicked.connect(self.playback_manager.refreshFrame)
        #self.show_trackingIDs_btn.setEnabled(False)
        self.show_trackingIDs_btn.setToolTip("Show track IDs\nShow also the IDs of the tracked fish")
        self.show_trackingIDs_btn.setIcon(QtGui.QIcon(uiIcons.FGetIcon("track_id")))
        self.show_trackingIDs_btn.setIconSize(btn_size)

        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine);
        line.setFrameShadow(QtWidgets.QFrame.Sunken)

        #self.verticalLayout.addWidget(self.image_controls_label)
        #self.verticalLayout.addWidget(self.distance_tick)
        #self.verticalLayout.addWidget(self.contrast_tick)
        #self.verticalLayout.addWidget(self.gamma_label)
        self.addWidget(self.show_echogram_detections_btn)
        self.addWidget(self.show_echogram_tracks_btn)
        self.addWidget(self.gamma_value)
        self.addWidget(self.gamma_slider)
        self.addWidget(self.bgsub_btn)
        self.addWidget(self.colormap_btn)
        self.addWidget(self.show_detections_btn)
        self.addWidget(self.show_tracks_btn)
        self.addWidget(self.show_detection_size_btn)
        self.addWidget(self.show_trackingIDs_btn)
        self.addWidget(line)
        self.addWidget(self.measure_btn)

    def gammaSliderChanged(self, value):
        applied_value = float(value)/20
        self.sonar_processor.setGamma(applied_value)
        self.gamma_value.setText(str(applied_value))

    def showDetectionsChanged(self, value):
        self.detector.setShowDetections(value)
        self.playback_manager.refreshFrame()

    def showTracksChanged(self, value):
        self.tracker.setShowBoundingBox(value)
        self.fish_manager.setShowFish(value)
        self.playback_manager.refreshFrame()

    def showEchogramDetectionsChanged(self, value):
        self.detector.setShowEchogramDetections(value)
        self.playback_manager.refreshFrame()

    def showEchogramTracksChanged(self, value):
        self.fish_manager.setShowEchogramFish(value)
        self.playback_manager.refreshFrame()

    def toggleMeasureBtn(self, value):
        if self.measure_btn.isChecked() == value:
                self.measure_btn.toggle()

if __name__ == "__main__":
    import sys
    from playback_manager import PlaybackManager
    from fish_manager import FishManager
    from detector import Detector
    from tracker import Tracker

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    playback_manager = PlaybackManager(app, main_window)
    #playback_manager.openTestFile()
    fish_manager = FishManager(None)
    #fish_manager.testPopulate(100)
    #info_w = InfoWidget(playback_manager, fish_manager)
    sonar_processor = ImageProcessor()
    detector = Detector(playback_manager)
    tracker = Tracker(detector)

    parameter_list = ParameterList(playback_manager, sonar_processor, None, fish_manager, detector, tracker)
    main_window.setCentralWidget(parameter_list)
    main_window.show()
    sys.exit(app.exec_())