Servidor virtual para poder desplegar en la nube, con una cuota fija y sin necesidad de utilizar un servicio en concreto.

# Cosas a tener en cuenta
 - Cercanía: Mientras más cerca de los usuarios finales, mejor.
 - Sistema operativo: Usar Linux y LTS.
 - Seguridad contra malware.
 - Usuario root: Contraseña y SSH.

### **Recomendaciones**
Actualizar: `apt update && apt upgrade -y`

Nvm: Sea a través del github `https://github.com/nvm-sh/nvm`
o con este comando:`curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash`
Cerrar y abrir la terminal o ejecutar el comando que recomienda.
`nvm install -lts`

Crear carpeta para el proyecto y clonar el repositorio y hacer el `npm install && npm run build && npm start` 
Mantener procesos: `npm install pm2 -g`
Instalar nginx como reverse proxy | Con Hostinger -> Sistema operativo -> Dokploy
## **Tutorial**:
![Video tutorial Midu - VPS Hostinger](https://youtu.be/kwVNpfru6pk?si=okDlb47-JiZu9WGq)