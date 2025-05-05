import threading
from helpers import clear, adjustment_thread, help_menu, SettingThreadArgs, CameraThreadArgs, camera_thread, clear_console
from image_handler import Img
from font_utils import AsciiFont


def main():
    img = Img()
    setting_args = SettingThreadArgs()
    font = AsciiFont("consola.ttf", size=28)
    setting_args.currentImg = img
    cam_args = CameraThreadArgs(img, setting_args)

    threading.Thread(target=adjustment_thread, args=(setting_args,), daemon=True).start()
    threading.Thread(target=camera_thread, args=(cam_args,), daemon=True).start()

    help_menu()
    while setting_args.status:
        if setting_args.pressedKey == 'h':
            clear_console()
            help_menu()
            setting_args.pressedKey = None
        clear()
        print(font.render_ascii(img))
    clear_console()


if __name__ == "__main__":
    main()
