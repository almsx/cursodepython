# Notas Importantes

* Instalación de Python:
        * url: http://www.python.org/

* Agregar Python al path de Windows:
        * url: https://www.youtube.com/watch?v=1-j5FZrX4gg

* Instalación de SSH y GPG keys en Windows
	* url: https://www.redeszone.net/windows/freesshd-para-windows-instalacion-y-manual-de-configuracion-de-freesshd-para-windows-servidor-ssh-y-sftp/

        * url: https://www.youtube.com/watch?v=-0ubjfEKJPA

* GitLab
        * url:
        https://about.gitlab.com/

* Instalación de GTK en macOS

Paso 1

brew install pygobject3 --with-python3 gtk+3

Paso 2
brew install pygobject pygobject3

Paso 3
mkdir -p "$HOME/Library/Python/2.7/lib/python/site-packages”

Paso 4
echo  'import site; site.addsitedir("/usr/local/lib/python2.7/site-packages")' >> "$HOME/Library/Python/2.7/lib/python/site-packages/homebrew.pth”
