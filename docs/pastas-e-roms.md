# Pastas dos emuladores e como adicionar ROMs

Onde colocar os jogos de cada sistema, quais formatos cada pasta aceita e
onde ficam BIOS e firmware.

## Onde fica a biblioteca

Todas as pastas abaixo ficam dentro da raiz `dg_emudeck_root`, definida no
`ansible/host_vars/localhost.yml`. Nesta máquina:

```
/home/jefferson/Games/library/EmuDeck/
├── roms/          sistemas leves (cartuchos, arcade, PS1, Saturn)
├── roms_mid/      sistemas médios (Dreamcast, PSP, N64, DS, Sega CD)
├── roms_heavy/    sistemas pesados (PS2, PS3, GameCube, Wii, Switch, Xbox)
├── roms_rare/     arcade especial (Sega Model 1/2/3, NAOMI) e PS4
└── Emulation/bios BIOS e firmware
```

A divisão em quatro pastas vem do layout do EmuDeck, e serve para colocar
cada grupo num disco diferente se quiser (veja *Mudar as pastas de lugar*).
**Cada sistema tem uma pasta fixa**: uma ROM na pasta errada não aparece no
ES-DE.

## Pasta de cada sistema

Caminhos relativos a `/home/jefferson/Games/library/`. A coluna *Emulador*
mostra o padrão; alguns sistemas têm alternativas, que o ES-DE oferece por
jogo (*Menu do jogo → Edit this game's metadata → Alternative emulator*).

| Sistema | Pasta | Formatos aceitos | Emulador |
|---|---|---|---|
| Nintendo Switch | `EmuDeck/roms_heavy/switch/` | .nca .nro .nso .nsp .xci | Eden |
| Sony PlayStation | `EmuDeck/roms/psx/` | .bin .cbn .ccd .chd .cue .ecm .exe .img .iso .m3u .mdf .mds .minipsf .pbp .psexe .psf .toc .z .znx .7z .zip | DuckStation |
| Sony PlayStation 2 | `EmuDeck/roms_heavy/ps2/` | .bin .chd .ciso .cso .dump .elf .gz .m3u .mdf .img .iso .isz .ngr .nrg .zso | PCSX2 |
| Sega Dreamcast | `EmuDeck/roms_mid/dreamcast/` | .cdi .chd .cue .dat .elf .gdi .iso .lst .m3u .7z .zip | Flycast |
| Nintendo GameCube | `EmuDeck/roms_heavy/gc/` | .ciso .dff .dol .elf .gcm .gcz .iso .json .m3u .rvz .tgc .wad .wbfs .wia .7z .zip | Dolphin |
| Nintendo Wii | `EmuDeck/roms_heavy/wii/` | .ciso .dff .dol .elf .gcm .gcz .iso .json .m3u .rvz .tgc .wad .wbfs .wia .7z .zip | Dolphin |
| Sony PlayStation Portable | `EmuDeck/roms_mid/psp/` | .chd .cso .elf .iso .pbp .prx .7z .zip | PPSSPP |
| Sony PlayStation 3 | `EmuDeck/roms_heavy/ps3/` | .ps3 | RPCS3 |
| Sony PlayStation 4 | `EmuDeck/roms_rare/ps4/` | .bin | shadPS4 |
| Microsoft Xbox | `EmuDeck/roms_heavy/xbox/` | .iso .xiso | xemu |
| Nintendo 3DS | `EmuDeck/roms_heavy/n3ds/` | .3ds .cci .cxi .app .elf .cia .3dsx | Azahar |
| Microsoft Xbox 360 | `EmuDeck/roms_heavy/xbox360/` | .iso .xex .xbla | Xenia Canary (per-game config) |
| Sega Model 2 | `EmuDeck/roms_rare/model2/` | .zip | Model 2 Emulator (Wine) |
| Sega Model 1 | `EmuDeck/roms_rare/model1/` | .zip | Model 1 dispatcher (Wine/MAME) |
| Sega Model 3 | `EmuDeck/roms_rare/model3/` | .zip | Supermodel |
| Sega NAOMI | `EmuDeck/roms_rare/naomi/` | .zip .7z | Flycast |
| Sega NAOMI 2 | `EmuDeck/roms_rare/naomi2/` | .zip .7z | Flycast |
| Nintendo Entertainment System | `EmuDeck/roms/nes/` | .nes .fds .unif .unf .zip .7z | Mesen (RetroArch) |
| Super Nintendo Entertainment System | `EmuDeck/roms/snes/` | .smc .sfc .swc .fig .bs .st .7z .zip | Auto bsnes/bsnes-hd (RetroArch) |
| Nintendo Game Boy | `EmuDeck/roms/gb/` | .gb .7z .zip | Gambatte (RetroArch) |
| Nintendo Game Boy Color | `EmuDeck/roms/gbc/` | .gbc .gb .7z .zip | Gambatte (RetroArch) |
| Nintendo Game Boy Advance | `EmuDeck/roms/gba/` | .gba .7z .zip | mGBA (RetroArch) |
| Nintendo DS | `EmuDeck/roms_mid/nds/` | .nds .zip .7z | melonDS |
| Nintendo 64 | `EmuDeck/roms_mid/n64/` | .n64 .v64 .z64 .ndd .zip .7z | Mupen64Plus-Next (RetroArch) |
| Sega Master System | `EmuDeck/roms/mastersystem/` | .sms .7z .zip | Genesis Plus GX (RetroArch) |
| Sega Genesis / Mega Drive | `EmuDeck/roms/genesis/` | .smd .md .bin .gen .7z .zip | Genesis Plus GX (RetroArch) |
| Sega Game Gear | `EmuDeck/roms/gamegear/` | .gg .7z .zip | Genesis Plus GX (RetroArch) |
| Sega 32X | `EmuDeck/roms/sega32x/` | .32x .smd .md .bin .7z .zip | PicoDrive (RetroArch) |
| Sega CD / Mega CD | `EmuDeck/roms_mid/megacd/` | .cue .chd .iso .ccd .m3u .7z .zip | Genesis Plus GX (RetroArch) |
| Sega Saturn | `EmuDeck/roms/saturn/` | .cue .chd .iso .ccd .mds .m3u .7z .zip | Beetle Saturn (RetroArch) |
| SNK Neo Geo AES / MVS | `EmuDeck/roms/neogeo/` | .zip .7z | FB Neo (RetroArch) |
| Capcom Play System | `EmuDeck/roms/cps/` | .zip .7z | FB Neo (RetroArch) |
| Capcom Play System II | `EmuDeck/roms/cps2/` | .zip .7z | FB Neo (RetroArch) |
| Arcade (MAME) | `EmuDeck/roms/mame/` | .zip .7z | MAME (RetroArch) |
| Atari 2600 (opcional) | `EmuDeck/roms/atari2600/` | .a26 .bin .rom .zip .7z | Stella (RetroArch) |
| Atari 5200 (opcional) | `EmuDeck/roms/atari5200/` | .a52 .bin .car .rom .zip .7z | Atari800 (RetroArch) |
| Atari 7800 ProSystem (opcional) | `EmuDeck/roms/atari7800/` | .a78 .bin .zip .7z | ProSystem (RetroArch) |
| Atari Lynx (opcional) | `EmuDeck/roms/atarilynx/` | .lnx .o .zip .7z | Handy (RetroArch) |
| Atari 800 (opcional) | `EmuDeck/roms/atari800/` | .atr .bas .bin .car .cas .dcm .xex .xfd .zip .7z | Atari800 (RetroArch) |
| Atari ST (opcional) | `EmuDeck/roms/atarist/` | .st .stx .msa .dim .ipf .zip | Hatari (RetroArch) |
| OpenBOR Game Engine | `EmuDeck/roms_mid/openbor/` | .pak | OpenBOR |

Sistemas marcados *(opcional)* só aparecem no ES-DE depois de ligados no
`localhost.yml`: `dg_atari_enabled: true` para os Atari 8 bits/Lynx e
`dg_atari_st_enabled: true` para o Atari ST (veja `docs/atari.md` e
`docs/atari-st.md`).

Jogos de PC, ports e fan games não usam essas pastas: cada um é instalado
pelo seu `install-*.yml` e aparece sozinho no sistema **Ports** do ES-DE.

## Como adicionar ROMs

1. **Crie a pasta do sistema**, se ainda não existir. Use exatamente o nome
   da tabela:

   ```sh
   mkdir -p ~/Games/library/EmuDeck/roms_mid/n64
   ```

2. **Copie a ROM** para a pasta, num dos formatos aceitos.

3. **Atualize a lista no ES-DE**: *Menu → Game Collection Settings →
   Update Gamelists*, ou feche e abra o ES-DE. O sistema aparece no ES-DE
   quando a pasta dele tem pelo menos um jogo.

4. **Opcional: baixe capas e vídeos** com *Menu → Scraper*.

### Cuidados por tipo de jogo

- **Arcade (MAME, FB Neo, NAOMI, Sega Model):** **não descompacte**. Cada
  jogo é um `.zip` com o nome curto do romset (por exemplo `ssriders.zip`),
  e o emulador identifica o jogo por esse nome. O romset precisa ser da
  versão que o emulador espera; para o MAME do RetroArch, um romset atual.
- **Neo Geo:** o BIOS `neogeo.zip` vai **junto com os jogos**, na pasta
  `roms/neogeo/`.
- **Jogos de vários discos (PS1, Saturn, Sega CD, Dreamcast):** crie um
  arquivo `.m3u` listando os discos, um por linha, e deixe os discos numa
  subpasta. O ES-DE mostra só o `.m3u`, e a troca de disco funciona dentro do
  jogo.
- **Formatos compactados:** prefira `.chd` para jogos de CD/DVD (PS1, PS2,
  Saturn, Sega CD, Dreamcast) e `.rvz` para GameCube/Wii; ocupam bem menos
  espaço e rodam igual.
- **PS3:** cada jogo é uma **pasta** extraída com o nome terminando em
  `.ps3`, por exemplo `roms_heavy/ps3/Gran Turismo 5 (BCUS98114).ps3/`.
  Detalhes e conversão de `.iso` em `docs/ps3-library.md`.
- **PS4:** cada jogo é uma pasta extraída com o ID do título
  (`roms_rare/ps4/CUSA00003/`, com o `eboot.bin` dentro), não o `.pkg`.
- **Xbox 360:** depois de colocar novos `.iso` em `roms_heavy/xbox360/`,
  rode `ansible-playbook install-xenia.yml` para o Xenia Manager registrar
  os jogos (veja `docs/xenia-manager.md`).

## BIOS e firmware

Vários sistemas precisam de BIOS, que não vem com os emuladores. Coloque os
arquivos em `/home/jefferson/Games/library/EmuDeck/Emulation/bios/`
(`dg_bios_root`). Rode `ansible-playbook site.yml --tags configure` depois
de adicionar BIOS novas, para o repo criar os links.

| Sistema | O que fazer |
|---|---|
| PlayStation (DuckStation) | BIOS em `Emulation/bios/` (ex.: `scph5501.bin`). O DuckStation já procura lá. |
| Nintendo DS (melonDS) | `bios7.bin`, `bios9.bin`, `dsfirmware.bin` em `Emulation/bios/`. O repo copia para o melonDS. |
| NAOMI / NAOMI 2 / Atomiswave (Flycast) | `naomi.zip`, `naomi2.zip`, `awbios.zip` em `Emulation/bios/dc/`. O repo cria os links no Flycast; sem eles os jogos não bootam. |
| Dreamcast (Flycast) | Opcional: o Flycast tem BIOS embutida (HLE). Para usar a BIOS real, coloque `dc_boot.bin` e `dc_flash.bin` na pasta de dados do Flycast, `~/Games/distrobox/gaming/.local/share/flycast/`. |
| Xbox (xemu) | `mcpx_1.0.bin`, `Complex_4627.bin` e `xbox_hdd.qcow2` em `Emulation/bios/`. |
| PS4 (shadPS4) | Módulos do firmware em `roms_rare/ps4-firmware/11.00_sys_modules/`. |
| Atari (opcional) | `5200.ROM`, `ATARIXL.ROM`, `ATARIBAS.ROM`, `ATARIOSA.ROM`, `ATARIOSB.ROM`, `lynxboot.img` e `tos.img` em `Emulation/bios/`; todos opcionais exceto o `tos.img` do Atari ST. |
| PlayStation 2 (PCSX2) | Na primeira abertura do PCSX2, o assistente pede a pasta das BIOS: aponte para `Emulation/bios/`. |
| PlayStation 3 (RPCS3) | Abra o RPCS3 pelo menu e use *File → Install Firmware* com o `PS3UPDAT.PUP` da Sony. |
| Switch (Eden) | Abra o Eden pelo menu e instale suas `prod.keys` e o firmware pelas opções do próprio Eden. |
| Saturn, Sega CD (RetroArch) | BIOS na pasta de sistema do RetroArch, `~/Games/distrobox/gaming/.config/retroarch/system/` (ex.: `sega_101.bin`, `mpr-17933.bin` para Saturn; `bios_CD_U.bin` para Sega CD). |

O `ansible-playbook site.yml --tags verify` avisa sobre BIOS que faltam sem
falhar, então dá para adicionar as BIOS aos poucos.

## Mudar as pastas de lugar

Para usar outro disco ou outra estrutura, edite o
`ansible/host_vars/localhost.yml` e rode `ansible-playbook site.yml` de novo.
O playbook regenera as pastas no ES-DE e nos emuladores. As variáveis
principais:

| Variável | Padrão | Controla |
|---|---|---|
| `dg_emudeck_root` | `<dg_external_games_root>/EmuDeck` | Raiz de tudo abaixo |
| `dg_rom_root` | `<dg_emudeck_root>/roms` | Pasta `roms/` |
| `dg_rom_mid_root` | `<dg_emudeck_root>/roms_mid` | Pasta `roms_mid/` |
| `dg_rom_heavy_root` | `<dg_emudeck_root>/roms_heavy` | Pasta `roms_heavy/` |
| `dg_rom_rare_root` | `<dg_emudeck_root>/roms_rare` | Pasta `roms_rare/` |
| `dg_bios_root` | `<dg_emudeck_root>/Emulation/bios` | BIOS e firmware |

O repo só lê essas pastas e cria links para elas; ele nunca apaga nem move
ROMs, BIOS ou saves.
