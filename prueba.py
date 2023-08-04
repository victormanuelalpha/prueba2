print('Hello, Word')
print(f'prueba de commit')
#git config --global user.name 'jedua285'
#git config --global user.email 'jose.campuzano@alphanetworks.mx'
#git config --global core.editor 'code .'
#git init
#git remote add origin https://github.com/victormanuelalpha/prueba2.git
#git remote -v
#fetch
#git pull origin main
#en la de archivos
#git branch
#git branch -m lalo jedua
"""
    Servicio Social@DESKTOP-CB0CEO5 MINGW64 ~/Documents/Jose Eduardo/git (jedua)
$ git status
On branch jedua
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   hola_mundo.py
        new file:   prueba.txt


Servicio Social@DESKTOP-CB0CEO5 MINGW64 ~/Documents/Jose Eduardo/git (jedua)
$ git branch
* jedua
  main

Servicio Social@DESKTOP-CB0CEO5 MINGW64 ~/Documents/Jose Eduardo/git (jedua)
$ git branch -r
  origin/jedua
  origin/main

Servicio Social@DESKTOP-CB0CEO5 MINGW64 ~/Documents/Jose Eduardo/git (jedua)
$ git remote add origin https://github.com/victormanuelalpha/prueba2.git
error: remote origin already exists.

Servicio Social@DESKTOP-CB0CEO5 MINGW64 ~/Documents/Jose Eduardo/git (jedua)
$ git init
Reinitialized existing Git repository in C:/Users/Servicio Social/Documents/Jose Eduardo/git/.git/

Servicio Social@DESKTOP-CB0CEO5 MINGW64 ~/Documents/Jose Eduardo/git (jedua)
$ git remote -v
origin  https://github.com/victormanuelalpha/prueba2.git (fetch)
origin  https://github.com/victormanuelalpha/prueba2.git (push)

Servicio Social@DESKTOP-CB0CEO5 MINGW64 ~/Documents/Jose Eduardo/git (jedua)
$ git pull origin main
From https://github.com/victormanuelalpha/prueba2
 * branch            main       -> FETCH_HEAD
Already up to date.

Servicio Social@DESKTOP-CB0CEO5 MINGW64 ~/Documents/Jose Eduardo/git (jedua)
$ git branch
* jedua
  main

Servicio Social@DESKTOP-CB0CEO5 MINGW64 ~/Documents/Jose Eduardo/git (jedua)
$ git branch -r
  origin/jedua
  origin/main

Servicio Social@DESKTOP-CB0CEO5 MINGW64 ~/Documents/Jose Eduardo/git (jedua)
$ git pull origin main
From https://github.com/victormanuelalpha/prueba2
 * branch            main       -> FETCH_HEAD
Already up to date.

Servicio Social@DESKTOP-CB0CEO5 MINGW64 ~/Documents/Jose Eduardo/git (jedua)
$ git status
On branch jedua
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   hola_mundo.py
        new file:   prueba.txt


Servicio Social@DESKTOP-CB0CEO5 MINGW64 ~/Documents/Jose Eduardo/git (jedua)
$ git commit -m "archivo subido desde branch jedua"
[jedua 99a7936] archivo subido desde branch jedua
 2 files changed, 16 insertions(+)
 create mode 100644 hola_mundo.py
 create mode 100644 prueba.txt

Servicio Social@DESKTOP-CB0CEO5 MINGW64 ~/Documents/Jose Eduardo/git (jedua)
$ git status
On branch jedua
nothing to commit, working tree clean

Servicio Social@DESKTOP-CB0CEO5 MINGW64 ~/Documents/Jose Eduardo/git (jedua)
$ git push origin jedua
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 575 bytes | 575.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/victormanuelalpha/prueba2.git
   0c22eae..99a7936  jedua -> jedua

Servicio Social@DESKTOP-CB0CEO5 MINGW64 ~/Documents/Jose Eduardo/git (jedua)
$ git checkout main
Switched to branch 'main'

Servicio Social@DESKTOP-CB0CEO5 MINGW64 ~/Documents/Jose Eduardo/git (main)
$ git fetch
remote: Enumerating objects: 21, done.
remote: Counting objects: 100% (21/21), done.
remote: Compressing objects: 100% (9/9), done.
remote: Total 19 (delta 6), reused 18 (delta 5), pack-reused 0
Unpacking objects: 100% (19/19), 1.80 KiB | 1024 bytes/s, done.
From https://github.com/victormanuelalpha/prueba2
 * [new branch]      Alex       -> origin/Alex
 * [new branch]      leo        -> origin/leo
 * [new branch]      mafer      -> origin/mafer
 * [new branch]      victor     -> origin/victor
 * [new branch]      xolo       -> origin/xolo

Servicio Social@DESKTOP-CB0CEO5 MINGW64 ~/Documents/Jose Eduardo/git (main)
$ git branch -a
  jedua
* main
  remotes/origin/Alex
  remotes/origin/jedua
  remotes/origin/leo
  remotes/origin/mafer
  remotes/origin/main
  remotes/origin/victor
  remotes/origin/xolo

Servicio Social@DESKTOP-CB0CEO5 MINGW64 ~/Documents/Jose Eduardo/git (main)

"""

"""
    git checkout Alex
    git log  //para ver la ruta
    git pull origin xolo
    git fetch
"""

print('prueba de rama')