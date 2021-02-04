#coding:UTF-8
import discord
from discord.ext import tasks
from datetime import datetime 

TOKEN = "ODA2NDEyMTY5NTcwNTQ5NzYx.YBpD2w.GyZx-URzJcFiR-BjdKlGIBeSTTE" #トークン
CHANNEL_ID = 757143658612129825 #チャンネルID

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の日付
    now_d = datetime.now().strftime('%A')
    if now_d == 'Friday':
    # 現在の時刻
    now_t = datetime.now().strftime('%H:%M')
    if now_t == '21:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('いよいよ楽しい週末の始まりです！！ せっかくですしゲームしませんか？！')  

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
