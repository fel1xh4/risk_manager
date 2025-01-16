from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout,
                             QTabWidget, QMessageBox, QAction)
from .add_tab import AddTab
from .view_tab import ViewTab
from .summary_tab import SummaryTab
from .config_tab import ConfigTab
from .risk_matrix_tab import RiskMatrixTab
from ..core.uncertainty_manager import UncertaintyManager
from ..data.config_handler import ConfigHandler
from ..data.data_handler import DataHandler

class UncertaintyTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Uncertainty Tracking Tool")
        self.setGeometry(100, 100, 800, 600)

        self.data_handler = DataHandler("uncertainties.csv")
        self.config_handler = ConfigHandler("workstreams.xlsx")
        self.WORKSTREAMS = self.config_handler.load_workstreams()
        self.uncertainty_manager = UncertaintyManager(self.data_handler)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.tabs = QTabWidget()
        self.layout.addWidget(self.tabs)

        self.add_tab = AddTab(self.uncertainty_manager, self.WORKSTREAMS)
        self.view_tab = ViewTab(self.uncertainty_manager)
        self.summary_tab = SummaryTab(self.uncertainty_manager)
        self.config_tab = ConfigTab(self.config_handler)
        self.risk_matrix_tab = RiskMatrixTab(self.uncertainty_manager, self.WORKSTREAMS)

        self.tabs.addTab(self.add_tab, "Add Uncertainty")
        self.tabs.addTab(self.view_tab, "View Uncertainties")
        self.tabs.addTab(self.summary_tab, "Summary")
        self.tabs.addTab(self.config_tab, "Configuration")
        self.tabs.addTab(self.risk_matrix_tab, "Risk Matrix")

        self._setup_menu_bar()
        self._initialize_tabs()

    def _initialize_tabs(self):
        self.risk_matrix_tab._update_risk_matrix_tab()
        self.view_tab._update_view_tab()
        self.summary_tab._update_summary_tab()
        # Keine Initialisierung für AddTab notwendig

    def _setup_menu_bar(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        save_action = QAction("Save", self)
        save_action.triggered.connect(self._save_data)
        file_menu.addAction(save_action)
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        actions_menu = menu_bar.addMenu("Actions")
        add_action = QAction("Add Uncertainty", self)
        add_action.triggered.connect(lambda: self.tabs.setCurrentIndex(0))
        actions_menu.addAction(add_action)
        view_action = QAction("View Uncertainties", self)
        view_action.triggered.connect(self._update_view_tab)
        actions_menu.addAction(view_action)
        summary_action = QAction("Summarize Uncertainties", self)
        summary_action.triggered.connect(self._update_summary_tab)
        actions_menu.addAction(summary_action)
        config_action = QAction("Configuration", self)
        config_action.triggered.connect(lambda: self.tabs.setCurrentIndex(3))
        actions_menu.addAction(config_action)
        risk_matrix_action = QAction("Risk Matrix", self)
        risk_matrix_action.triggered.connect(lambda: self.tabs.setCurrentIndex(4))
        actions_menu.addAction(risk_matrix_action)

    def _save_data(self):
        if self.uncertainty_manager.save_data():
            QMessageBox.information(self, "Success", f"Data saved to {self.uncertainty_manager.data_file}")
        else:
            QMessageBox.critical(self, "Error", "Error saving data.")

    def _update_view_tab(self):
        self.view_tab._update_view_tab()

    def _update_summary_tab(self):
        self.summary_tab._update_summary_tab()