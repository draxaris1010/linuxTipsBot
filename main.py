#!/usr/bin/env python3
from flask import Flask, request, jsonify

from telegram_bot import TelegramBot
from config import TELEGRAM_INIT_WEBHOOK_URL
print("Hello world!");
