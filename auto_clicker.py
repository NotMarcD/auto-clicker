import pyautogui as autoclick

## roblox auto clicker script

def auto_click() :
    while True:
        autoclick.click(clicks=2)


def double_click() :
    autoclick.doubleClick()
    return


if __name__ == "__main__":
    autoclick.click(clicks=2, interval=1.0)