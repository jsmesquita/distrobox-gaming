# Como funciona depois de instalado

A instalação deste repo acontece **uma única vez** por máquina (veja
[`replicar-instalacao.md`](replicar-instalacao.md)). Depois disso, o setup
funciona sozinho: não é preciso rodar nada do repo no dia a dia, nem ao
ligar a máquina.

## Reiniciar ou desligar a máquina

Pode reiniciar ou desligar à vontade; nada se perde e nada precisa ser
refeito.

- **O box `gaming` é um container podman.** Ao desligar, ele só para; não é
  apagado. Tudo o que foi instalado continua lá.
- **Os atalhos ligam o box sozinhos.** Cada atalho do menu (ES-DE, Steam,
  emuladores) roda via `distrobox-enter`, que liga o container se ele
  estiver parado. A primeira abertura depois de ligar a máquina leva alguns
  segundos a mais; as seguintes são normais.
- **Configs, saves, emuladores e cores ficam em disco**, na pasta do box
  (`~/Games/distrobox/gaming`) e no menu do host (`~/.local/share`). Não há
  serviço que precise estar rodando nem nada que precise ser reaplicado no
  boot.

## Jogar

1. Abra o **ES-DE** pelo menu de aplicativos (Show Apps).
2. Escolha o sistema e o jogo. O ES-DE abre o emulador certo, em tela
   cheia, e volta para a lista quando o jogo fecha.

Os outros atalhos (Dolphin, PCSX2, RetroArch...) abrem o emulador sozinho.
Use quando precisar mexer nas opções dele, como mapear um controle.

## Adicionar jogos

1. Copie a ROM para `~/Games/library/EmuDeck/roms/<sistema>/` (por exemplo
   `mame/`, `snes/`, `ps2/`).
2. No ES-DE, atualize a lista (*Menu → Game Collection Settings → Update
   Gamelists*) ou reinicie o ES-DE.
3. Opcional: rode o *Scraper* para baixar capas e vídeos.

ROMs de arcade (MAME) ficam compactadas: deixe o `.zip` com o nome original
do romset, sem descompactar.

## Quando rodar algo do repo

Só nestes casos. Todos os comandos rodam de `~/distrobox-gaming/ansible`, e
rodar de novo nunca estraga nada: o playbook só muda o que for necessário.

| Situação | Comando |
|---|---|
| Bagunçou a configuração de um emulador | `ansible-playbook reset-configs.yml` |
| Quer instalar um extra (3DS, Xbox 360, jogo de PC...) | `ansible-playbook install-<nome>.yml` |
| Atualizou o repo (`git pull`) | `ansible-playbook site.yml` |
| Quer conferir se está tudo certo | `ansible-playbook site.yml --tags verify` |
| Máquina nova ou formatada | siga [`replicar-instalacao.md`](replicar-instalacao.md) |

## Atualizações

Nada se atualiza sozinho, e isso é proposital: o que funciona hoje continua
funcionando. Para atualizar quando quiser:

- **Pacotes do box (emuladores do Arch):**
  `distrobox enter gaming -- yay -Syu`
- **Cores do RetroArch:** no RetroArch, *Online Updater → Update Installed
  Cores*.
- **shadPS4:** `ansible-playbook refresh-shadps4.yml`

## Saves

O backup dos saves **não é automático**. Rode de vez em quando, e sempre
antes de mexer em algo arriscado:

```sh
~/Games/distrobox/gaming/bin/backup-saves
```

O backup vai para `dg_backup_root` (nesta máquina,
`~/Games/library/distrobox-gaming/backup/saves`). Como fica no mesmo disco,
copie essa pasta para um disco externo ou para a nuvem se quiser proteção
contra perda do disco. Para restaurar: `~/Games/distrobox/gaming/bin/restore-saves`.
Mais detalhes em [`save-backups.md`](save-backups.md).

## Se algo der errado

- **Um jogo não abre pelo ES-DE:** o motivo fica no fim do log,
  `~/Games/distrobox/gaming/ES-DE/logs/es_log.txt`.
- **Um core do RetroArch está faltando:**
  `ansible-playbook site.yml --tags retroarch`.
- **Um ícone aparece genérico no menu:** saia e entre de novo na sessão.
- **Um emulador ficou com configuração estranha:**
  `ansible-playbook reset-configs.yml`. Há backup automático dos arquivos
  alterados.
