from pyrogram.types import InlineKeyboardButton

import config
from VIPMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="нєℓρ", callback_data="settings_back_helper"),
            InlineKeyboardButton(
                text="ѕєт", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="gʀσυρ", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="gʀσυρ", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="мσʀє", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text="fʀєαтυʀєѕ", callback_data="settings_back_helper")
        ],
    ]
    return buttons
