#!/usr/bin/env python3
"""Print each connected gamepad as SDL sees it: <guid><TAB><name>.

Run inside the box (system SDL2, which is sdl2-compat over SDL3 on Arch) so
the GUID matches what Dolphin, Cemu and Azahar record. Used by the verify
role to check dg_controller_sdl_guid/name; handy to fill those in by hand:

    distrobox enter gaming -- python3 -I scripts/sdl-pad-ids.py
"""
import ctypes
import sys

SDL_INIT_JOYSTICK = 0x200
SDL_INIT_GAMECONTROLLER = 0x2000


class SDLGuid(ctypes.Structure):
    _fields_ = [("data", ctypes.c_uint8 * 16)]


def main() -> int:
    try:
        sdl = ctypes.CDLL("libSDL2-2.0.so.0")
    except OSError as exc:
        print(f"libSDL2 not found: {exc}", file=sys.stderr)
        return 2
    if sdl.SDL_Init(SDL_INIT_JOYSTICK | SDL_INIT_GAMECONTROLLER) != 0:
        print("SDL_Init failed", file=sys.stderr)
        return 2
    sdl.SDL_JoystickNameForIndex.restype = ctypes.c_char_p
    sdl.SDL_JoystickGetDeviceGUID.restype = SDLGuid
    for index in range(sdl.SDL_NumJoysticks()):
        buf = ctypes.create_string_buffer(33)
        sdl.SDL_JoystickGetGUIDString(sdl.SDL_JoystickGetDeviceGUID(index), buf, 33)
        name = (sdl.SDL_JoystickNameForIndex(index) or b"").decode(errors="replace")
        print(f"{buf.value.decode()}\t{name}")
    sdl.SDL_Quit()
    return 0


if __name__ == "__main__":
    sys.exit(main())
