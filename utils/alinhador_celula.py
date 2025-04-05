from PySide6.QtWidgets import QStyledItemDelegate
from PySide6.QtGui import QFontMetrics
from PySide6.QtCore import Qt

class ElidedItemDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        option.displayAlignment = Qt.AlignLeft | Qt.AlignVCenter  
        option.textElideMode = Qt.ElideRight  
