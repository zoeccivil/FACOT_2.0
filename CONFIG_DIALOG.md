# Diálogo de Configuración de Firebase

## Descripción

El diálogo de configuración de Firebase permite a los usuarios configurar las credenciales de Firebase sin necesidad de editar archivos de configuración manualmente.

## Cuándo Aparece

El diálogo aparece automáticamente en las siguientes situaciones:

1. **Primer inicio**: Si no se detectan credenciales de Firebase configuradas
2. **Credenciales inválidas**: Si las credenciales existentes no son válidas
3. **Manualmente**: Desde Configuración > "🔥 Configurar Firebase"

## Campos del Diálogo

### Archivo de Credenciales (JSON)

- **Descripción**: Ruta al archivo JSON de Service Account de Firebase
- **Cómo obtenerlo**:
  1. Ir a [Firebase Console](https://console.firebase.google.com/)
  2. Seleccionar tu proyecto
  3. Ir a Configuración > Service accounts
  4. Click en "Generate new private key"
  5. Guardar el archivo descargado

### Bucket de Storage

- **Descripción**: Nombre del bucket de Firebase Storage
- **Formato**: `{project-id}.firebasestorage.app`
- **Auto-completado**: Se completa automáticamente al seleccionar credenciales

## Funciones Disponibles

### 📂 Seleccionar...

Abre un diálogo para elegir el archivo JSON de credenciales.

Al seleccionar un archivo válido:
- Se extrae automáticamente el `project_id`
- Se sugiere el bucket de storage
- Se muestra información del proyecto

### 🔍 Validar conexión

Verifica que las credenciales sean válidas sin guardarlas.

Comprueba:
- El archivo es un JSON válido
- Es de tipo "service_account"
- Contiene los campos requeridos (`project_id`, `private_key`, `client_email`)

### 💾 Guardar y conectar

- Guarda la configuración en `facot_config.json`
- Cierra el diálogo
- La aplicación intentará conectar con Firebase

## Almacenamiento de Configuración

La configuración se guarda en `facot_config.json`:

```json
{
  "firebase": {
    "credentials_path": "/ruta/al/archivo/credenciales.json",
    "storage_bucket": "mi-proyecto.firebasestorage.app"
  }
}
```

**Nota**: El archivo `facot_config.json` está en `.gitignore` para evitar subir rutas locales al repositorio.

## Seguridad

### Credenciales Protegidas

- **NUNCA** se loguea el contenido de las credenciales
- Solo se muestra la ruta del archivo
- El archivo de credenciales debe tener permisos restrictivos

### Archivos a Proteger

Los siguientes archivos contienen información sensible y están en `.gitignore`:

```
firebase-credentials.json
*-firebase-adminsdk-*.json
service-account*.json
facot_config.json
.env
```

## Uso Programático

### Mostrar el Diálogo

```python
from dialogs.firebase_config_dialog import show_firebase_config_dialog

# Mostrar diálogo
if show_firebase_config_dialog(parent=self):
    print("Configuración guardada")
else:
    print("Usuario canceló")
```

### Acceder a la Configuración

```python
import facot_config

# Leer configuración
cred_path, bucket = facot_config.get_firebase_config()

# Guardar configuración
facot_config.set_firebase_config(
    credentials_path="/path/to/creds.json",
    storage_bucket="project.firebasestorage.app"
)
```

## Orden de Búsqueda de Credenciales

Cuando Firebase se inicializa, busca credenciales en este orden:

1. Configuración guardada en `facot_config.json`
2. Variable de entorno `FIREBASE_CREDENTIALS`
3. Variable de entorno `FIREBASE_CREDENTIALS_PATH`
4. Variable de entorno `GOOGLE_APPLICATION_CREDENTIALS`
5. Archivo `firebase-credentials.json` en el directorio actual
6. Archivo `firebase-credentials.json` en `%APPDATA%\FACOT` (Windows)

Si ninguna fuente tiene credenciales válidas, se abre el diálogo.

## Solución de Problemas

### "El archivo no es un JSON válido"

- Verificar que el archivo no esté corrupto
- Asegurarse de que sea el archivo descargado de Firebase (no editado)

### "Tipo de credencial inválido"

- El archivo debe ser de tipo "service_account"
- Descargar nuevas credenciales desde Firebase Console

### "Credenciales incompletas"

Campos requeridos:
- `type`: debe ser "service_account"
- `project_id`: ID del proyecto Firebase
- `private_key`: Clave privada RSA
- `client_email`: Email del service account

### El diálogo aparece repetidamente

- Verificar que la ruta guardada es accesible
- Comprobar permisos de lectura del archivo
- Verificar que `facot_config.json` se puede escribir
