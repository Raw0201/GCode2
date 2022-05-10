# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowrBwysb.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDockWidget, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow: object) -> object:
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1292, 1294)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/icons/resources/gear.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"/* ---------------------------------------------------------------------------\n"
"\n"
"    Created by the qtsass compiler v0.1.1\n"
"    \n"
"    https://github.com/sommerc/pyqt-stylesheets\n"
"\n"
"    The definitions are in the \"qdarkstyle.qss._styles.scss\" module\n"
"\n"
"    WARNING! All changes made in this file will be lost!\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"/* QDarkStyleSheet -----------------------------------------------------------\n"
"\n"
"This is the main style sheet, the palette has nine colors.\n"
"\n"
"It is based on three selecting colors, three greyish (background) colors\n"
"plus three whitish (foreground) colors. Each set of widgets of the same\n"
"type have a header like this:\n"
"\n"
"    ------------------\n"
"    GroupName --------\n"
"    ------------------\n"
"\n"
"And each widget is separated with a header like this:\n"
"\n"
"    QWidgetName ------\n"
"\n"
"This makes more easy to find and change some css field. The basic\n"
""
                        "configuration is described bellow.\n"
"\n"
"    BACKGROUND -----------\n"
"\n"
"        Light   (unpressed)\n"
"        Normal  (border, disabled, pressed, checked, toolbars, menus)\n"
"        Dark    (background)\n"
"\n"
"    FOREGROUND -----------\n"
"\n"
"        Light   (texts/labels)\n"
"        Normal  (not used yet)\n"
"        Dark    (disabled texts)\n"
"\n"
"    SELECTION ------------\n"
"\n"
"        Light  (selection/hover/active)\n"
"        Normal (selected)\n"
"        Dark   (selected disabled)\n"
"\n"
"If a stranger configuration is required because of a bugfix or anything\n"
"else, keep the comment on the line above so nobody changes it, including the\n"
"issue number.\n"
"\n"
"*/\n"
"/*\n"
"\n"
"See Qt documentation:\n"
"\n"
"  - https://doc.qt.io/qt-5/stylesheet.html\n"
"  - https://doc.qt.io/qt-5/stylesheet-reference.html\n"
"  - https://doc.qt.io/qt-5/stylesheet-examples.html\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"/* QWidget ----------"
                        "------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QWidget {\n"
"  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"}\n"
"\n"
"QWidget:disabled {\n"
"  background-color: #19232D;\n"
"  color: #787878;\n"
"  selection-background-color: #14506E;\n"
"  selection-color: #787878;\n"
"}\n"
"\n"
"QWidget::item:selected {\n"
"  background-color: #1464A0;\n"
"}\n"
"\n"
"QWidget::item:hover {\n"
"  background-color: #148CD2;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"/* QMainWindow ------------------------------------------------------------\n"
"\n"
"This adjusts the splitter in the dock widget, not qsplitter\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmainwindow\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QMainWindow::separator {\n"
""
                        "  background-color: #32414B;\n"
"  border: 0px solid #19232D;\n"
"  spacing: 0px;\n"
"  padding: 2px;\n"
"}\n"
"\n"
"QMainWindow::separator:hover {\n"
"  background-color: #505F69;\n"
"  border: 0px solid #148CD2;\n"
"}\n"
"\n"
"QMainWindow::separator:horizontal {\n"
"  width: 5px;\n"
"  margin-top: 2px;\n"
"  margin-bottom: 2px;\n"
"  image: url(\":/qss_icons/rc/toolbar_separator_vertical.png\");\n"
"}\n"
"\n"
"QMainWindow::separator:vertical {\n"
"  height: 5px;\n"
"  margin-left: 2px;\n"
"  margin-right: 2px;\n"
"  image: url(\":/qss_icons/rc/toolbar_separator_horizontal.png\");\n"
"}\n"
"\n"
"/* QToolTip ---------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtooltip\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QToolTip {\n"
"  background-color: #ffffff/*#148CD2*/;\n"
"  border: 1px solid #19232D;\n"
"  color: #19232D;\n"
"  /* Remove padding, for fix combo box tooltip */\n"
"  paddi"
                        "ng: 0px;\n"
"  /* Remove opacity, fix #174 - may need to use RGBA */\n"
"}\n"
"\n"
"/* QStatusBar -------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qstatusbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QStatusBar {\n"
"  border: 1px solid #32414B;\n"
"  /* Fixes Spyder #9120, #9121 */\n"
"  background: #32414B;\n"
"  /* Fixes #205, white vertical borders separating items */\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"  border: none;\n"
"}\n"
"\n"
"QStatusBar QToolTip {\n"
"  background-color: #148CD2;\n"
"  border: 1px solid #19232D;\n"
"  color: #19232D;\n"
"  /* Remove padding, for fix combo box tooltip */\n"
"  padding: 0px;\n"
"  /* Reducing transparency to read better */\n"
"  opacity: 230;\n"
"}\n"
"\n"
"QStatusBar QLabel {\n"
"  /* Fixes Spyder #9120, #9121 */\n"
"  background: transparent;\n"
"}\n"
"\n"
"/* QCheckBox --------------------------------------------------------------\n"
""
                        "\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qcheckbox\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QCheckBox {\n"
"  background-color: #19232D;\n"
"  color: #F0F0F0;\n"
"  spacing: 4px;\n"
"  outline: none;\n"
"  padding-top: 4px;\n"
"  padding-bottom: 4px;\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"  border: none;\n"
"}\n"
"\n"
"QCheckBox QWidget:disabled {\n"
"  background-color: #19232D;\n"
"  color: #787878;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  margin-left: 4px;\n"
"  height: 16px;\n"
"  width: 16px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover, QCheckBox::indicator:unchecked:focus, QCheckBox::indicator:unchecked:pressed {\n"
"  border: none;\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked_focus.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled {\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked_disabled"
                        ".png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"  image: url(\":/qss_icons/rc/checkbox_checked.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover, QCheckBox::indicator:checked:focus, QCheckBox::indicator:checked:pressed {\n"
"  border: none;\n"
"  image: url(\":/qss_icons/rc/checkbox_checked_focus.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled {\n"
"  image: url(\":/qss_icons/rc/checkbox_checked_disabled.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate {\n"
"  image: url(\":/qss_icons/rc/checkbox_indeterminate.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:disabled {\n"
"  image: url(\":/qss_icons/rc/checkbox_indeterminate_disabled.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:focus, QCheckBox::indicator:indeterminate:hover, QCheckBox::indicator:indeterminate:pressed {\n"
"  image: url(\":/qss_icons/rc/checkbox_indeterminate_focus.png\");\n"
"}\n"
"\n"
"/* QGroupBox --------------------------------------------------------------\n"
"\n"
"https://do"
                        "c.qt.io/qt-5/stylesheet-examples.html#customizing-qgroupbox\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QGroupBox {\n"
"  font-weight: bold;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  padding: 4px;\n"
"  margin-top: 16px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"  subcontrol-origin: margin;\n"
"  subcontrol-position: top left;\n"
"  left: 3px;\n"
"  padding-left: 3px;\n"
"  padding-right: 5px;\n"
"  padding-top: 8px;\n"
"  padding-bottom: 16px;\n"
"}\n"
"\n"
"QGroupBox::indicator {\n"
"  margin-left: 2px;\n"
"  height: 16px;\n"
"  width: 16px;\n"
"}\n"
"\n"
"QGroupBox::indicator:unchecked {\n"
"  border: none;\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked.png\");\n"
"}\n"
"\n"
"QGroupBox::indicator:unchecked:hover, QGroupBox::indicator:unchecked:focus, QGroupBox::indicator:unchecked:pressed {\n"
"  border: none;\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked_focus.png\");\n"
"}\n"
"\n"
"QGroupBox::indicator:unchecked:disabled {\n"
""
                        "  image: url(\":/qss_icons/rc/checkbox_unchecked_disabled.png\");\n"
"}\n"
"\n"
"QGroupBox::indicator:checked {\n"
"  border: none;\n"
"  image: url(\":/qss_icons/rc/checkbox_checked.png\");\n"
"}\n"
"\n"
"QGroupBox::indicator:checked:hover, QGroupBox::indicator:checked:focus, QGroupBox::indicator:checked:pressed {\n"
"  border: none;\n"
"  image: url(\":/qss_icons/rc/checkbox_checked_focus.png\");\n"
"}\n"
"\n"
"QGroupBox::indicator:checked:disabled {\n"
"  image: url(\":/qss_icons/rc/checkbox_checked_disabled.png\");\n"
"}\n"
"\n"
"/* QRadioButton -----------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qradiobutton\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QRadioButton {\n"
"  background-color: #19232D;\n"
"  color: #F0F0F0;\n"
"  spacing: 4px;\n"
"  padding: 0px;\n"
"  border: none;\n"
"  outline: none;\n"
"}\n"
"\n"
"QRadioButton:focus {\n"
"  border: none;\n"
"}\n"
"\n"
"QRadioButton:"
                        "disabled {\n"
"  background-color: #19232D;\n"
"  color: #787878;\n"
"  border: none;\n"
"  outline: none;\n"
"}\n"
"\n"
"QRadioButton QWidget {\n"
"  background-color: #19232D;\n"
"  color: #F0F0F0;\n"
"  spacing: 0px;\n"
"  padding: 0px;\n"
"  outline: none;\n"
"  border: none;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"  border: none;\n"
"  outline: none;\n"
"  margin-left: 4px;\n"
"  height: 16px;\n"
"  width: 16px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"  image: url(\":/qss_icons/rc/radio_unchecked.png\");\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover, QRadioButton::indicator:unchecked:focus, QRadioButton::indicator:unchecked:pressed {\n"
"  border: none;\n"
"  outline: none;\n"
"  image: url(\":/qss_icons/rc/radio_unchecked_focus.png\");\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:disabled {\n"
"  image: url(\":/qss_icons/rc/radio_unchecked_disabled.png\");\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"  border: none;\n"
"  outline: none;\n"
"  image: url(\":/qss_ic"
                        "ons/rc/radio_checked.png\");\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover, QRadioButton::indicator:checked:focus, QRadioButton::indicator:checked:pressed {\n"
"  border: none;\n"
"  outline: none;\n"
"  image: url(\":/qss_icons/rc/radio_checked_focus.png\");\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:disabled {\n"
"  outline: none;\n"
"  image: url(\":/qss_icons/rc/radio_checked_disabled.png\");\n"
"}\n"
"\n"
"/* QMenuBar ---------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmenubar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QMenuBar {\n"
"  background-color: #32414B;\n"
"  padding: 2px;\n"
"  border: 1px solid #19232D;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QMenuBar:focus {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"  background: transparent;\n"
"  padding: 4px;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"  padding: 4px;\n"
"  background: transpa"
                        "rent;\n"
"  border: 0px solid #32414B;\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"  padding: 4px;\n"
"  border: 0px solid #32414B;\n"
"  background-color: #148CD2;\n"
"  color: #F0F0F0;\n"
"  margin-bottom: 0px;\n"
"  padding-bottom: 0px;\n"
"}\n"
"\n"
"/* QMenu ------------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmenu\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QMenu {\n"
"  border: 0px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  margin: 0px;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"  height: 1px;\n"
"  background-color: #505F69;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QMenu::icon {\n"
"  margin: 0px;\n"
"  padding-left: 8px;\n"
"}\n"
"\n"
"QMenu::item {\n"
"  background-color: #32414B;\n"
"  padding: 4px 24px 4px 24px;\n"
"  /* Reserve space for selection border */\n"
"  border: 1px transparent #32414B;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QMenu::"
                        "indicator {\n"
"  width: 12px;\n"
"  height: 12px;\n"
"  padding-left: 6px;\n"
"  /* non-exclusive indicator = check box style indicator (see QActionGroup::setExclusive) */\n"
"  /* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked {\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked:selected {\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked_disabled.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked {\n"
"  image: url(\":/qss_icons/rc/checkbox_checked.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked:selected {\n"
"  image: url(\":/qss_icons/rc/checkbox_checked_disabled.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked {\n"
"  image: url(\":/qss_icons/rc/radio_unchecked.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked:selected {\n"
"  image: url(\":/qss_icons/rc/radio_unchecked_disabled.png\");\n"
"}\n"
""
                        "\n"
"QMenu::indicator:exclusive:checked {\n"
"  image: url(\":/qss_icons/rc/radio_checked.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked:selected {\n"
"  image: url(\":/qss_icons/rc/radio_checked_disabled.png\");\n"
"}\n"
"\n"
"QMenu::right-arrow {\n"
"  margin: 5px;\n"
"  image: url(\":/qss_icons/rc/arrow_right.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"}\n"
"\n"
"/* QAbstractItemView ------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qcombobox\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QAbstractItemView {\n"
"  alternate-background-color: #19232D;\n"
"  color: #F0F0F0;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QAbstractItemView QLineEdit {\n"
"  padding: 2px;\n"
"}\n"
"\n"
"/* QAbstractScrollArea ----------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qabstractscrollarea\n"
""
                        "\n"
"--------------------------------------------------------------------------- */\n"
"QAbstractScrollArea {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  padding: 2px;\n"
"  /* fix #159 */\n"
"  min-height: 1.25em;\n"
"  /* fix #159 */\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QAbstractScrollArea:disabled {\n"
"  color: #787878;\n"
"}\n"
"\n"
"/* QScrollArea ------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QScrollArea QWidget QWidget:disabled {\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"/* QScrollBar -------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qscrollbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QScrollBar:horizontal {\n"
"  height: 16px;\n"
"  margin: 2px 16px 2px 16px;\n"
"  border: 1px solid #32414B;\n"
"  border-radi"
                        "us: 4px;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"  background-color: #19232D;\n"
"  width: 16px;\n"
"  margin: 16px 2px 16px 2px;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: #787878;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  min-width: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"  background-color: #148CD2;\n"
"  border: 1px solid #148CD2;\n"
"  border-radius: 4px;\n"
"  min-width: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:focus {\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: #787878;\n"
"  border: 1px solid #32414B;\n"
"  min-height: 8px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"  background-color: #148CD2;\n"
"  border: 1px solid #148CD2;\n"
"  border-radius: 4px;\n"
"  min-height: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:focus {\n"
"  borde"
                        "r: 1px solid #1464A0;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  margin: 0px 0px 0px 0px;\n"
"  border-image: url(\":/qss_icons/rc/arrow_right_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover, QScrollBar::add-line:horizontal:on {\n"
"  border-image: url(\":/qss_icons/rc/arrow_right.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  margin: 3px 0px 3px 0px;\n"
"  border-image: url(\":/qss_icons/rc/arrow_down_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on {\n"
"  border-image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: bottom;\n"
"  subcontr"
                        "ol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  margin: 0px 3px 0px 3px;\n"
"  border-image: url(\":/qss_icons/rc/arrow_left_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on {\n"
"  border-image: url(\":/qss_icons/rc/arrow_left.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  margin: 3px 0px 3px 0px;\n"
"  border-image: url(\":/qss_icons/rc/arrow_up_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover, QScrollBar::sub-line:vertical:on {\n"
"  border-image: url(\":/qss_icons/rc/arrow_up.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin"
                        ";\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {\n"
"  background: none;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"  background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"  background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"  background: none;\n"
"}\n"
"\n"
"/* QTextEdit --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-specific-widgets\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTextEdit {\n"
"  background-color: #19232D;\n"
"  color: #F0F0F0;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"QTextEdit:hover {\n"
"  border: 1px solid #148CD2;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"QTextEdit:selected {\n"
"  background: "
                        "#1464A0;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"/* QPlainTextEdit ---------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QPlainTextEdit {\n"
"  background-color: #19232D;\n"
"  color: #F0F0F0;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"QPlainTextEdit:hover {\n"
"  border: 1px solid #148CD2;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"QPlainTextEdit:selected {\n"
"  background: #1464A0;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"/* QSizeGrip --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qsizegrip\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QSizeGrip {\n"
"  background: transparent;\n"
"  width: 12px;\n"
"  height: 12px;\n"
"  image: url(\":/qss_icons/rc/window_grip.png\");\n"
"}\n"
"\n"
"/* QStackedWi"
                        "dget ---------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QStackedWidget {\n"
"  padding: 2px;\n"
"  border: 1px solid #32414B;\n"
"  border: 1px solid #19232D;\n"
"}\n"
"\n"
"/* QToolBar ---------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtoolbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QToolBar {\n"
"  background-color: #32414B;\n"
"  border-bottom: 1px solid #19232D;\n"
"  padding: 2px;\n"
"  font-weight: bold;\n"
"  spacing: 2px;\n"
"}\n"
"\n"
"QToolBar QToolButton {\n"
"  background-color: #32414B;\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"QToolBar QToolButton:hover {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QToolBar QToolButton:checked {\n"
"  border: 1px solid #19232D;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QToolBar QToolButton:checked:hover {\n"
"  border"
                        ": 1px solid #148CD2;\n"
"}\n"
"\n"
"QToolBar::handle:horizontal {\n"
"  width: 16px;\n"
"  image: url(\":/qss_icons/rc/toolbar_move_horizontal.png\");\n"
"}\n"
"\n"
"QToolBar::handle:vertical {\n"
"  height: 16px;\n"
"  image: url(\":/qss_icons/rc/toolbar_move_vertical.png\");\n"
"}\n"
"\n"
"QToolBar::separator:horizontal {\n"
"  width: 16px;\n"
"  image: url(\":/qss_icons/rc/toolbar_separator_horizontal.png\");\n"
"}\n"
"\n"
"QToolBar::separator:vertical {\n"
"  height: 16px;\n"
"  image: url(\":/qss_icons/rc/toolbar_separator_vertical.png\");\n"
"}\n"
"\n"
"QToolButton#qt_toolbar_ext_button {\n"
"  background: #32414B;\n"
"  border: 0px;\n"
"  color: #F0F0F0;\n"
"  image: url(\":/qss_icons/rc/arrow_right.png\");\n"
"}\n"
"\n"
"/* QAbstractSpinBox -------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QAbstractSpinBox {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  /* Th"
                        "is fixes 103, 111 */\n"
"  padding-top: 2px;\n"
"  /* This fixes 103, 111 */\n"
"  padding-bottom: 2px;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  border-radius: 4px;\n"
"  /* min-width: 5px; removed to fix 109 */\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button {\n"
"  background-color: transparent #19232D;\n"
"  subcontrol-origin: border;\n"
"  subcontrol-position: top right;\n"
"  border-left: 1px solid #32414B;\n"
"  border-bottom: 1px solid #32414B;\n"
"  border-top-left-radius: 0;\n"
"  border-bottom-left-radius: 0;\n"
"  margin: 1px;\n"
"  width: 12px;\n"
"  margin-bottom: -1px;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow, QAbstractSpinBox::up-arrow:disabled, QAbstractSpinBox::up-arrow:off {\n"
"  image: url(\":/qss_icons/rc/arrow_up_disabled.png\");\n"
"  height: 8px;\n"
"  width: 8px;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow:hover {\n"
"  image: url(\":/qss_icons/rc/arrow_up.png\");\n"
"}\n"
"\n"
"QAbstractSpinBox:down-button {\n"
"  background-color: transparent #19232D;\n"
"  subcontrol-origin"
                        ": border;\n"
"  subcontrol-position: bottom right;\n"
"  border-left: 1px solid #32414B;\n"
"  border-top: 1px solid #32414B;\n"
"  border-top-left-radius: 0;\n"
"  border-bottom-left-radius: 0;\n"
"  margin: 1px;\n"
"  width: 12px;\n"
"  margin-top: -1px;\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow, QAbstractSpinBox::down-arrow:disabled, QAbstractSpinBox::down-arrow:off {\n"
"  image: url(\":/qss_icons/rc/arrow_down_disabled.png\");\n"
"  height: 8px;\n"
"  width: 8px;\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow:hover {\n"
"  image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"}\n"
"\n"
"QAbstractSpinBox:hover {\n"
"  border: 1px solid #148CD2;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QAbstractSpinBox:focus {\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"QAbstractSpinBox:selected {\n"
"  background: #1464A0;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"/* ------------------------------------------------------------------------ */\n"
"/* DISPLAYS --------------------------------------------------------------- */\n"
"/* -"
                        "----------------------------------------------------------------------- */\n"
"/* QLabel -----------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qframe\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QLabel {\n"
"  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 2px;\n"
"  margin: 0px;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  color: #787878;\n"
"}\n"
"\n"
"/* QTextBrowser -----------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qabstractscrollarea\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTextBrowser {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QTextBrowser:disabled {\n"
" "
                        " background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #787878;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QTextBrowser:hover, QTextBrowser:!hover, QTextBrowser:selected, QTextBrowser:pressed {\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"/* QGraphicsView ----------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QGraphicsView {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QGraphicsView:disabled {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #787878;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QGraphicsView:hover, QGraphicsView:!hover, QGraphicsView:selected, QGraphicsView:pressed {\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"/* QCalendarWidget --------------------------------------------------------\n"
"\n"
"---------------------------------------------------------------------------"
                        " */\n"
"QCalendarWidget {\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QCalendarWidget:disabled {\n"
"  background-color: #19232D;\n"
"  color: #787878;\n"
"}\n"
"\n"
"/* QLCDNumber -------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QLCDNumber {\n"
"  background-color: #19232D;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QLCDNumber:disabled {\n"
"  background-color: #19232D;\n"
"  color: #787878;\n"
"}\n"
"\n"
"/* QProgressBar -----------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qprogressbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QProgressBar {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  border-radius: 4px;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QProgressBar:disabled {\n"
"  background-color: #19232D;\n"
"  bo"
                        "rder: 1px solid #32414B;\n"
"  color: #787878;\n"
"  border-radius: 4px;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"  background-color: #1464A0;\n"
"  color: #19232D;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QProgressBar::chunk:disabled {\n"
"  background-color: #14506E;\n"
"  color: #787878;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"/* ------------------------------------------------------------------------ */\n"
"/* BUTTONS ---------------------------------------------------------------- */\n"
"/* ------------------------------------------------------------------------ */\n"
"/* QPushButton ------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qpushbutton\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QPushButton {\n"
"  background-color: #505F69;\n"
"  border: 1px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  border-radius: 4px;\n"
"  padding: 3px;\n"
"  outline: none;"
                        "\n"
"  /* Issue #194 - Special case of QPushButton inside dialogs, for better UI */\n"
"  min-width: 20px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"  background-color: #32414B;\n"
"  border: 1px solid #32414B;\n"
"  color: #787878;\n"
"  border-radius: 4px;\n"
"  padding: 3px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"  background-color: #32414B;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  padding: 3px;\n"
"  outline: none;\n"
"}\n"
"\n"
"QPushButton:checked:disabled {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #787878;\n"
"  border-radius: 4px;\n"
"  padding: 3px;\n"
"  outline: none;\n"
"}\n"
"\n"
"QPushButton:checked:selected {\n"
"  background: #1464A0;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"QPushButton::menu-indicator {\n"
"  subcontrol-origin: padding;\n"
"  subcontrol-position: bottom right;\n"
"  bottom: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #19232D;\n"
"}\n"
"\n"
"QPushButton:pressed:hov"
                        "er {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  border: 1px solid #148CD2;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QPushButton:selected {\n"
"  background: #1464A0;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  border: 1px solid #148CD2;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"/* QToolButton ------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtoolbutton\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QToolButton {\n"
"  background-color: transparent;\n"
"  border: 1px solid transparent;\n"
"  border-radius: 4px;\n"
"  margin: 0px;\n"
"  padding: 2px;\n"
"  /* The subcontrols below are used only in the DelayedPopup mode */\n"
"  /* The subcontrols below are used only in the MenuButtonPopup mode */\n"
"  /* The subcontrol below is used only in the InstantPopup or DelayedPopup mode */"
                        "\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"  background-color: transparent;\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"QToolButton:checked:disabled {\n"
"  border: 1px solid #14506E;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"  margin: 1px;\n"
"  background-color: transparent;\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"  border: none;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"0\"] {\n"
"  /* Only for DelayedPopup */\n"
"  padding-right: 2px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] {\n"
"  /* Only for MenuButtonPopup */\n"
"  padding-right: 20px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"]::menu-button {\n"
"  border: none;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"]::menu-button:hover {\n"
"  border: none;\n"
"  border-left: 1px solid #148CD2;\n"
"  border-radius: 0;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"2\"] {\n"
"  /* Only for InstantPopup */\n"
"  padding-right: 2px;\n"
"}\n"
"\n"
"QToolButton::menu-butto"
                        "n {\n"
"  padding: 2px;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #32414B;\n"
"  width: 12px;\n"
"  outline: none;\n"
"}\n"
"\n"
"QToolButton::menu-button:hover {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QToolButton::menu-button:checked:hover {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QToolButton::menu-indicator {\n"
"  image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"  height: 8px;\n"
"  width: 8px;\n"
"  top: 0;\n"
"  /* Exclude a shift for better image */\n"
"  left: -2px;\n"
"  /* Shift it a bit */\n"
"}\n"
"\n"
"QToolButton::menu-arrow {\n"
"  image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"  height: 8px;\n"
"  width: 8px;\n"
"}\n"
"\n"
"QToolButton::menu-arrow:hover {\n"
"  image: url(\":/qss_icons/rc/arrow_down_focus.png\");\n"
"}\n"
"\n"
"/* QCommandLinkButton -----------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QCommandLinkButton {\n"
"  background-color: transparent;\n"
"  border: 1"
                        "px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  border-radius: 4px;\n"
"  padding: 0px;\n"
"  margin: 0px;\n"
"}\n"
"\n"
"QCommandLinkButton:disabled {\n"
"  background-color: transparent;\n"
"  color: #787878;\n"
"}\n"
"\n"
"/* ------------------------------------------------------------------------ */\n"
"/* INPUTS - NO FIELDS ----------------------------------------------------- */\n"
"/* ------------------------------------------------------------------------ */\n"
"/* QComboBox --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qcombobox\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QComboBox {\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  selection-background-color: #1464A0;\n"
"  padding-left: 4px;\n"
"  padding-right: 36px;\n"
"  /* 4 + 16*2 See scrollbar size */\n"
"  /* Fixes #103, #111 */\n"
"  min-height: 1.5em;\n"
"  /* padding-top: 2px;     removed to fix"
                        " #132 */\n"
"  /* padding-bottom: 2px;  removed to fix #132 */\n"
"  /* min-width: 75px;      removed to fix #109 */\n"
"  /* Needed to remove indicator - fix #132 */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 0;\n"
"  background-color: #19232D;\n"
"  selection-background-color: #1464A0;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView:hover {\n"
"  background-color: #19232D;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView:selected {\n"
"  background: #1464A0;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView:alternate {\n"
"  background: #19232D;\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"  background-color: #19232D;\n"
"  color: #787878;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"QComboBox:on {\n"
"  selection-background-color: #1464A0;\n"
"}\n"
"\n"
"QComboBox::indicator {\n"
"  border: none;\n"
"  border-radius: 0;\n"
"  backg"
                        "round-color: transparent;\n"
"  selection-background-color: transparent;\n"
"  color: transparent;\n"
"  selection-color: transparent;\n"
"  /* Needed to remove indicator - fix #132 */\n"
"}\n"
"\n"
"QComboBox::indicator:alternate {\n"
"  background: #19232D;\n"
"}\n"
"\n"
"QComboBox::item:alternate {\n"
"  background: #19232D;\n"
"}\n"
"\n"
"QComboBox::item:checked {\n"
"  font-weight: bold;\n"
"}\n"
"\n"
"QComboBox::item:selected {\n"
"  border: 0px solid transparent;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"  subcontrol-origin: padding;\n"
"  subcontrol-position: top right;\n"
"  width: 12px;\n"
"  border-left: 1px solid #32414B;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"  image: url(\":/qss_icons/rc/arrow_down_disabled.png\");\n"
"  height: 8px;\n"
"  width: 8px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on, QComboBox::down-arrow:hover, QComboBox::down-arrow:focus {\n"
"  image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"}\n"
"\n"
"/* QSlider ----------------------------------------------------------------\n"
""
                        "\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qslider\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QSlider:disabled {\n"
"  background: #19232D;\n"
"}\n"
"\n"
"QSlider:focus {\n"
"  border: none;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"  background: #32414B;\n"
"  border: 1px solid #32414B;\n"
"  height: 4px;\n"
"  margin: 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"  background: #32414B;\n"
"  border: 1px solid #32414B;\n"
"  width: 4px;\n"
"  margin: 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"  background: #1464A0;\n"
"  border: 1px solid #32414B;\n"
"  width: 4px;\n"
"  margin: 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical :disabled {\n"
"  background: #14506E;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"  background: #1464A0;\n"
"  border: 1px solid #32414B;\n"
"  height: 4px;\n"
"  margin: 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
""
                        "QSlider::sub-page:horizontal:disabled {\n"
"  background: #14506E;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"  background: #787878;\n"
"  border: 1px solid #32414B;\n"
"  width: 8px;\n"
"  height: 8px;\n"
"  margin: -8px 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"  background: #148CD2;\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:focus {\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"  background: #787878;\n"
"  border: 1px solid #32414B;\n"
"  width: 8px;\n"
"  height: 8px;\n"
"  margin: 0 -8px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"  background: #148CD2;\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QSlider::handle:vertical:focus {\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"/* QLineEdit --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qlineedit\n"
"\n"
"-------------------"
                        "-------------------------------------------------------- */\n"
"QLineEdit {\n"
"  background-color: #19232D;\n"
"  padding-top: 2px;\n"
"  /* This QLineEdit fix  103, 111 */\n"
"  padding-bottom: 2px;\n"
"  /* This QLineEdit fix  103, 111 */\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  border-style: solid;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"  background-color: #19232D;\n"
"  color: #787878;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"  border: 1px solid #148CD2;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"QLineEdit:selected {\n"
"  background-color: #1464A0;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"/* QTabWiget --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtabwidget-and-qtabbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTabWidget {\n"
""
                        "  padding: 2px;\n"
"  selection-background-color: #32414B;\n"
"}\n"
"\n"
"QTabWidget QWidget {\n"
"  /* Fixes #189 */\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  margin: 0px;\n"
"  /* Fixes double border inside pane with pyqt5 */\n"
"  padding: 0px;\n"
"}\n"
"\n"
"QTabWidget::pane:selected {\n"
"  background-color: #32414B;\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"/* QTabBar ----------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtabwidget-and-qtabbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTabBar {\n"
"  qproperty-drawBase: 0;\n"
"  border-radius: 4px;\n"
"  margin: 0px;\n"
"  padding: 2px;\n"
"  border: 0;\n"
"  /* left: 5px; move to the right by 5px - removed for fix */\n"
"}\n"
"\n"
"QTabBar::close-button {\n"
"  border: 0;\n"
"  margin: 2px;\n"
"  padding: 2px;\n"
"  image: url(\":/qss_ico"
                        "ns/rc/window_close.png\");\n"
"}\n"
"\n"
"QTabBar::close-button:hover {\n"
"  image: url(\":/qss_icons/rc/window_close_focus.png\");\n"
"}\n"
"\n"
"QTabBar::close-button:pressed {\n"
"  image: url(\":/qss_icons/rc/window_close_pressed.png\");\n"
"}\n"
"\n"
"/* QTabBar::tab - selected ------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtabwidget-and-qtabbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTabBar::tab {\n"
"  /* !selected and disabled ----------------------------------------- */\n"
"  /* selected ------------------------------------------------------- */\n"
"}\n"
"\n"
"QTabBar::tab:top:selected:disabled {\n"
"  border-bottom: 3px solid #14506E;\n"
"  color: #787878;\n"
"  background-color: #32414B;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected:disabled {\n"
"  border-top: 3px solid #14506E;\n"
"  color: #787878;\n"
"  background-color: #32414B;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected:di"
                        "sabled {\n"
"  border-right: 3px solid #14506E;\n"
"  color: #787878;\n"
"  background-color: #32414B;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected:disabled {\n"
"  border-left: 3px solid #14506E;\n"
"  color: #787878;\n"
"  background-color: #32414B;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:disabled {\n"
"  border-bottom: 3px solid #19232D;\n"
"  color: #787878;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:disabled {\n"
"  border-top: 3px solid #19232D;\n"
"  color: #787878;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:disabled {\n"
"  border-right: 3px solid #19232D;\n"
"  color: #787878;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:disabled {\n"
"  border-left: 3px solid #19232D;\n"
"  color: #787878;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected {\n"
"  border-bottom: 2px solid #19232D;\n"
"  margin-top: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected {\n"
"  border-top: 2px solid #"
                        "19232D;\n"
"  margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected {\n"
"  border-left: 2px solid #19232D;\n"
"  margin-right: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected {\n"
"  border-right: 2px solid #19232D;\n"
"  margin-left: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:top {\n"
"  background-color: #32414B;\n"
"  color: #F0F0F0;\n"
"  margin-left: 2px;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  padding-top: 2px;\n"
"  padding-bottom: 2px;\n"
"  min-width: 5px;\n"
"  border-bottom: 3px solid #32414B;\n"
"  border-top-left-radius: 3px;\n"
"  border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"  background-color: #505F69;\n"
"  color: #F0F0F0;\n"
"  border-bottom: 3px solid #1464A0;\n"
"  border-top-left-radius: 3px;\n"
"  border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:hover {\n"
"  border: 1px solid #148CD2;\n"
"  border-bottom: 3px solid #148CD2;\n"
"  /* Fixes spyder-ide/spyder#9766 */\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
""
                        "}\n"
"\n"
"QTabBar::tab:bottom {\n"
"  color: #F0F0F0;\n"
"  border-top: 3px solid #32414B;\n"
"  background-color: #32414B;\n"
"  margin-left: 2px;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  padding-top: 2px;\n"
"  padding-bottom: 2px;\n"
"  border-bottom-left-radius: 3px;\n"
"  border-bottom-right-radius: 3px;\n"
"  min-width: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected {\n"
"  color: #F0F0F0;\n"
"  background-color: #505F69;\n"
"  border-top: 3px solid #1464A0;\n"
"  border-bottom-left-radius: 3px;\n"
"  border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:hover {\n"
"  border: 1px solid #148CD2;\n"
"  border-top: 3px solid #148CD2;\n"
"  /* Fixes spyder-ide/spyder#9766 */\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:left {\n"
"  color: #F0F0F0;\n"
"  background-color: #32414B;\n"
"  margin-top: 2px;\n"
"  padding-left: 2px;\n"
"  padding-right: 2px;\n"
"  padding-top: 4px;\n"
"  padding-bottom: 4px;\n"
"  border-top-left-radius: "
                        "3px;\n"
"  border-bottom-left-radius: 3px;\n"
"  min-height: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"  color: #F0F0F0;\n"
"  background-color: #505F69;\n"
"  border-right: 3px solid #1464A0;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:hover {\n"
"  border: 1px solid #148CD2;\n"
"  border-right: 3px solid #148CD2;\n"
"  padding: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:right {\n"
"  color: #F0F0F0;\n"
"  background-color: #32414B;\n"
"  margin-top: 2px;\n"
"  padding-left: 2px;\n"
"  padding-right: 2px;\n"
"  padding-top: 4px;\n"
"  padding-bottom: 4px;\n"
"  border-top-right-radius: 3px;\n"
"  border-bottom-right-radius: 3px;\n"
"  min-height: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"  color: #F0F0F0;\n"
"  background-color: #505F69;\n"
"  border-left: 3px solid #1464A0;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:hover {\n"
"  border: 1px solid #148CD2;\n"
"  border-left: 3px solid #148CD2;\n"
"  padding: 0px;\n"
"}\n"
"\n"
"QTabBar QToolButton {\n"
"  /* Fixes #136 */\n"
"  background-color:"
                        " #32414B;\n"
"  height: 12px;\n"
"  width: 12px;\n"
"}\n"
"\n"
"QTabBar QToolButton:pressed {\n"
"  background-color: #32414B;\n"
"}\n"
"\n"
"QTabBar QToolButton:pressed:hover {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:enabled {\n"
"  image: url(\":/qss_icons/rc/arrow_left.png\");\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:disabled {\n"
"  image: url(\":/qss_icons/rc/arrow_left_disabled.png\");\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:enabled {\n"
"  image: url(\":/qss_icons/rc/arrow_right.png\");\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:disabled {\n"
"  image: url(\":/qss_icons/rc/arrow_right_disabled.png\");\n"
"}\n"
"\n"
"/* QDockWiget -------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QDockWidget {\n"
"  outline: 1px solid #32414B;\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  titlebar-close-icon: "
                        "url(\":/qss_icons/rc/window_close.png\");\n"
"  titlebar-normal-icon: url(\":/qss_icons/rc/window_undock.png\");\n"
"}\n"
"\n"
"QDockWidget::title {\n"
"  /* Better size for title bar */\n"
"  padding: 6px;\n"
"  spacing: 4px;\n"
"  border: none;\n"
"  background-color: #32414B;\n"
"}\n"
"\n"
"QDockWidget::close-button {\n"
"  background-color: #32414B;\n"
"  border-radius: 4px;\n"
"  border: none;\n"
"}\n"
"\n"
"QDockWidget::close-button:hover {\n"
"  image: url(\":/qss_icons/rc/window_close_focus.png\");\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed {\n"
"  image: url(\":/qss_icons/rc/window_close_pressed.png\");\n"
"}\n"
"\n"
"QDockWidget::float-button {\n"
"  background-color: #32414B;\n"
"  border-radius: 4px;\n"
"  border: none;\n"
"}\n"
"\n"
"QDockWidget::float-button:hover {\n"
"  image: url(\":/qss_icons/rc/window_undock_focus.png\");\n"
"}\n"
"\n"
"QDockWidget::float-button:pressed {\n"
"  image: url(\":/qss_icons/rc/window_undock_pressed.png\");\n"
"}\n"
"\n"
"/* QTreeView QListView QTableView --"
                        "---------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtreeview\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qlistview\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtableview\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTreeView:branch:selected, QTreeView:branch:hover {\n"
"  background: url(\":/qss_icons/rc/transparent.png\");\n"
"}\n"
"\n"
"QTreeView:branch:has-siblings:!adjoins-item {\n"
"  border-image: url(\":/qss_icons/rc/branch_line.png\") 0;\n"
"}\n"
"\n"
"QTreeView:branch:has-siblings:adjoins-item {\n"
"  border-image: url(\":/qss_icons/rc/branch_more.png\") 0;\n"
"}\n"
"\n"
"QTreeView:branch:!has-children:!has-siblings:adjoins-item {\n"
"  border-image: url(\":/qss_icons/rc/branch_end.png\") 0;\n"
"}\n"
"\n"
"QTreeView:branch:has-children:!has-siblings:closed, QTreeView:branch:closed:has-children:has-siblings {\n"
"  border-image: none;\n"
"  image: url(\":/qss_"
                        "icons/rc/branch_closed.png\");\n"
"}\n"
"\n"
"QTreeView:branch:open:has-children:!has-siblings, QTreeView:branch:open:has-children:has-siblings {\n"
"  border-image: none;\n"
"  image: url(\":/qss_icons/rc/branch_open.png\");\n"
"}\n"
"\n"
"QTreeView:branch:has-children:!has-siblings:closed:hover, QTreeView:branch:closed:has-children:has-siblings:hover {\n"
"  image: url(\":/qss_icons/rc/branch_closed_focus.png\");\n"
"}\n"
"\n"
"QTreeView:branch:open:has-children:!has-siblings:hover, QTreeView:branch:open:has-children:has-siblings:hover {\n"
"  image: url(\":/qss_icons/rc/branch_open_focus.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:checked,\n"
"QListView::indicator:checked {\n"
"  image: url(\":/qss_icons/rc/checkbox_checked.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:checked:hover, QTreeView::indicator:checked:focus, QTreeView::indicator:checked:pressed,\n"
"QListView::indicator:checked:hover,\n"
"QListView::indicator:checked:focus,\n"
"QListView::indicator:checked:pressed {\n"
"  image: url(\":/qss_icons/r"
                        "c/checkbox_checked_focus.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:unchecked,\n"
"QListView::indicator:unchecked {\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:unchecked:hover, QTreeView::indicator:unchecked:focus, QTreeView::indicator:unchecked:pressed,\n"
"QListView::indicator:unchecked:hover,\n"
"QListView::indicator:unchecked:focus,\n"
"QListView::indicator:unchecked:pressed {\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked_focus.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:indeterminate,\n"
"QListView::indicator:indeterminate {\n"
"  image: url(\":/qss_icons/rc/checkbox_indeterminate.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:indeterminate:hover, QTreeView::indicator:indeterminate:focus, QTreeView::indicator:indeterminate:pressed,\n"
"QListView::indicator:indeterminate:hover,\n"
"QListView::indicator:indeterminate:focus,\n"
"QListView::indicator:indeterminate:pressed {\n"
"  image: url(\":/qss_icons/rc/checkbox_indeterminate_focus.png\");\n"
"}\n"
""
                        "\n"
"QTreeView,\n"
"QListView,\n"
"QTableView,\n"
"QColumnView {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  gridline-color: #32414B;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QTreeView:disabled,\n"
"QListView:disabled,\n"
"QTableView:disabled,\n"
"QColumnView:disabled {\n"
"  background-color: #19232D;\n"
"  color: #787878;\n"
"}\n"
"\n"
"QTreeView:selected,\n"
"QListView:selected,\n"
"QTableView:selected,\n"
"QColumnView:selected {\n"
"  background-color: #1464A0;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"QTreeView:hover,\n"
"QListView:hover,\n"
"QTableView:hover,\n"
"QColumnView:hover {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QTreeView::item:pressed,\n"
"QListView::item:pressed,\n"
"QTableView::item:pressed,\n"
"QColumnView::item:pressed {\n"
"  background-color: #1464A0;\n"
"}\n"
"\n"
"QTreeView::item:selected:hover,\n"
"QListView::item:selected:hover,\n"
"QTableView::item:selected:hover,\n"
"QColumnView::item:selected:hov"
                        "er {\n"
"  background: #1464A0;\n"
"  color: #19232D;\n"
"}\n"
"\n"
"QTreeView::item:selected:active,\n"
"QListView::item:selected:active,\n"
"QTableView::item:selected:active,\n"
"QColumnView::item:selected:active {\n"
"  background-color: #1464A0;\n"
"}\n"
"\n"
"QTreeView::item:!selected:hover,\n"
"QListView::item:!selected:hover,\n"
"QTableView::item:!selected:hover,\n"
"QColumnView::item:!selected:hover {\n"
"  outline: 0;\n"
"  color: #148CD2;\n"
"  background-color: #32414B;\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"  background-color: #19232D;\n"
"  border: 1px transparent #32414B;\n"
"  border-radius: 0px;\n"
"}\n"
"\n"
"/* QHeaderView ------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qheaderview\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QHeaderView {\n"
"  background-color: #32414B;\n"
"  border: 0px transparent #32414B;\n"
"  padding: 0px;\n"
"  margin: 0px;\n"
"  b"
                        "order-radius: 0px;\n"
"}\n"
"\n"
"QHeaderView:disabled {\n"
"  background-color: #32414B;\n"
"  border: 1px transparent #32414B;\n"
"  padding: 2px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"  background-color: #32414B;\n"
"  color: #F0F0F0;\n"
"  padding: 2px;\n"
"  border-radius: 0px;\n"
"  text-align: left;\n"
"}\n"
"\n"
"QHeaderView::section:checked {\n"
"  color: #F0F0F0;\n"
"  background-color: #1464A0;\n"
"}\n"
"\n"
"QHeaderView::section:checked:disabled {\n"
"  color: #787878;\n"
"  background-color: #14506E;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal {\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  border-left: 1px solid #19232D;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal::first, QHeaderView::section::horizontal::only-one {\n"
"  border-left: 1px solid #32414B;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal:disabled {\n"
"  color: #787878;\n"
"}\n"
"\n"
"QHeaderView::section::vertical {\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  border-top: 1px solid #19232D;\n"
"}\n"
""
                        "\n"
"QHeaderView::section::vertical::first, QHeaderView::section::vertical::only-one {\n"
"  border-top: 1px solid #32414B;\n"
"}\n"
"\n"
"QHeaderView::section::vertical:disabled {\n"
"  color: #787878;\n"
"}\n"
"\n"
"QHeaderView::down-arrow {\n"
"  /* Those settings (border/width/height/background-color) solve bug */\n"
"  /* transparent arrow background and size */\n"
"  background-color: #32414B;\n"
"  border: none;\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  padding-left: 2px;\n"
"  padding-right: 2px;\n"
"  image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"  background-color: #32414B;\n"
"  border: none;\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  padding-left: 2px;\n"
"  padding-right: 2px;\n"
"  image: url(\":/qss_icons/rc/arrow_up.png\");\n"
"}\n"
"\n"
"/* QToolBox --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtoolbox\n"
"\n"
"-------------------------------------------------"
                        "-------------------------- */\n"
"QToolBox {\n"
"  padding: 0px;\n"
"  border: 0px;\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"QToolBox:selected {\n"
"  padding: 0px;\n"
"  border: 2px solid #1464A0;\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  border-top-left-radius: 4px;\n"
"  border-top-right-radius: 4px;\n"
"}\n"
"\n"
"QToolBox::tab:disabled {\n"
"  color: #787878;\n"
"}\n"
"\n"
"QToolBox::tab:selected {\n"
"  background-color: #505F69;\n"
"  border-bottom: 2px solid #1464A0;\n"
"}\n"
"\n"
"QToolBox::tab:selected:disabled {\n"
"  background-color: #32414B;\n"
"  border-bottom: 2px solid #14506E;\n"
"}\n"
"\n"
"QToolBox::tab:!selected {\n"
"  background-color: #32414B;\n"
"  border-bottom: 2px solid #32414B;\n"
"}\n"
"\n"
"QToolBox::tab:!selected:disabled {\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QToolBox::tab:hover {\n"
"  border-color: #148CD2;\n"
"  border-bottom: 2px solid #148CD2;\n"
"}\n"
"\n"
"QToolBox QScrol"
                        "lArea QWidget QWidget {\n"
"  padding: 0px;\n"
"  border: 0px;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"/* QFrame -----------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qframe\n"
"https://doc.qt.io/qt-5/qframe.html#-prop\n"
"https://doc.qt.io/qt-5/qframe.html#details\n"
"https://stackoverflow.com/questions/14581498/qt-stylesheet-for-hline-vline-color\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"/* (dot) .QFrame  fix #141, #126, #123 */\n"
".QFrame {\n"
"  border-radius: 4px;\n"
"  border: 1px solid #32414B;\n"
"  /* No frame */\n"
"  /* HLine */\n"
"  /* HLine */\n"
"}\n"
"\n"
".QFrame[frameShape=\"0\"] {\n"
"  border-radius: 4px;\n"
"  border: 1px transparent #32414B;\n"
"}\n"
"\n"
".QFrame[frameShape=\"4\"] {\n"
"  max-height: 2px;\n"
"  border: none;\n"
"  background-color: #32414B;\n"
"}\n"
"\n"
".QFrame[frameShape=\"5\"] {\n"
"  max-width: 2px;\n"
"  border: none;\n"
"  bac"
                        "kground-color: #32414B;\n"
"}\n"
"\n"
"/* QSplitter --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qsplitter\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QSplitter {\n"
"  background-color: #32414B;\n"
"  spacing: 0px;\n"
"  padding: 0px;\n"
"  margin: 0px;\n"
"}\n"
"\n"
"QSplitter::handle {\n"
"  background-color: #32414B;\n"
"  border: 0px solid #19232D;\n"
"  spacing: 0px;\n"
"  padding: 1px;\n"
"  margin: 0px;\n"
"}\n"
"\n"
"QSplitter::handle:hover {\n"
"  background-color: #787878;\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"  width: 5px;\n"
"  image: url(\":/qss_icons/rc/line_vertical.png\");\n"
"}\n"
"\n"
"QSplitter::handle:vertical {\n"
"  height: 5px;\n"
"  image: url(\":/qss_icons/rc/line_horizontal.png\");\n"
"}\n"
"\n"
"/* QDateEdit, QDateTimeEdit -----------------------------------------------\n"
"\n"
"------------------------------------------------------------"
                        "--------------- */\n"
"QDateEdit, QDateTimeEdit {\n"
"  selection-background-color: #1464A0;\n"
"  border-style: solid;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  /* This fixes 103, 111 */\n"
"  padding-top: 2px;\n"
"  /* This fixes 103, 111 */\n"
"  padding-bottom: 2px;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  min-width: 10px;\n"
"}\n"
"\n"
"QDateEdit:on, QDateTimeEdit:on {\n"
"  selection-background-color: #1464A0;\n"
"}\n"
"\n"
"QDateEdit::drop-down, QDateTimeEdit::drop-down {\n"
"  subcontrol-origin: padding;\n"
"  subcontrol-position: top right;\n"
"  width: 12px;\n"
"  border-left: 1px solid #32414B;\n"
"}\n"
"\n"
"QDateEdit::down-arrow, QDateTimeEdit::down-arrow {\n"
"  image: url(\":/qss_icons/rc/arrow_down_disabled.png\");\n"
"  height: 8px;\n"
"  width: 8px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow:on, QDateEdit::down-arrow:hover, QDateEdit::down-arrow:focus, QDateTimeEdit::down-arrow:on, QDateTimeEdit::down-arrow:hover, QDateTimeEdit::down-arrow:focus {\n"
"  image:"
                        " url(\":/qss_icons/rc/arrow_down.png\");\n"
"}\n"
"\n"
"QDateEdit QAbstractItemView, QDateTimeEdit QAbstractItemView {\n"
"  background-color: #19232D;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #32414B;\n"
"  selection-background-color: #1464A0;\n"
"}\n"
"\n"
"/* QAbstractView ----------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QAbstractView:hover {\n"
"  border: 1px solid #148CD2;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QAbstractView:selected {\n"
"  background: #1464A0;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"/* PlotWidget -------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"PlotWidget {\n"
"  /* Fix cut labels in plots #134 */\n"
"  padding: 0px;\n"
"}")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionGuardar_como = QAction(MainWindow)
        self.actionGuardar_como.setObjectName(u"actionGuardar_como")
        self.actionDirectorio_base = QAction(MainWindow)
        self.actionDirectorio_base.setObjectName(u"actionDirectorio_base")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionDuplicate = QAction(MainWindow)
        self.actionDuplicate.setObjectName(u"actionDuplicate")
        icon1 = QIcon()
        icon1.addFile(u":/resources/cnc.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDuplicate.setIcon(icon1)
        self.actionDelete = QAction(MainWindow)
        self.actionDelete.setObjectName(u"actionDelete")
        self.actionVersion = QAction(MainWindow)
        self.actionVersion.setObjectName(u"actionVersion")
        self.actionInvert_X = QAction(MainWindow)
        self.actionInvert_X.setObjectName(u"actionInvert_X")
        self.actionInvert_Y = QAction(MainWindow)
        self.actionInvert_Y.setObjectName(u"actionInvert_Y")
        self.actionInvert_Z = QAction(MainWindow)
        self.actionInvert_Z.setObjectName(u"actionInvert_Z")
        self.actionMove_up = QAction(MainWindow)
        self.actionMove_up.setObjectName(u"actionMove_up")
        self.actionMove_down = QAction(MainWindow)
        self.actionMove_down.setObjectName(u"actionMove_down")
        self.actionGo_to = QAction(MainWindow)
        self.actionGo_to.setObjectName(u"actionGo_to")
        self.actionReturn_to = QAction(MainWindow)
        self.actionReturn_to.setObjectName(u"actionReturn_to")
        self.actionShow_functions = QAction(MainWindow)
        self.actionShow_functions.setObjectName(u"actionShow_functions")
        self.actionShow_tape1_widget = QAction(MainWindow)
        self.actionShow_tape1_widget.setObjectName(u"actionShow_tape1_widget")
        self.actionShow_tape2_widget = QAction(MainWindow)
        self.actionShow_tape2_widget.setObjectName(u"actionShow_tape2_widget")
        self.actionHide_functions = QAction(MainWindow)
        self.actionHide_functions.setObjectName(u"actionHide_functions")
        self.actionHide_tape1_widget = QAction(MainWindow)
        self.actionHide_tape1_widget.setObjectName(u"actionHide_tape1_widget")
        self.actionHide_tape2_widget = QAction(MainWindow)
        self.actionHide_tape2_widget.setObjectName(u"actionHide_tape2_widget")
        self.actionSeleccionar_maquina = QAction(MainWindow)
        self.actionSeleccionar_maquina.setObjectName(u"actionSeleccionar_maquina")
        self.actionShow_config_widget = QAction(MainWindow)
        self.actionShow_config_widget.setObjectName(u"actionShow_config_widget")
        self.actionHide_config_widget = QAction(MainWindow)
        self.actionHide_config_widget.setObjectName(u"actionHide_config_widget")
        self.actionBlock = QAction(MainWindow)
        self.actionBlock.setObjectName(u"actionBlock")
        self.actionGraph = QAction(MainWindow)
        self.actionGraph.setObjectName(u"actionGraph")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tape1_widget = QTableWidget(self.centralwidget)
        if (self.tape1_widget.columnCount() < 1):
            self.tape1_widget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tape1_widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tape1_widget.setObjectName(u"tape1_widget")
        self.tape1_widget.setStyleSheet(u"QWidget {\n"
"  background-color: #000000;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"}")
        self.tape1_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tape1_widget.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.tape1_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tape1_widget.setColumnCount(1)
        self.tape1_widget.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout.addWidget(self.tape1_widget)

        self.tape2_widget = QTableWidget(self.centralwidget)
        if (self.tape2_widget.columnCount() < 1):
            self.tape2_widget.setColumnCount(1)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tape2_widget.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        self.tape2_widget.setObjectName(u"tape2_widget")
        self.tape2_widget.setStyleSheet(u"QWidget {\n"
"  background-color: #000000;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"}")
        self.tape2_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tape2_widget.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.tape2_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tape2_widget.setColumnCount(1)
        self.tape2_widget.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout.addWidget(self.tape2_widget)

        self.config_widget = QTableWidget(self.centralwidget)
        if (self.config_widget.columnCount() < 1):
            self.config_widget.setColumnCount(1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.config_widget.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        self.config_widget.setObjectName(u"config_widget")
        self.config_widget.setStyleSheet(u"QWidget {\n"
"  background-color: #000000;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"}")
        self.config_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.config_widget.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.config_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.config_widget.setColumnCount(1)
        self.config_widget.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout.addWidget(self.config_widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1292, 31))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuShow = QMenu(self.menuView)
        self.menuShow.setObjectName(u"menuShow")
        self.menuHide = QMenu(self.menuView)
        self.menuHide.setObjectName(u"menuHide")
        self.menuNavigate = QMenu(self.menubar)
        self.menuNavigate.setObjectName(u"menuNavigate")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dock_functions = QDockWidget(MainWindow)
        self.dock_functions.setObjectName(u"dock_functions")
        sizePolicy.setHeightForWidth(self.dock_functions.sizePolicy().hasHeightForWidth())
        self.dock_functions.setSizePolicy(sizePolicy)
        self.dock_functions.setMinimumSize(QSize(171, 858))
        self.dock_functions.setStyleSheet(u"")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout_5 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tabWidget_principal = QTabWidget(self.dockWidgetContents)
        self.tabWidget_principal.setObjectName(u"tabWidget_principal")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget_principal.sizePolicy().hasHeightForWidth())
        self.tabWidget_principal.setSizePolicy(sizePolicy1)
        self.tabWidget_principal.setStyleSheet(u"")
        self.tabWidget_principal_functions = QWidget()
        self.tabWidget_principal_functions.setObjectName(u"tabWidget_principal_functions")
        self.gridLayout_4 = QGridLayout(self.tabWidget_principal_functions)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox_machine = QGroupBox(self.tabWidget_principal_functions)
        self.groupBox_machine.setObjectName(u"groupBox_machine")
        sizePolicy.setHeightForWidth(self.groupBox_machine.sizePolicy().hasHeightForWidth())
        self.groupBox_machine.setSizePolicy(sizePolicy)
        self.groupBox_machine.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.groupBox_machine)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(3)
        self.gridLayout_3.setVerticalSpacing(5)
        self.gridLayout_3.setContentsMargins(1, 10, 1, 1)
        self.btn_spindle_index = QPushButton(self.groupBox_machine)
        self.btn_spindle_index.setObjectName(u"btn_spindle_index")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_spindle_index.sizePolicy().hasHeightForWidth())
        self.btn_spindle_index.setSizePolicy(sizePolicy2)
        self.btn_spindle_index.setMinimumSize(QSize(28, 0))
        self.btn_spindle_index.setMaximumSize(QSize(120, 16777215))

        self.gridLayout_3.addWidget(self.btn_spindle_index, 2, 0, 1, 1)

        self.btn_spindle = QPushButton(self.groupBox_machine)
        self.btn_spindle.setObjectName(u"btn_spindle")

        self.gridLayout_3.addWidget(self.btn_spindle, 0, 0, 1, 1)

        self.btn_misc = QPushButton(self.groupBox_machine)
        self.btn_misc.setObjectName(u"btn_misc")
        sizePolicy2.setHeightForWidth(self.btn_misc.sizePolicy().hasHeightForWidth())
        self.btn_misc.setSizePolicy(sizePolicy2)
        self.btn_misc.setMinimumSize(QSize(28, 0))
        self.btn_misc.setMaximumSize(QSize(120, 16777215))

        self.gridLayout_3.addWidget(self.btn_misc, 3, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_machine, 2, 0, 1, 1)

        self.groupBox_tool = QGroupBox(self.tabWidget_principal_functions)
        self.groupBox_tool.setObjectName(u"groupBox_tool")
        sizePolicy.setHeightForWidth(self.groupBox_tool.sizePolicy().hasHeightForWidth())
        self.groupBox_tool.setSizePolicy(sizePolicy)
        self.groupBox_tool.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.groupBox_tool)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(3)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(1, 10, 1, 1)
        self.btn_tool_call = QPushButton(self.groupBox_tool)
        self.btn_tool_call.setObjectName(u"btn_tool_call")
        sizePolicy2.setHeightForWidth(self.btn_tool_call.sizePolicy().hasHeightForWidth())
        self.btn_tool_call.setSizePolicy(sizePolicy2)
        self.btn_tool_call.setMinimumSize(QSize(28, 0))
        self.btn_tool_call.setMaximumSize(QSize(120, 16777215))

        self.gridLayout_2.addWidget(self.btn_tool_call, 2, 0, 1, 1)

        self.btn_tool_close = QPushButton(self.groupBox_tool)
        self.btn_tool_close.setObjectName(u"btn_tool_close")
        sizePolicy2.setHeightForWidth(self.btn_tool_close.sizePolicy().hasHeightForWidth())
        self.btn_tool_close.setSizePolicy(sizePolicy2)
        self.btn_tool_close.setMinimumSize(QSize(28, 0))
        self.btn_tool_close.setMaximumSize(QSize(120, 16777215))

        self.gridLayout_2.addWidget(self.btn_tool_close, 3, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_tool, 1, 0, 1, 1)

        self.groupBox_program = QGroupBox(self.tabWidget_principal_functions)
        self.groupBox_program.setObjectName(u"groupBox_program")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_program.sizePolicy().hasHeightForWidth())
        self.groupBox_program.setSizePolicy(sizePolicy3)
        self.groupBox_program.setStyleSheet(u"")
        self.groupBox_program.setCheckable(False)
        self.gridLayout = QGridLayout(self.groupBox_program)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setContentsMargins(1, 10, 1, 1)
        self.btn_comment = QPushButton(self.groupBox_program)
        self.btn_comment.setObjectName(u"btn_comment")
        sizePolicy2.setHeightForWidth(self.btn_comment.sizePolicy().hasHeightForWidth())
        self.btn_comment.setSizePolicy(sizePolicy2)
        self.btn_comment.setMinimumSize(QSize(28, 0))
        self.btn_comment.setMaximumSize(QSize(120, 16777215))

        self.gridLayout.addWidget(self.btn_comment, 3, 0, 1, 1)

        self.btn_header = QPushButton(self.groupBox_program)
        self.btn_header.setObjectName(u"btn_header")
        sizePolicy2.setHeightForWidth(self.btn_header.sizePolicy().hasHeightForWidth())
        self.btn_header.setSizePolicy(sizePolicy2)
        self.btn_header.setMinimumSize(QSize(28, 0))
        self.btn_header.setMaximumSize(QSize(120, 16777215))
        self.btn_header.setFlat(False)

        self.gridLayout.addWidget(self.btn_header, 0, 0, 1, 1)

        self.btn_subrutine = QPushButton(self.groupBox_program)
        self.btn_subrutine.setObjectName(u"btn_subrutine")

        self.gridLayout.addWidget(self.btn_subrutine, 5, 0, 1, 1)

        self.btn_end = QPushButton(self.groupBox_program)
        self.btn_end.setObjectName(u"btn_end")
        sizePolicy2.setHeightForWidth(self.btn_end.sizePolicy().hasHeightForWidth())
        self.btn_end.setSizePolicy(sizePolicy2)
        self.btn_end.setMinimumSize(QSize(28, 0))
        self.btn_end.setMaximumSize(QSize(120, 16777215))

        self.gridLayout.addWidget(self.btn_end, 7, 0, 1, 1)

        self.btn_free = QPushButton(self.groupBox_program)
        self.btn_free.setObjectName(u"btn_free")
        self.btn_free.setMinimumSize(QSize(28, 0))
        self.btn_free.setMaximumSize(QSize(120, 16777215))

        self.gridLayout.addWidget(self.btn_free, 1, 0, 1, 1)

        self.btn_collect = QPushButton(self.groupBox_program)
        self.btn_collect.setObjectName(u"btn_collect")
        sizePolicy2.setHeightForWidth(self.btn_collect.sizePolicy().hasHeightForWidth())
        self.btn_collect.setSizePolicy(sizePolicy2)
        self.btn_collect.setMinimumSize(QSize(28, 0))
        self.btn_collect.setMaximumSize(QSize(120, 16777215))

        self.gridLayout.addWidget(self.btn_collect, 6, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_program, 0, 0, 1, 1)

        self.tabWidget_principal.addTab(self.tabWidget_principal_functions, "")

        self.verticalLayout_5.addWidget(self.tabWidget_principal)

        self.tabWidget_functions = QTabWidget(self.dockWidgetContents)
        self.tabWidget_functions.setObjectName(u"tabWidget_functions")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tabWidget_functions.sizePolicy().hasHeightForWidth())
        self.tabWidget_functions.setSizePolicy(sizePolicy4)
        self.tabWidget_functions.setMinimumSize(QSize(0, 0))
        self.tabWidget_functions.setMaximumSize(QSize(16777215, 16777215))
        self.tabWidget_functions_turning = QWidget()
        self.tabWidget_functions_turning.setObjectName(u"tabWidget_functions_turning")
        self.verticalLayout_2 = QVBoxLayout(self.tabWidget_functions_turning)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_turning = QGroupBox(self.tabWidget_functions_turning)
        self.groupBox_turning.setObjectName(u"groupBox_turning")
        self.groupBox_turning.setFlat(True)
        self.gridLayout_5 = QGridLayout(self.groupBox_turning)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(3)
        self.gridLayout_5.setVerticalSpacing(5)
        self.gridLayout_5.setContentsMargins(1, 10, 1, 1)
        self.btn_lineal = QPushButton(self.groupBox_turning)
        self.btn_lineal.setObjectName(u"btn_lineal")
        sizePolicy2.setHeightForWidth(self.btn_lineal.sizePolicy().hasHeightForWidth())
        self.btn_lineal.setSizePolicy(sizePolicy2)
        self.btn_lineal.setMinimumSize(QSize(28, 0))
        self.btn_lineal.setMaximumSize(QSize(120, 16777215))

        self.gridLayout_5.addWidget(self.btn_lineal, 0, 0, 1, 1)

        self.btn_radial = QPushButton(self.groupBox_turning)
        self.btn_radial.setObjectName(u"btn_radial")

        self.gridLayout_5.addWidget(self.btn_radial, 1, 0, 1, 1)

        self.btn_thread = QPushButton(self.groupBox_turning)
        self.btn_thread.setObjectName(u"btn_thread")

        self.gridLayout_5.addWidget(self.btn_thread, 2, 0, 1, 1)

        self.btn_cutoff = QPushButton(self.groupBox_turning)
        self.btn_cutoff.setObjectName(u"btn_cutoff")

        self.gridLayout_5.addWidget(self.btn_cutoff, 3, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_turning)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.tabWidget_functions.addTab(self.tabWidget_functions_turning, "")
        self.tabWidget_functions_milling = QWidget()
        self.tabWidget_functions_milling.setObjectName(u"tabWidget_functions_milling")
        self.gridLayout_9 = QGridLayout(self.tabWidget_functions_milling)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.groupBox_milling = QGroupBox(self.tabWidget_functions_milling)
        self.groupBox_milling.setObjectName(u"groupBox_milling")
        self.groupBox_milling.setFlat(True)
        self.gridLayout_10 = QGridLayout(self.groupBox_milling)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setHorizontalSpacing(3)
        self.gridLayout_10.setVerticalSpacing(5)
        self.gridLayout_10.setContentsMargins(1, 10, 1, 1)
        self.btn_mill_end = QPushButton(self.groupBox_milling)
        self.btn_mill_end.setObjectName(u"btn_mill_end")

        self.gridLayout_10.addWidget(self.btn_mill_end, 1, 0, 1, 1)

        self.btn_lineal_3 = QPushButton(self.groupBox_milling)
        self.btn_lineal_3.setObjectName(u"btn_lineal_3")

        self.gridLayout_10.addWidget(self.btn_lineal_3, 2, 0, 1, 1)

        self.btn_radial_3 = QPushButton(self.groupBox_milling)
        self.btn_radial_3.setObjectName(u"btn_radial_3")

        self.gridLayout_10.addWidget(self.btn_radial_3, 3, 0, 1, 1)

        self.btn_mill_ini = QPushButton(self.groupBox_milling)
        self.btn_mill_ini.setObjectName(u"btn_mill_ini")

        self.gridLayout_10.addWidget(self.btn_mill_ini, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_milling, 0, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_8, 1, 0, 1, 1)

        self.tabWidget_functions.addTab(self.tabWidget_functions_milling, "")
        self.tabWidget_functions_mill_cycles = QWidget()
        self.tabWidget_functions_mill_cycles.setObjectName(u"tabWidget_functions_mill_cycles")
        self.verticalLayout_3 = QVBoxLayout(self.tabWidget_functions_mill_cycles)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_mill_cycles = QGroupBox(self.tabWidget_functions_mill_cycles)
        self.groupBox_mill_cycles.setObjectName(u"groupBox_mill_cycles")
        self.gridLayout_7 = QGridLayout(self.groupBox_mill_cycles)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(3)
        self.gridLayout_7.setVerticalSpacing(5)
        self.gridLayout_7.setContentsMargins(1, 10, 1, 1)
        self.btn_bevel = QPushButton(self.groupBox_mill_cycles)
        self.btn_bevel.setObjectName(u"btn_bevel")

        self.gridLayout_7.addWidget(self.btn_bevel, 4, 0, 1, 1)

        self.btn_facing = QPushButton(self.groupBox_mill_cycles)
        self.btn_facing.setObjectName(u"btn_facing")

        self.gridLayout_7.addWidget(self.btn_facing, 5, 0, 1, 1)

        self.btn_flat = QPushButton(self.groupBox_mill_cycles)
        self.btn_flat.setObjectName(u"btn_flat")

        self.gridLayout_7.addWidget(self.btn_flat, 2, 0, 1, 1)

        self.btn_face = QPushButton(self.groupBox_mill_cycles)
        self.btn_face.setObjectName(u"btn_face")

        self.gridLayout_7.addWidget(self.btn_face, 3, 0, 1, 1)

        self.btn_concaver = QPushButton(self.groupBox_mill_cycles)
        self.btn_concaver.setObjectName(u"btn_concaver")

        self.gridLayout_7.addWidget(self.btn_concaver, 7, 0, 1, 1)

        self.btn_slotting = QPushButton(self.groupBox_mill_cycles)
        self.btn_slotting.setObjectName(u"btn_slotting")

        self.gridLayout_7.addWidget(self.btn_slotting, 6, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_mill_cycles)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.tabWidget_functions.addTab(self.tabWidget_functions_mill_cycles, "")
        self.tabWidget_functions_drilling = QWidget()
        self.tabWidget_functions_drilling.setObjectName(u"tabWidget_functions_drilling")
        self.verticalLayout_4 = QVBoxLayout(self.tabWidget_functions_drilling)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_drilling = QGroupBox(self.tabWidget_functions_drilling)
        self.groupBox_drilling.setObjectName(u"groupBox_drilling")
        self.gridLayout_8 = QGridLayout(self.groupBox_drilling)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(3)
        self.gridLayout_8.setVerticalSpacing(5)
        self.gridLayout_8.setContentsMargins(1, 10, 1, 1)
        self.btn_csink = QPushButton(self.groupBox_drilling)
        self.btn_csink.setObjectName(u"btn_csink")

        self.gridLayout_8.addWidget(self.btn_csink, 4, 0, 1, 1)

        self.btn_drill = QPushButton(self.groupBox_drilling)
        self.btn_drill.setObjectName(u"btn_drill")

        self.gridLayout_8.addWidget(self.btn_drill, 3, 0, 1, 1)

        self.btn_drill_ini = QPushButton(self.groupBox_drilling)
        self.btn_drill_ini.setObjectName(u"btn_drill_ini")

        self.gridLayout_8.addWidget(self.btn_drill_ini, 0, 0, 1, 1)

        self.btn_ream = QPushButton(self.groupBox_drilling)
        self.btn_ream.setObjectName(u"btn_ream")

        self.gridLayout_8.addWidget(self.btn_ream, 5, 0, 1, 1)

        self.btn_drill_end = QPushButton(self.groupBox_drilling)
        self.btn_drill_end.setObjectName(u"btn_drill_end")

        self.gridLayout_8.addWidget(self.btn_drill_end, 1, 0, 1, 1)

        self.btn_center = QPushButton(self.groupBox_drilling)
        self.btn_center.setObjectName(u"btn_center")

        self.gridLayout_8.addWidget(self.btn_center, 2, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_drilling)

        self.verticalSpacer_2 = QSpacerItem(20, 369, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.tabWidget_functions.addTab(self.tabWidget_functions_drilling, "")
        self.tabWidget_functions_platter = QWidget()
        self.tabWidget_functions_platter.setObjectName(u"tabWidget_functions_platter")
        self.verticalLayout = QVBoxLayout(self.tabWidget_functions_platter)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_platter = QGroupBox(self.tabWidget_functions_platter)
        self.groupBox_platter.setObjectName(u"groupBox_platter")
        self.gridLayout_6 = QGridLayout(self.groupBox_platter)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(3)
        self.gridLayout_6.setVerticalSpacing(5)
        self.gridLayout_6.setContentsMargins(1, 10, 1, 1)
        self.btn_call_square = QPushButton(self.groupBox_platter)
        self.btn_call_square.setObjectName(u"btn_call_square")

        self.gridLayout_6.addWidget(self.btn_call_square, 1, 0, 1, 1)

        self.btn_lineal_rgh_y = QPushButton(self.groupBox_platter)
        self.btn_lineal_rgh_y.setObjectName(u"btn_lineal_rgh_y")

        self.gridLayout_6.addWidget(self.btn_lineal_rgh_y, 7, 0, 1, 1)

        self.btn_flatten = QPushButton(self.groupBox_platter)
        self.btn_flatten.setObjectName(u"btn_flatten")

        self.gridLayout_6.addWidget(self.btn_flatten, 3, 0, 1, 1)

        self.btn_call_lineal_y = QPushButton(self.groupBox_platter)
        self.btn_call_lineal_y.setObjectName(u"btn_call_lineal_y")

        self.gridLayout_6.addWidget(self.btn_call_lineal_y, 6, 0, 1, 1)

        self.btn_call_lineal_x = QPushButton(self.groupBox_platter)
        self.btn_call_lineal_x.setObjectName(u"btn_call_lineal_x")

        self.gridLayout_6.addWidget(self.btn_call_lineal_x, 4, 0, 1, 1)

        self.btn_call_flatten = QPushButton(self.groupBox_platter)
        self.btn_call_flatten.setObjectName(u"btn_call_flatten")

        self.gridLayout_6.addWidget(self.btn_call_flatten, 2, 0, 1, 1)

        self.btn_lineal_rgh_x = QPushButton(self.groupBox_platter)
        self.btn_lineal_rgh_x.setObjectName(u"btn_lineal_rgh_x")

        self.gridLayout_6.addWidget(self.btn_lineal_rgh_x, 5, 0, 1, 1)

        self.btn_platter_data = QPushButton(self.groupBox_platter)
        self.btn_platter_data.setObjectName(u"btn_platter_data")

        self.gridLayout_6.addWidget(self.btn_platter_data, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_platter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.tabWidget_functions.addTab(self.tabWidget_functions_platter, "")

        self.verticalLayout_5.addWidget(self.tabWidget_functions)

        self.dock_functions.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.dock_functions)
        QWidget.setTabOrder(self.btn_header, self.btn_comment)
        QWidget.setTabOrder(self.btn_comment, self.btn_tool_call)
        QWidget.setTabOrder(self.btn_tool_call, self.btn_tool_close)
        QWidget.setTabOrder(self.btn_tool_close, self.btn_spindle_index)
        QWidget.setTabOrder(self.btn_spindle_index, self.btn_lineal)
        QWidget.setTabOrder(self.btn_lineal, self.btn_radial)
        QWidget.setTabOrder(self.btn_radial, self.btn_thread)
        QWidget.setTabOrder(self.btn_thread, self.btn_cutoff)
        QWidget.setTabOrder(self.btn_cutoff, self.btn_flat)
        QWidget.setTabOrder(self.btn_flat, self.btn_face)
        QWidget.setTabOrder(self.btn_face, self.btn_bevel)
        QWidget.setTabOrder(self.btn_bevel, self.btn_facing)
        QWidget.setTabOrder(self.btn_facing, self.btn_slotting)
        QWidget.setTabOrder(self.btn_slotting, self.btn_concaver)
        QWidget.setTabOrder(self.btn_concaver, self.btn_center)
        QWidget.setTabOrder(self.btn_center, self.btn_drill)
        QWidget.setTabOrder(self.btn_drill, self.btn_csink)
        QWidget.setTabOrder(self.btn_csink, self.btn_ream)
        QWidget.setTabOrder(self.btn_ream, self.btn_platter_data)
        QWidget.setTabOrder(self.btn_platter_data, self.btn_call_square)
        QWidget.setTabOrder(self.btn_call_square, self.btn_call_flatten)
        QWidget.setTabOrder(self.btn_call_flatten, self.btn_flatten)
        QWidget.setTabOrder(self.btn_flatten, self.btn_call_lineal_x)
        QWidget.setTabOrder(self.btn_call_lineal_x, self.btn_lineal_rgh_x)
        QWidget.setTabOrder(self.btn_lineal_rgh_x, self.btn_call_lineal_y)
        QWidget.setTabOrder(self.btn_call_lineal_y, self.btn_lineal_rgh_y)
        QWidget.setTabOrder(self.btn_lineal_rgh_y, self.tabWidget_principal)
        QWidget.setTabOrder(self.tabWidget_principal, self.tape1_widget)
        QWidget.setTabOrder(self.tape1_widget, self.tape2_widget)
        QWidget.setTabOrder(self.tape2_widget, self.config_widget)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuNavigate.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuEdit.addAction(self.actionDuplicate)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionInvert_X)
        self.menuEdit.addAction(self.actionInvert_Y)
        self.menuEdit.addAction(self.actionInvert_Z)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionBlock)
        self.menuEdit.addAction(self.actionDelete)
        self.menuHelp.addAction(self.actionVersion)
        self.menuView.addAction(self.menuShow.menuAction())
        self.menuView.addAction(self.menuHide.menuAction())
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionGraph)
        self.menuShow.addAction(self.actionShow_functions)
        self.menuShow.addAction(self.actionShow_tape1_widget)
        self.menuShow.addAction(self.actionShow_tape2_widget)
        self.menuShow.addAction(self.actionShow_config_widget)
        self.menuHide.addAction(self.actionHide_functions)
        self.menuHide.addAction(self.actionHide_tape1_widget)
        self.menuHide.addAction(self.actionHide_tape2_widget)
        self.menuHide.addAction(self.actionHide_config_widget)
        self.menuNavigate.addAction(self.actionMove_up)
        self.menuNavigate.addAction(self.actionMove_down)
        self.menuNavigate.addAction(self.actionGo_to)
        self.menuNavigate.addAction(self.actionReturn_to)

        self.retranslateUi(MainWindow)
        self.actionShow_functions.triggered.connect(self.dock_functions.show)
        self.actionShow_tape1_widget.triggered.connect(self.tape1_widget.show)
        self.actionShow_tape2_widget.triggered.connect(self.tape2_widget.show)
        self.actionHide_functions.triggered.connect(self.dock_functions.hide)
        self.actionHide_tape1_widget.triggered.connect(self.tape1_widget.hide)
        self.actionHide_tape2_widget.triggered.connect(self.tape2_widget.hide)
        self.actionShow_config_widget.triggered.connect(self.config_widget.show)
        self.actionHide_config_widget.triggered.connect(self.config_widget.hide)
        self.dock_functions.dockLocationChanged.connect(self.dock_functions.update)

        self.tabWidget_principal.setCurrentIndex(0)
        self.tabWidget_functions.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CNC Editor", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
#if QT_CONFIG(statustip)
        self.actionNew.setStatusTip(QCoreApplication.translate("MainWindow", u"Crear un nuevo programa CNC", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(statustip)
        self.actionOpen.setStatusTip(QCoreApplication.translate("MainWindow", u"Abrir un programa CNC existente", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(statustip)
        self.actionSave.setStatusTip(QCoreApplication.translate("MainWindow", u"Guardar el programa CNC actual", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar_como.setText(QCoreApplication.translate("MainWindow", u"Guardar como", None))
#if QT_CONFIG(statustip)
        self.actionGuardar_como.setStatusTip(QCoreApplication.translate("MainWindow", u"Guardar el programa CNC actual con otro nombre", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionGuardar_como.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionDirectorio_base.setText(QCoreApplication.translate("MainWindow", u"Directorio base", None))
#if QT_CONFIG(statustip)
        self.actionDirectorio_base.setStatusTip(QCoreApplication.translate("MainWindow", u"Seleccionar el folder donde se va a trabajar", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionDirectorio_base.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Cerrar", None))
#if QT_CONFIG(statustip)
        self.actionClose.setStatusTip(QCoreApplication.translate("MainWindow", u"Cerrar la aplicaci\u00f3n", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionClose.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionDuplicate.setText(QCoreApplication.translate("MainWindow", u"Duplicar l\u00edneas       ", None))
#if QT_CONFIG(statustip)
        self.actionDuplicate.setStatusTip(QCoreApplication.translate("MainWindow", u"Duplicar las l\u00edneas seleccionadas", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionDuplicate.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+D", None))
#endif // QT_CONFIG(shortcut)
        self.actionDelete.setText(QCoreApplication.translate("MainWindow", u"Borrar l\u00edneas", None))
#if QT_CONFIG(statustip)
        self.actionDelete.setStatusTip(QCoreApplication.translate("MainWindow", u"Borrar las l\u00edneas seleccionadas", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionDelete.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.actionVersion.setText(QCoreApplication.translate("MainWindow", u"Versi\u00f3n", None))
#if QT_CONFIG(shortcut)
        self.actionVersion.setShortcut(QCoreApplication.translate("MainWindow", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.actionInvert_X.setText(QCoreApplication.translate("MainWindow", u"Invertir X", None))
#if QT_CONFIG(statustip)
        self.actionInvert_X.setStatusTip(QCoreApplication.translate("MainWindow", u"Invertir el signo de los movimientos en el eje X", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionInvert_X.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+X", None))
#endif // QT_CONFIG(shortcut)
        self.actionInvert_Y.setText(QCoreApplication.translate("MainWindow", u"Invertir Y", None))
#if QT_CONFIG(statustip)
        self.actionInvert_Y.setStatusTip(QCoreApplication.translate("MainWindow", u"Invertir el signo de los movimientos en el eje Y", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionInvert_Y.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Y", None))
#endif // QT_CONFIG(shortcut)
        self.actionInvert_Z.setText(QCoreApplication.translate("MainWindow", u"Invertir Z", None))
#if QT_CONFIG(statustip)
        self.actionInvert_Z.setStatusTip(QCoreApplication.translate("MainWindow", u"Invertir el signo de los movimientos en el eje Z", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionInvert_Z.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Z", None))
#endif // QT_CONFIG(shortcut)
        self.actionMove_up.setText(QCoreApplication.translate("MainWindow", u"Mover arriba", None))
#if QT_CONFIG(statustip)
        self.actionMove_up.setStatusTip(QCoreApplication.translate("MainWindow", u"Mover hacia arriba las l\u00edneas seleccionadas", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionMove_up.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Up", None))
#endif // QT_CONFIG(shortcut)
        self.actionMove_down.setText(QCoreApplication.translate("MainWindow", u"Mover abajo", None))
#if QT_CONFIG(statustip)
        self.actionMove_down.setStatusTip(QCoreApplication.translate("MainWindow", u"Mover hacia abajo las l\u00edneas seleccionadas", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionMove_down.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Down", None))
#endif // QT_CONFIG(shortcut)
        self.actionGo_to.setText(QCoreApplication.translate("MainWindow", u"Ir a programa", None))
#if QT_CONFIG(statustip)
        self.actionGo_to.setStatusTip(QCoreApplication.translate("MainWindow", u"Cambiar al programa CNC seleccionado", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionGo_to.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Right", None))
#endif // QT_CONFIG(shortcut)
        self.actionReturn_to.setText(QCoreApplication.translate("MainWindow", u"Regresar a programa      ", None))
#if QT_CONFIG(statustip)
        self.actionReturn_to.setStatusTip(QCoreApplication.translate("MainWindow", u"Regresar al programa CNC anterior", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionReturn_to.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Left", None))
#endif // QT_CONFIG(shortcut)
        self.actionShow_functions.setText(QCoreApplication.translate("MainWindow", u"Barra de funciones", None))
#if QT_CONFIG(statustip)
        self.actionShow_functions.setStatusTip(QCoreApplication.translate("MainWindow", u"Mostrar la barra de funciones", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionShow_functions.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.actionShow_tape1_widget.setText(QCoreApplication.translate("MainWindow", u"Ventana programa 1", None))
#if QT_CONFIG(statustip)
        self.actionShow_tape1_widget.setStatusTip(QCoreApplication.translate("MainWindow", u"Mostrar la ventana del programa principal", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionShow_tape1_widget.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.actionShow_tape2_widget.setText(QCoreApplication.translate("MainWindow", u"Ventana programa 2", None))
#if QT_CONFIG(statustip)
        self.actionShow_tape2_widget.setStatusTip(QCoreApplication.translate("MainWindow", u"Mostrar la ventana del programa secundario", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionShow_tape2_widget.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.actionHide_functions.setText(QCoreApplication.translate("MainWindow", u"Barra de funciones", None))
#if QT_CONFIG(statustip)
        self.actionHide_functions.setStatusTip(QCoreApplication.translate("MainWindow", u"Ocultar la barra de funciones", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionHide_functions.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.actionHide_tape1_widget.setText(QCoreApplication.translate("MainWindow", u"Ventana programa 1", None))
#if QT_CONFIG(statustip)
        self.actionHide_tape1_widget.setStatusTip(QCoreApplication.translate("MainWindow", u"Ocultar la ventana del programa principal", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionHide_tape1_widget.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.actionHide_tape2_widget.setText(QCoreApplication.translate("MainWindow", u"Ventana programa 2", None))
#if QT_CONFIG(statustip)
        self.actionHide_tape2_widget.setStatusTip(QCoreApplication.translate("MainWindow", u"Ocultar la ventana del programa secundario", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionHide_tape2_widget.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.actionSeleccionar_maquina.setText(QCoreApplication.translate("MainWindow", u"Seleccionar m\u00e1quina", None))
#if QT_CONFIG(statustip)
        self.actionSeleccionar_maquina.setStatusTip(QCoreApplication.translate("MainWindow", u"Seleccionar el tipo de m\u00e1quina a programar", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionSeleccionar_maquina.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+M", None))
#endif // QT_CONFIG(shortcut)
        self.actionShow_config_widget.setText(QCoreApplication.translate("MainWindow", u"Esquema programa", None))
#if QT_CONFIG(statustip)
        self.actionShow_config_widget.setStatusTip(QCoreApplication.translate("MainWindow", u"Mostrar el esquema del programa", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionShow_config_widget.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.actionHide_config_widget.setText(QCoreApplication.translate("MainWindow", u"Esquema programa", None))
#if QT_CONFIG(statustip)
        self.actionHide_config_widget.setStatusTip(QCoreApplication.translate("MainWindow", u"Ocultar el esquema del programa", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionHide_config_widget.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.actionBlock.setText(QCoreApplication.translate("MainWindow", u"Bloquear l\u00edneas", None))
#if QT_CONFIG(statustip)
        self.actionBlock.setStatusTip(QCoreApplication.translate("MainWindow", u"Bloquear las l\u00edneas seleccionadas", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionBlock.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.actionGraph.setText(QCoreApplication.translate("MainWindow", u"Graficar tape", None))
#if QT_CONFIG(shortcut)
        self.actionGraph.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+G", None))
#endif // QT_CONFIG(shortcut)
        ___qtablewidgetitem = self.tape1_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Programa principal", None));
        ___qtablewidgetitem1 = self.tape2_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Programa secundario", None));
        ___qtablewidgetitem2 = self.config_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Esquema", None));
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"Visualizar", None))
        self.menuShow.setTitle(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.menuHide.setTitle(QCoreApplication.translate("MainWindow", u"Ocultar", None))
        self.menuNavigate.setTitle(QCoreApplication.translate("MainWindow", u"Navegar", None))
        self.dock_functions.setWindowTitle(QCoreApplication.translate("MainWindow", u"Funciones", None))
        self.groupBox_machine.setTitle(QCoreApplication.translate("MainWindow", u"M\u00e1quina", None))
#if QT_CONFIG(tooltip)
        self.btn_spindle_index.setToolTip(QCoreApplication.translate("MainWindow", u"Orientar el husillo a X cantidad de grados", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_spindle_index.setStatusTip(QCoreApplication.translate("MainWindow", u"Orientar el husillo a X cantidad de grados", None))
#endif // QT_CONFIG(statustip)
        self.btn_spindle_index.setText(QCoreApplication.translate("MainWindow", u"&Orientar husillo", None))
#if QT_CONFIG(tooltip)
        self.btn_spindle.setToolTip(QCoreApplication.translate("MainWindow", u"Indique el sentido y velocidad de giro del husillo", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_spindle.setStatusTip(QCoreApplication.translate("MainWindow", u"Indique el sentido y velocidad de giro del husillo", None))
#endif // QT_CONFIG(statustip)
        self.btn_spindle.setText(QCoreApplication.translate("MainWindow", u"Giro del hu&sillo", None))
#if QT_CONFIG(tooltip)
        self.btn_misc.setToolTip(QCoreApplication.translate("MainWindow", u"Funciones miscel\u00e1neas de la m\u00e1quina", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_misc.setStatusTip(QCoreApplication.translate("MainWindow", u"Funciones miscel\u00e1neas de la m\u00e1quina", None))
#endif // QT_CONFIG(statustip)
        self.btn_misc.setText(QCoreApplication.translate("MainWindow", u"Funciones &M", None))
        self.groupBox_tool.setTitle(QCoreApplication.translate("MainWindow", u"Herramienta", None))
#if QT_CONFIG(tooltip)
        self.btn_tool_call.setToolTip(QCoreApplication.translate("MainWindow", u"Llama una herramienta guardada o colocada en la m\u00e1quina", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_tool_call.setStatusTip(QCoreApplication.translate("MainWindow", u"Llama una herramienta guardada o colocada en la m\u00e1quina", None))
#endif // QT_CONFIG(statustip)
        self.btn_tool_call.setText(QCoreApplication.translate("MainWindow", u"Llamar herramien&ta", None))
#if QT_CONFIG(tooltip)
        self.btn_tool_close.setToolTip(QCoreApplication.translate("MainWindow", u"Finaliza el uso de una herramienta en la m\u00e1quina", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_tool_close.setStatusTip(QCoreApplication.translate("MainWindow", u"Finaliza el uso de una herramienta en la m\u00e1quina", None))
#endif // QT_CONFIG(statustip)
        self.btn_tool_close.setText(QCoreApplication.translate("MainWindow", u"Cerrar &herramienta", None))
        self.groupBox_program.setTitle(QCoreApplication.translate("MainWindow", u"Programa", None))
#if QT_CONFIG(tooltip)
        self.btn_comment.setToolTip(QCoreApplication.translate("MainWindow", u"Agrega comentarios para facilitar la comprensi\u00f3n del programa", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_comment.setStatusTip(QCoreApplication.translate("MainWindow", u"Agrega comentarios para facilitar la comprensi\u00f3n del programa", None))
#endif // QT_CONFIG(statustip)
        self.btn_comment.setText(QCoreApplication.translate("MainWindow", u"&Comentario", None))
#if QT_CONFIG(tooltip)
        self.btn_header.setToolTip(QCoreApplication.translate("MainWindow", u"Agrega el encabezado del programa", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_header.setStatusTip(QCoreApplication.translate("MainWindow", u"Agrega el encabezado del programa", None))
#endif // QT_CONFIG(statustip)
        self.btn_header.setText(QCoreApplication.translate("MainWindow", u"&Iniciar programa", None))
#if QT_CONFIG(tooltip)
        self.btn_subrutine.setToolTip(QCoreApplication.translate("MainWindow", u"Llama la subrutina dentro del programa principal", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_subrutine.setStatusTip(QCoreApplication.translate("MainWindow", u"Llama la subrutina dentro del programa principal", None))
#endif // QT_CONFIG(statustip)
        self.btn_subrutine.setText(QCoreApplication.translate("MainWindow", u"Llamar s&ubrutina", None))
#if QT_CONFIG(tooltip)
        self.btn_end.setToolTip(QCoreApplication.translate("MainWindow", u"Agrega los comandos de finalizaci\u00f3n del programa", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_end.setStatusTip(QCoreApplication.translate("MainWindow", u"Agrega los comandos de finalizaci\u00f3n del programa", None))
#endif // QT_CONFIG(statustip)
        self.btn_end.setText(QCoreApplication.translate("MainWindow", u"&Finalizar programa", None))
#if QT_CONFIG(tooltip)
        self.btn_free.setToolTip(QCoreApplication.translate("MainWindow", u"Agrega un espacio en blanco en el programa", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_free.setStatusTip(QCoreApplication.translate("MainWindow", u"Agrega un espacio en blanco en el programa", None))
#endif // QT_CONFIG(statustip)
        self.btn_free.setText(QCoreApplication.translate("MainWindow", u"&Espacio", None))
#if QT_CONFIG(tooltip)
        self.btn_collect.setToolTip(QCoreApplication.translate("MainWindow", u"Activar el proceso de recolecci\u00f3n de la pieza", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_collect.setStatusTip(QCoreApplication.translate("MainWindow", u"Activar el proceso de recolecci\u00f3n de la pieza", None))
#endif // QT_CONFIG(statustip)
        self.btn_collect.setText(QCoreApplication.translate("MainWindow", u"Recolectar &Pieza", None))
        self.tabWidget_principal.setTabText(self.tabWidget_principal.indexOf(self.tabWidget_principal_functions), "")
        self.groupBox_turning.setTitle(QCoreApplication.translate("MainWindow", u"Torneado", None))
#if QT_CONFIG(tooltip)
        self.btn_lineal.setToolTip(QCoreApplication.translate("MainWindow", u"Realizar un movimiento lineal de mecanizado o posicionamiento para torneado", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_lineal.setStatusTip(QCoreApplication.translate("MainWindow", u"Realizar un movimiento lineal de mecanizado o posicionamiento para torneado", None))
#endif // QT_CONFIG(statustip)
        self.btn_lineal.setText(QCoreApplication.translate("MainWindow", u"Torneado lineal", None))
#if QT_CONFIG(tooltip)
        self.btn_radial.setToolTip(QCoreApplication.translate("MainWindow", u"Realizar un movimiento radial de mecanizado para torneado", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_radial.setStatusTip(QCoreApplication.translate("MainWindow", u"Realizar un movimiento radial de mecanizado para torneado", None))
#endif // QT_CONFIG(statustip)
        self.btn_radial.setText(QCoreApplication.translate("MainWindow", u"Torneado radial", None))
#if QT_CONFIG(tooltip)
        self.btn_thread.setToolTip(QCoreApplication.translate("MainWindow", u"Realizar un maquinado de roscado", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_thread.setStatusTip(QCoreApplication.translate("MainWindow", u"Realizar un maquinado de roscado", None))
#endif // QT_CONFIG(statustip)
        self.btn_thread.setText(QCoreApplication.translate("MainWindow", u"Roscado", None))
#if QT_CONFIG(tooltip)
        self.btn_cutoff.setToolTip(QCoreApplication.translate("MainWindow", u"Realizar un maquinado de tronzado", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_cutoff.setStatusTip(QCoreApplication.translate("MainWindow", u"Realizar un maquinado de tronzado", None))
#endif // QT_CONFIG(statustip)
        self.btn_cutoff.setText(QCoreApplication.translate("MainWindow", u"Tronzado", None))
        self.tabWidget_functions.setTabText(self.tabWidget_functions.indexOf(self.tabWidget_functions_turning), "")
        self.groupBox_milling.setTitle(QCoreApplication.translate("MainWindow", u"Fresado", None))
#if QT_CONFIG(tooltip)
        self.btn_mill_end.setToolTip(QCoreApplication.translate("MainWindow", u"Agrega los comandos de finalizaci\u00f3n para fresados", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_mill_end.setStatusTip(QCoreApplication.translate("MainWindow", u"Agrega los comandos de finalizaci\u00f3n para fresados", None))
#endif // QT_CONFIG(statustip)
        self.btn_mill_end.setText(QCoreApplication.translate("MainWindow", u"Finalizar Fresados", None))
#if QT_CONFIG(tooltip)
        self.btn_lineal_3.setToolTip(QCoreApplication.translate("MainWindow", u"Realizar un movimiento lineal de mecanizado o posicionamiento para fresado", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_lineal_3.setStatusTip(QCoreApplication.translate("MainWindow", u"Realizar un movimiento lineal de mecanizado o posicionamiento para fresado", None))
#endif // QT_CONFIG(statustip)
        self.btn_lineal_3.setText(QCoreApplication.translate("MainWindow", u"Fresado lineal", None))
#if QT_CONFIG(tooltip)
        self.btn_radial_3.setToolTip(QCoreApplication.translate("MainWindow", u"Realizar un movimiento radial de mecanizado para fresado", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_radial_3.setStatusTip(QCoreApplication.translate("MainWindow", u"Realizar un movimiento radial de mecanizado para fresado", None))
#endif // QT_CONFIG(statustip)
        self.btn_radial_3.setText(QCoreApplication.translate("MainWindow", u"Fresado radial", None))
#if QT_CONFIG(tooltip)
        self.btn_mill_ini.setToolTip(QCoreApplication.translate("MainWindow", u"Agrega los comandos de preparaci\u00f3n para fresados", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_mill_ini.setStatusTip(QCoreApplication.translate("MainWindow", u"Agrega los comandos de preparaci\u00f3n para fresados", None))
#endif // QT_CONFIG(statustip)
        self.btn_mill_ini.setText(QCoreApplication.translate("MainWindow", u"Iniciar Fresados", None))
        self.tabWidget_functions.setTabText(self.tabWidget_functions.indexOf(self.tabWidget_functions_milling), "")
        self.groupBox_mill_cycles.setTitle(QCoreApplication.translate("MainWindow", u"Ciclos de fresado", None))
#if QT_CONFIG(tooltip)
        self.btn_bevel.setToolTip(QCoreApplication.translate("MainWindow", u"Realizar un mecanizado de bisel", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_bevel.setStatusTip(QCoreApplication.translate("MainWindow", u"Realizar un mecanizado de bisel", None))
#endif // QT_CONFIG(statustip)
        self.btn_bevel.setText(QCoreApplication.translate("MainWindow", u"Bisel", None))
#if QT_CONFIG(tooltip)
        self.btn_facing.setToolTip(QCoreApplication.translate("MainWindow", u"Realizar un mecanizado de refrentado", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_facing.setStatusTip(QCoreApplication.translate("MainWindow", u"Realizar un mecanizado de refrentado", None))
#endif // QT_CONFIG(statustip)
        self.btn_facing.setText(QCoreApplication.translate("MainWindow", u"Refrentado", None))
#if QT_CONFIG(tooltip)
        self.btn_flat.setToolTip(QCoreApplication.translate("MainWindow", u"Realizar un mecanizado de palete", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_flat.setStatusTip(QCoreApplication.translate("MainWindow", u"Realizar un mecanizado de palete", None))
#endif // QT_CONFIG(statustip)
        self.btn_flat.setText(QCoreApplication.translate("MainWindow", u"Paleta", None))
#if QT_CONFIG(tooltip)
        self.btn_face.setToolTip(QCoreApplication.translate("MainWindow", u"Realizar un mecanizado de caras", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_face.setStatusTip(QCoreApplication.translate("MainWindow", u"Realizar un mecanizado de caras", None))
#endif // QT_CONFIG(statustip)
        self.btn_face.setText(QCoreApplication.translate("MainWindow", u"Caras", None))
#if QT_CONFIG(tooltip)
        self.btn_concaver.setToolTip(QCoreApplication.translate("MainWindow", u"Realizar un mecanizado de ch\u00f3cola", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_concaver.setStatusTip(QCoreApplication.translate("MainWindow", u"Realizar un mecanizado de ch\u00f3cola", None))
#endif // QT_CONFIG(statustip)
        self.btn_concaver.setText(QCoreApplication.translate("MainWindow", u"Ch\u00f3cola", None))
#if QT_CONFIG(tooltip)
        self.btn_slotting.setToolTip(QCoreApplication.translate("MainWindow", u"Realizar un mecanizado de ranurado", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_slotting.setStatusTip(QCoreApplication.translate("MainWindow", u"Realizar un mecanizado de ranurado", None))
#endif // QT_CONFIG(statustip)
        self.btn_slotting.setText(QCoreApplication.translate("MainWindow", u"Ranurado", None))
        self.tabWidget_functions.setTabText(self.tabWidget_functions.indexOf(self.tabWidget_functions_mill_cycles), "")
        self.groupBox_drilling.setTitle(QCoreApplication.translate("MainWindow", u"Perforado", None))
#if QT_CONFIG(tooltip)
        self.btn_csink.setToolTip(QCoreApplication.translate("MainWindow", u"Realizar un perforado de bisel (Counter sink)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_csink.setStatusTip(QCoreApplication.translate("MainWindow", u"Realizar un perforado de bisel (Counter sink)", None))
#endif // QT_CONFIG(statustip)
        self.btn_csink.setText(QCoreApplication.translate("MainWindow", u"C'Sink", None))
#if QT_CONFIG(tooltip)
        self.btn_drill.setToolTip(QCoreApplication.translate("MainWindow", u"Realizar un perforado de agujero en corte escalonado", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_drill.setStatusTip(QCoreApplication.translate("MainWindow", u"Realizar un perforado de agujero en corte escalonado", None))
#endif // QT_CONFIG(statustip)
        self.btn_drill.setText(QCoreApplication.translate("MainWindow", u"Perforado", None))
#if QT_CONFIG(tooltip)
        self.btn_drill_ini.setToolTip(QCoreApplication.translate("MainWindow", u"Agrega los comandos de preparaci\u00f3n para perforados", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_drill_ini.setStatusTip(QCoreApplication.translate("MainWindow", u"Agrega los comandos de preparaci\u00f3n para perforados", None))
#endif // QT_CONFIG(statustip)
        self.btn_drill_ini.setText(QCoreApplication.translate("MainWindow", u"Iniciar perforados", None))
#if QT_CONFIG(tooltip)
        self.btn_ream.setToolTip(QCoreApplication.translate("MainWindow", u"Realizar un perforado de alisado (rimado)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_ream.setStatusTip(QCoreApplication.translate("MainWindow", u"Realizar un perforado de alisado (rimado)", None))
#endif // QT_CONFIG(statustip)
        self.btn_ream.setText(QCoreApplication.translate("MainWindow", u"Rimado", None))
#if QT_CONFIG(tooltip)
        self.btn_drill_end.setToolTip(QCoreApplication.translate("MainWindow", u"Agrega los comandos de finalizaci\u00f3n para perforados", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_drill_end.setStatusTip(QCoreApplication.translate("MainWindow", u"Agrega los comandos de finalizaci\u00f3n para perforados", None))
#endif // QT_CONFIG(statustip)
        self.btn_drill_end.setText(QCoreApplication.translate("MainWindow", u"Finalizar perforados", None))
#if QT_CONFIG(tooltip)
        self.btn_center.setToolTip(QCoreApplication.translate("MainWindow", u"Realizar un perforado de agujero de centro", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_center.setStatusTip(QCoreApplication.translate("MainWindow", u"Realizar un perforado de agujero de centro", None))
#endif // QT_CONFIG(statustip)
        self.btn_center.setText(QCoreApplication.translate("MainWindow", u"Agujero centro", None))
        self.tabWidget_functions.setTabText(self.tabWidget_functions.indexOf(self.tabWidget_functions_drilling), "")
        self.groupBox_platter.setTitle(QCoreApplication.translate("MainWindow", u"Platina - Plato", None))
#if QT_CONFIG(tooltip)
        self.btn_call_square.setToolTip(QCoreApplication.translate("MainWindow", u"Agrega la matriz de piezas al programa principal", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_call_square.setStatusTip(QCoreApplication.translate("MainWindow", u"Agrega la matriz de piezas al programa principal", None))
#endif // QT_CONFIG(statustip)
        self.btn_call_square.setText(QCoreApplication.translate("MainWindow", u"Generar matriz", None))
#if QT_CONFIG(tooltip)
        self.btn_lineal_rgh_y.setToolTip(QCoreApplication.translate("MainWindow", u"Agrega el desbaste vertical a la subrutina", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_lineal_rgh_y.setStatusTip(QCoreApplication.translate("MainWindow", u"Agrega el desbaste vertical a la subrutina", None))
#endif // QT_CONFIG(statustip)
        self.btn_lineal_rgh_y.setText(QCoreApplication.translate("MainWindow", u"Sub vertical", None))
#if QT_CONFIG(tooltip)
        self.btn_flatten.setToolTip(QCoreApplication.translate("MainWindow", u"Agrega el refrentado de platina a la subrutina", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_flatten.setStatusTip(QCoreApplication.translate("MainWindow", u"Agrega el refrentado de platina a la subrutina", None))
#endif // QT_CONFIG(statustip)
        self.btn_flatten.setText(QCoreApplication.translate("MainWindow", u"Sub refrentado", None))
#if QT_CONFIG(tooltip)
        self.btn_call_lineal_y.setToolTip(QCoreApplication.translate("MainWindow", u"Agrega el desbaste vertical al programa principal", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_call_lineal_y.setStatusTip(QCoreApplication.translate("MainWindow", u"Agrega el desbaste vertical al programa principal", None))
#endif // QT_CONFIG(statustip)
        self.btn_call_lineal_y.setText(QCoreApplication.translate("MainWindow", u"Desbaste vertical", None))
#if QT_CONFIG(tooltip)
        self.btn_call_lineal_x.setToolTip(QCoreApplication.translate("MainWindow", u"Agrega el desbaste horizontal al programa principal", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_call_lineal_x.setStatusTip(QCoreApplication.translate("MainWindow", u"Agrega el desbaste horizontal al programa principal", None))
#endif // QT_CONFIG(statustip)
        self.btn_call_lineal_x.setText(QCoreApplication.translate("MainWindow", u"Desbaste horizontal", None))
#if QT_CONFIG(tooltip)
        self.btn_call_flatten.setToolTip(QCoreApplication.translate("MainWindow", u"Agrega el refrentado de platina al programa principal", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_call_flatten.setStatusTip(QCoreApplication.translate("MainWindow", u"Agrega el refrentado de platina al programa principal", None))
#endif // QT_CONFIG(statustip)
        self.btn_call_flatten.setText(QCoreApplication.translate("MainWindow", u"Refrenta platina", None))
#if QT_CONFIG(tooltip)
        self.btn_lineal_rgh_x.setToolTip(QCoreApplication.translate("MainWindow", u"Agrega el desbaste horizontal a la subrutina", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_lineal_rgh_x.setStatusTip(QCoreApplication.translate("MainWindow", u"Agrega el desbaste horizontal a la subrutina", None))
#endif // QT_CONFIG(statustip)
        self.btn_lineal_rgh_x.setText(QCoreApplication.translate("MainWindow", u"Sub horizontal", None))
#if QT_CONFIG(tooltip)
        self.btn_platter_data.setToolTip(QCoreApplication.translate("MainWindow", u"Agrega los datos de la matriz de piezas", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_platter_data.setStatusTip(QCoreApplication.translate("MainWindow", u"Agrega los datos de la matriz de piezas", None))
#endif // QT_CONFIG(statustip)
        self.btn_platter_data.setText(QCoreApplication.translate("MainWindow", u"Datos matriz", None))
        self.tabWidget_functions.setTabText(self.tabWidget_functions.indexOf(self.tabWidget_functions_platter), "")
    # retranslateUi

