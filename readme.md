# pinentry-kphttp

A gnupg pinentry program, which automatically retrieves the key from KeePass/KeePassX/KeePassXC using the KeePassHTTP-Protocol.

## Requirements
  * KeePass/KeePassX/KeePassXC
  * KeePassHTTP

## Setup
  * Add the following URL to your Gnupg-password in keepass:

        https://gnupg.org

  * Add pinentry-kphttp to /home/<youruser>/bin
  * edit ~/.gnupg/gpg-agent.conf and add your path:

        pinentry-program /home/<youruser>/bin/pinentry-gtk-2

On first use KeePass will ask you to allow the application to access your passwords.
