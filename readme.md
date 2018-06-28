# pinentry-kphttp

A gnupg pinentry program, which automatically retrieves the key from KeePass/KeePassX/KeePassXC using the KeePassHTTP-Protocol.

**Status:** experimental/unstable

## Requirements
  * KeePass/KeePassX/KeePassXC
  * KeePassHTTP

## TODOs
  * [ ] Show error if KeePass is not started
  * [ ] GTK GUI
    * [ ] Pinentry info: set window info if triggered by the assuan pipe
    * [ ] User input
      * [x] Select which "PIN" to use with a button
      * [ ] Select to add a new PIN with email-address & password/pin
      * [ ] Select to type it, but not to save it in keepass(e.g. if using a smartcard)

## Setup
  * Add the following URL to your Gnupg-password in keepass:

        https://gnupg.org

  * Add pinentry-kphttp to /home/<youruser>/bin
  * edit ~/.gnupg/gpg-agent.conf and add your path:

        pinentry-program /home/<youruser>/bin/pinentry-gtk-2

On first use KeePass will ask you to allow the application to access your passwords.
