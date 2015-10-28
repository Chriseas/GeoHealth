# -*- coding: utf-8 -*-
"""
/***************************************************************************

                                 GeoHealth
                                 A QGIS plugin

                              -------------------
        begin                : 2014-08-20
        copyright            : (C) 2014 by Etienne Trimaille
        email                : etienne@trimaille.eu
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4.QtCore import QFileInfo
from qgis.core import QgsMapLayerRegistry, QgsRasterLayer, QgsProviderRegistry

from PyQt4.QtGui import QWidget, QDialogButtonBox, QFileDialog

from GeoHealth.ui.import_ui.open_raster import Ui_Form
from GeoHealth.core.tools import trans


class OpenRasterWidget(QWidget, Ui_Form):

    def __init__(self, parent=None):
        self.parent = parent
        super(OpenRasterWidget, self).__init__()
        self.setupUi(self)

        self.buttonBox.button(QDialogButtonBox.Open).clicked.connect(
            self.open_raster)
        # noinspection PyUnresolvedReferences
        self.bt_browse.clicked.connect(self.open_file_browser)

    def open_file_browser(self):

        # noinspection PyArgumentList
        raster_filter = QgsProviderRegistry.instance().fileRasterFilters()

        # noinspection PyArgumentList
        raster = QFileDialog.getOpenFileName(
            parent=self.parent,
            caption=trans('Select raster'),
            filter=raster_filter)
        self.le_shapefile.setText(raster)

    def open_raster(self):
        path = self.le_shapefile.text()

        file_info = QFileInfo(path)
        layer = QgsRasterLayer(path, file_info.baseName())

        # noinspection PyArgumentList
        QgsMapLayerRegistry.instance().addMapLayer(layer)
