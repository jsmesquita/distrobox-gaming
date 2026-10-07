# Replicar a instalação em outra máquina

Guia passo a passo para recriar este setup (box `gaming`, emuladores,
ES-DE, atalhos) numa máquina nova. Testado num host **Ubuntu 26.04**; o box
é sempre Arch, independente do host. Detalhes técnicos de hosts não-Arch
estão em [`rebuild-runbook.md`](rebuild-runbook.md#non-arch-hosts-eg-ubuntu).

## Visão geral

O repo recria **todo o software e as configurações**. O que é seu e não está
no git precisa ser levado à parte:

| Item | Onde fica | Vai pelo repo? |
|---|---|---|
| Emuladores, cores do RetroArch, configs, ES-DE, atalhos, ícones | gerados pelo playbook | **Sim** |
| `ansible/host_vars/localhost.yml` (caminhos, UID/GID, resolução) | no repo, mas no `.gitignore` | Não — guarde uma cópia |
| ROMs e BIOS | `<dg_emudeck_root>/roms*` (quatro pastas) e `<dg_emudeck_root>/Emulation/bios` — veja [`pastas-e-roms.md`](pastas-e-roms.md) | Não |
| Saves | dentro do box (`~/Games/distrobox/gaming`) e no backup em `<dg_external_games_root>/distrobox-gaming/backup/saves` | Não |
| Capas/vídeos do scraper do ES-DE | `~/Games/distrobox/gaming/ES-DE/downloaded_media` | Não |
| Jogos da Steam | biblioteca da Steam | Não — baixe de novo |

## Antes: na máquina antiga

1. Faça backup dos saves:

   ```sh
   ~/Games/distrobox/gaming/bin/backup-saves
   ```

   Ele copia para `dg_backup_root`, por padrão
   `<dg_external_games_root>/distrobox-gaming/backup/saves` (nesta máquina,
   `~/Games/library/distrobox-gaming/backup/saves`).

2. Copie para um disco externo ou para a nuvem:
   - `ansible/host_vars/localhost.yml`
   - a pasta da biblioteca (`~/Games/library`: ROMs, BIOS e o backup dos saves)
   - opcional: `~/Games/distrobox/gaming/ES-DE/downloaded_media`, para não
     precisar rodar o scraper de novo

> **Atalho:** se a máquina nova tiver o mesmo usuário e os mesmos caminhos,
> basta copiar a pasta `~/Games` inteira. O playbook recria o container e
> reaproveita o que já estiver lá (saves, mídia, configs).

## Na máquina nova

### 1. Pré-requisitos do host

```sh
sudo apt install git curl podman distrobox ansible python-is-python3
ansible-galaxy collection install community.general
```

`python-is-python3` é necessário porque o `check_host` exige o comando
`python`. As ferramentas de extração (`bsdtar`, `7z`, `unrar`...) são
instaladas automaticamente pelo playbook no passo 5.

### 2. Clonar o repo

```sh
git clone https://github.com/jsmesquita/distrobox-gaming.git ~/distrobox-gaming
```

### 3. Configurar a máquina

Coloque a cópia do `localhost.yml` em `~/distrobox-gaming/ansible/host_vars/`.
Sem cópia, parta do modelo:

```sh
cd ~/distrobox-gaming/ansible
cp host_vars/localhost.yml.example host_vars/localhost.yml
```

Revise o arquivo para a máquina nova:

- `dg_host_uid` / `dg_host_gid`: saída de `id -u` / `id -g`.
- `dg_data_root`, `dg_external_games_root`: onde ficam o box e a biblioteca.
- `dg_sorr_host_gamescope_opts`: resolução da tela (`-W 1920 -H 1080`).

### 4. Copiar ROMs, BIOS e saves

Copie a biblioteca para o caminho configurado em `dg_external_games_root`
(por exemplo `~/Games/library`), mantendo a estrutura do `EmuDeck/`
(`roms/`, `roms_mid/`, `roms_heavy/`, `roms_rare/` e `Emulation/bios/`).
O mais simples é copiar a pasta `EmuDeck/` inteira. A pasta de cada sistema
está em [`pastas-e-roms.md`](pastas-e-roms.md).

### 5. Rodar o setup completo

Rode **num terminal de verdade** (não pelo `!` do Claude Code — o Ansible
recusa stdio não bloqueante) e com `-K`, porque a primeira execução usa sudo
para instalar ferramentas do host:

```sh
cd ~/distrobox-gaming/ansible
ansible-playbook site.yml -K
```

Isso valida o host, instala as ferramentas que faltam, cria o box Arch,
instala os emuladores e os cores do RetroArch, aplica as configurações
(incluindo tela cheia no RetroArch), registra os sistemas no ES-DE e instala
os atalhos com ícones no menu de aplicativos. A primeira execução demora;
as seguintes só mudam o que for necessário e não precisam de `-K`.

Se um download falhar (o buildbot do RetroArch às vezes fica instável),
basta rodar o mesmo comando de novo: o que já foi baixado é reaproveitado.

### 6. Restaurar os saves

Com o backup no caminho de `dg_backup_root`:

```sh
ansible-playbook restore-saves.yml
```

### 7. Instalar os opcionais que você usa

Os extras ficam fora do setup padrão; cada um tem seu playbook
(`ansible/install-*.yml`). Exemplos:

```sh
ansible-playbook install-azahar.yml   # emulador de 3DS
ansible-playbook install-xenia.yml    # Xbox 360
ansible-playbook install-sorr.yml     # Streets of Rage Remake
```

Lista completa: `ls ansible/install-*.yml` e a seção *Opt-in roles* do README.

### 8. Conferir

```sh
ansible-playbook site.yml --tags verify
```

O `verify` confirma, entre outros, que o UID/GID do box bate com o host e que
todo core do RetroArch usado pelo ES-DE está instalado. BIOS e firmware
ausentes geram só avisos.

### 9. Últimos ajustes

- Abra o **ES-DE** pelo menu de aplicativos. Se copiou o `downloaded_media`,
  as capas já aparecem; senão, rode *Menu → Scraper*.
- Abra a **Steam** do box, faça login e baixe os jogos.
- Se algum ícone aparecer genérico no menu, saia e entre de novo na sessão.

## Depois de instalado

Veja [`uso-diario.md`](uso-diario.md) para o uso no dia a dia. Resumo: não é
preciso rodar nada ao ligar a máquina, porque os atalhos ligam o box sozinhos.
Rode o repo só quando:

| Situação | Comando |
|---|---|
| Atualizou o repo (`git pull`) | `ansible-playbook site.yml` |
| Bagunçou a config de um emulador | `ansible-playbook reset-configs.yml` |
| Atualizar os pacotes do box | `distrobox enter gaming -- yay -Syu` |
| Backup dos saves | `~/Games/distrobox/gaming/bin/backup-saves` |
