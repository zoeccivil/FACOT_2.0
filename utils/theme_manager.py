"""
Gestor de temas para FACOT.

Proporciona soporte para múltiples temas visuales:
- light: Tema claro por defecto
- dark: Tema oscuro
- midnight: Tema oscuro azulado
- coral: Tema cálido
- high_contrast: Alto contraste para accesibilidad
"""

from __future__ import annotations
from typing import Dict, Optional, Any

# Importar PyQt6 solo si está disponible (para tests sin GUI)
try:
    from PyQt6.QtWidgets import QApplication
    _HAS_PYQT6 = True
except ImportError:
    QApplication = None  # type: ignore
    _HAS_PYQT6 = False


# Definición de temas disponibles
THEMES: Dict[str, Dict[str, str]] = {
    "light": {
        "name": "Claro",
        "description": "Tema claro por defecto",
        "background": "#ffffff",
        "foreground": "#333333",
        "primary": "#2196f3",
        "secondary": "#757575",
        "accent": "#ff9800",
        "success": "#4caf50",
        "warning": "#ff9800",
        "error": "#f44336",
        "surface": "#f5f5f5",
        "border": "#e0e0e0",
    },
    "dark": {
        "name": "Oscuro",
        "description": "Tema oscuro",
        "background": "#1e1e1e",
        "foreground": "#e0e0e0",
        "primary": "#64b5f6",
        "secondary": "#b0bec5",
        "accent": "#ffb74d",
        "success": "#81c784",
        "warning": "#ffb74d",
        "error": "#e57373",
        "surface": "#2d2d2d",
        "border": "#404040",
    },
    "midnight": {
        "name": "Medianoche",
        "description": "Tema oscuro azulado",
        "background": "#0d1b2a",
        "foreground": "#e0e0e0",
        "primary": "#48cae4",
        "secondary": "#90caf9",
        "accent": "#f9c74f",
        "success": "#80ed99",
        "warning": "#ffd166",
        "error": "#ef476f",
        "surface": "#1b263b",
        "border": "#2a3f5f",
    },
    "coral": {
        "name": "Coral",
        "description": "Tema cálido",
        "background": "#fff8f0",
        "foreground": "#3d3d3d",
        "primary": "#ff6b6b",
        "secondary": "#845ec2",
        "accent": "#ffc75f",
        "success": "#4caf50",
        "warning": "#ff9800",
        "error": "#d63031",
        "surface": "#fff0e6",
        "border": "#ffd9c4",
    },
    "high_contrast": {
        "name": "Alto Contraste",
        "description": "Tema de alto contraste para accesibilidad",
        "background": "#000000",
        "foreground": "#ffffff",
        "primary": "#00ff00",
        "secondary": "#ffff00",
        "accent": "#00ffff",
        "success": "#00ff00",
        "warning": "#ffff00",
        "error": "#ff0000",
        "surface": "#1a1a1a",
        "border": "#ffffff",
    },
}


def get_available_themes() -> Dict[str, str]:
    """
    Obtiene los temas disponibles.
    
    Returns:
        Dict con {theme_id: nombre_display}
    """
    return {key: val["name"] for key, val in THEMES.items()}


def get_theme_colors(theme_id: str) -> Dict[str, str]:
    """
    Obtiene los colores de un tema.
    
    Args:
        theme_id: ID del tema
    
    Returns:
        Dict con los colores del tema
    """
    return THEMES.get(theme_id, THEMES["light"])


def generate_stylesheet(theme_id: str) -> str:
    """
    Genera la hoja de estilos (QSS) para un tema.
    
    Args:
        theme_id: ID del tema
    
    Returns:
        String con el QSS generado
    """
    colors = get_theme_colors(theme_id)
    
    qss = f"""
    /* Tema: {colors.get('name', theme_id)} */
    
    QMainWindow, QDialog, QWidget {{
        background-color: {colors['background']};
        color: {colors['foreground']};
    }}
    
    QLabel {{
        color: {colors['foreground']};
    }}
    
    QPushButton {{
        background-color: {colors['primary']};
        color: white;
        border: none;
        padding: 8px 16px;
        border-radius: 4px;
        font-weight: bold;
    }}
    
    QPushButton:hover {{
        background-color: {colors['accent']};
    }}
    
    QPushButton:pressed {{
        background-color: {colors['secondary']};
    }}
    
    QPushButton:disabled {{
        background-color: {colors['border']};
        color: {colors['secondary']};
    }}
    
    QLineEdit, QTextEdit, QPlainTextEdit, QSpinBox, QDoubleSpinBox {{
        background-color: {colors['surface']};
        color: {colors['foreground']};
        border: 1px solid {colors['border']};
        border-radius: 4px;
        padding: 6px;
    }}
    
    QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus {{
        border-color: {colors['primary']};
    }}
    
    QComboBox {{
        background-color: {colors['surface']};
        color: {colors['foreground']};
        border: 1px solid {colors['border']};
        border-radius: 4px;
        padding: 6px;
    }}
    
    QComboBox:hover {{
        border-color: {colors['primary']};
    }}
    
    QComboBox QAbstractItemView {{
        background-color: {colors['surface']};
        color: {colors['foreground']};
        selection-background-color: {colors['primary']};
        selection-color: white;
    }}
    
    QTableWidget, QTableView {{
        background-color: {colors['surface']};
        color: {colors['foreground']};
        gridline-color: {colors['border']};
        selection-background-color: {colors['primary']};
        selection-color: white;
        alternate-background-color: {colors['background']};
    }}
    
    QTableWidget::item, QTableView::item {{
        padding: 5px;
    }}
    
    QHeaderView::section {{
        background-color: {colors['surface']};
        color: {colors['foreground']};
        border: 1px solid {colors['border']};
        padding: 5px;
        font-weight: bold;
    }}
    
    QTabWidget::pane {{
        border: 1px solid {colors['border']};
        background-color: {colors['background']};
    }}
    
    QTabBar::tab {{
        background-color: {colors['surface']};
        color: {colors['foreground']};
        padding: 8px 16px;
        border: 1px solid {colors['border']};
        border-bottom: none;
        border-top-left-radius: 4px;
        border-top-right-radius: 4px;
    }}
    
    QTabBar::tab:selected {{
        background-color: {colors['background']};
        border-bottom: 2px solid {colors['primary']};
    }}
    
    QTabBar::tab:hover {{
        background-color: {colors['primary']};
        color: white;
    }}
    
    QMenuBar {{
        background-color: {colors['surface']};
        color: {colors['foreground']};
    }}
    
    QMenuBar::item {{
        padding: 5px 10px;
    }}
    
    QMenuBar::item:selected {{
        background-color: {colors['primary']};
        color: white;
    }}
    
    QMenu {{
        background-color: {colors['surface']};
        color: {colors['foreground']};
        border: 1px solid {colors['border']};
    }}
    
    QMenu::item {{
        padding: 5px 25px;
    }}
    
    QMenu::item:selected {{
        background-color: {colors['primary']};
        color: white;
    }}
    
    QGroupBox {{
        border: 1px solid {colors['border']};
        border-radius: 4px;
        margin-top: 10px;
        padding-top: 10px;
    }}
    
    QGroupBox::title {{
        color: {colors['foreground']};
        subcontrol-origin: margin;
        left: 10px;
        padding: 0 5px;
    }}
    
    QScrollBar:vertical {{
        background-color: {colors['surface']};
        width: 12px;
        border-radius: 6px;
    }}
    
    QScrollBar::handle:vertical {{
        background-color: {colors['border']};
        border-radius: 6px;
        min-height: 20px;
    }}
    
    QScrollBar::handle:vertical:hover {{
        background-color: {colors['primary']};
    }}
    
    QScrollBar:horizontal {{
        background-color: {colors['surface']};
        height: 12px;
        border-radius: 6px;
    }}
    
    QScrollBar::handle:horizontal {{
        background-color: {colors['border']};
        border-radius: 6px;
        min-width: 20px;
    }}
    
    QScrollBar::handle:horizontal:hover {{
        background-color: {colors['primary']};
    }}
    
    QStatusBar {{
        background-color: {colors['surface']};
        color: {colors['foreground']};
    }}
    
    QToolTip {{
        background-color: {colors['surface']};
        color: {colors['foreground']};
        border: 1px solid {colors['border']};
        padding: 5px;
    }}
    
    QCheckBox {{
        color: {colors['foreground']};
    }}
    
    QCheckBox::indicator {{
        width: 18px;
        height: 18px;
    }}
    
    QRadioButton {{
        color: {colors['foreground']};
    }}
    
    QDateEdit {{
        background-color: {colors['surface']};
        color: {colors['foreground']};
        border: 1px solid {colors['border']};
        border-radius: 4px;
        padding: 6px;
    }}
    
    QProgressBar {{
        background-color: {colors['surface']};
        border: 1px solid {colors['border']};
        border-radius: 4px;
        text-align: center;
    }}
    
    QProgressBar::chunk {{
        background-color: {colors['primary']};
        border-radius: 3px;
    }}
    """
    
    return qss


def apply_theme(app: Any, theme_id: str) -> bool:
    """
    Aplica un tema a la aplicación.
    
    Args:
        app: Instancia de QApplication
        theme_id: ID del tema a aplicar
    
    Returns:
        True si se aplicó correctamente
    """
    if not _HAS_PYQT6:
        print("[THEME] PyQt6 no disponible, no se puede aplicar tema")
        return False
    
    if not app:
        return False
    
    if theme_id not in THEMES:
        print(f"[THEME] Tema '{theme_id}' no encontrado, usando 'light'")
        theme_id = "light"
    
    try:
        stylesheet = generate_stylesheet(theme_id)
        app.setStyleSheet(stylesheet)
        print(f"[THEME] Tema '{theme_id}' aplicado correctamente")
        return True
    except Exception as e:
        print(f"[THEME] Error aplicando tema: {e}")
        return False


def load_saved_theme(app: Any) -> str:
    """
    Carga y aplica el tema guardado en la configuración.
    
    Args:
        app: Instancia de QApplication
    
    Returns:
        ID del tema aplicado
    """
    try:
        import facot_config
        theme_id = facot_config.get_theme()
    except Exception:
        theme_id = "light"
    
    apply_theme(app, theme_id)
    return theme_id


class ThemeManager:
    """
    Gestor singleton de temas.
    
    Proporciona una interfaz centralizada para gestionar temas.
    """
    
    _instance: Optional['ThemeManager'] = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self._current_theme = "light"
        self._app: Any = None
    
    def set_app(self, app: Any):
        """Establece la instancia de QApplication."""
        self._app = app
    
    def get_current_theme(self) -> str:
        """Obtiene el tema actual."""
        return self._current_theme
    
    def apply_theme(self, theme_id: str) -> bool:
        """
        Aplica un tema.
        
        Args:
            theme_id: ID del tema
        
        Returns:
            True si se aplicó correctamente
        """
        if _HAS_PYQT6 and QApplication is not None:
            app = self._app or QApplication.instance()
        else:
            app = self._app
            
        if apply_theme(app, theme_id):
            self._current_theme = theme_id
            return True
        return False
    
    def save_and_apply_theme(self, theme_id: str) -> bool:
        """
        Aplica un tema y lo guarda en la configuración.
        
        Args:
            theme_id: ID del tema
        
        Returns:
            True si se aplicó y guardó correctamente
        """
        if self.apply_theme(theme_id):
            try:
                import facot_config
                facot_config.set_theme(theme_id)
                return True
            except Exception as e:
                print(f"[THEME] Error guardando tema: {e}")
        return False
    
    def load_saved_theme(self) -> str:
        """Carga y aplica el tema guardado."""
        try:
            import facot_config
            theme_id = facot_config.get_theme()
        except Exception:
            theme_id = "light"
        
        self.apply_theme(theme_id)
        return theme_id


# Instancia global
_theme_manager: Optional[ThemeManager] = None


def get_theme_manager() -> ThemeManager:
    """Obtiene la instancia global del gestor de temas."""
    global _theme_manager
    if _theme_manager is None:
        _theme_manager = ThemeManager()
    return _theme_manager
