#!/usr/bin/env python3
"""YF — 元风跟单王 ERP Discord Bot with LLM brain.

Bilingual (CN/EN) product manager persona for YF ERP.
Powered by opencode-go or compatible OpenAI API.
"""

import os
import sys
import logging
import aiohttp
import discord
from discord.ext import commands

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s %(message)s",
)
log = logging.getLogger(__name__)

TOKEN = os.getenv("DISCORD_BOT_TOKEN", "")
LLM_API_KEY = os.getenv("MINIMAX_CN_API_KEY", "")
LLM_BASE_URL = os.getenv("LLM_BASE_URL", "https://api.minimax.chat/v1/text/chatcompletion_v2")
LLM_MODEL = os.getenv("LLM_MODEL", "MiniMax-M3")
ALLOWED_USERS = os.getenv("ALLOWED_USERS", "")

assert TOKEN, "DISCORD_BOT_TOKEN not set"
assert LLM_API_KEY, "MINIMAX_CN_API_KEY not set"

ALLOWED_IDS = [uid.strip() for uid in ALLOWED_USERS.split(",") if uid.strip()]

SYSTEM_PROMPT = """你叫 YF (元风) — 元风跟单王 ERP 的产品经理。

PERSONA:
- 你是经验丰富的制造业 ERP 产品经理，专精于跟单（订单跟踪）系统
- 说人话，不拽术语。能用中文说清楚就不用英文
- 对比尔的主人 Markus（马库斯）说话要直白，他是你的 PM/老板
- 在对订单数据的问题上，你是认真的——一个订单错了可能就是几千块的损失
- 中英双语是你的默认模式。工厂工人看中文，管理层看英文

关于 YF ERP（元风跟单王）：
- 基于 Django/Python 的订单跟踪 ERP 系统
- 以 Windows EXE（ERP_Server_Tray_vX.X.X.X.exe）形式分发
- 用户双击 EXE 启动，浏览器访问 localhost:8080 使用
- 支持远程访问：Cloudflare Tunnel → yf.harwav.com
- 功能包括：订单管理、生产跟踪（自产/外协）、报表统计、用户角色权限
- JWT API 认证，支持外部系统集成
- 双语界面（简体中文 + 英文）

CORE VALUES:
- 订单数据必须准确，错误的订单号码、重量、状态会给用户造成实际的业务损失
- 系统升级不能破坏现有数据——用户直接运行新 EXE 就能升级，不需要手动迁移
- 这是一个 Windows 桌面产品，不是 SaaS。用户双击 EXE 就能用
- 中文英文同等重要

BEHAVIOR RULES:
- 回答关于 YF ERP 的问题：功能、版本、部署、配置
- 讨论版本发布计划、Bug 优先级、新功能规划
- 不要编造具体的版本号或发布日期——看 CHANGELOG
- 如果你不确定，老实说不知道
- 不要泄露任何 API Key、Token、或凭据
- 跟 Markus 说话时，可以中英混搭，但不要装逼

You are YF — the Product Manager for 元风跟单王 ERP (YF ERP System).

PERSONA:
- Experienced manufacturing ERP product manager, specializing in order tracking systems
- Speak plainly, not with jargon
- Direct and honest with Markus (your PM/boss)
- Dead serious about order data accuracy — wrong data costs real money
- Bilingual by default: Chinese for factory workers, English for management

ABOUT YF ERP:
- Django/Python-based order tracking ERP
- Ships as Windows EXE (ERP_Server_Tray_vX.X.X.X.exe)
- Users double-click the EXE, access via browser at localhost:8080
- Remote access via Cloudflare Tunnel → yf.harwav.com
- Features: order management, production tracking (in-house/outsourced), reports, role-based access
- JWT API authentication
- Bilingual UI (Simplified Chinese + English)

CORE VALUES:
- Order data must never be wrong
- Upgrades must never break existing data
- Windows EXE is the product, not SaaS
- Both languages matter equally

BEHAVIOR RULES:
- Answer questions about YF ERP features, versions, deployment, configuration
- Discuss release plans, bug prioritization, feature scoping
- Don't make up specific version numbers or dates
- If unsure, say so honestly
- Never reveal API keys, tokens, or credentials
- Bilingual is normal: mix CN and EN naturally"""

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="yf!", intents=intents, help_command=None)


async def llm_chat(messages: list[dict]) -> str | None:
    """Call LLM and return response text."""
    url = f"{LLM_BASE_URL}/chat/completions"
    headers = {
        "Authorization": f"Bearer {LLM_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": LLM_MODEL,
        "messages": messages,
        "max_tokens": 512,
        "temperature": 0.7,
    }
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(
                url, headers=headers, json=payload,
                timeout=aiohttp.ClientTimeout(total=30)
            ) as resp:
                if resp.status != 200:
                    text = await resp.text()
                    log.error(f"LLM API error {resp.status}: {text[:200]}")
                    return None
                data = await resp.json()
                return data["choices"][0]["message"]["content"]
        except Exception as e:
            log.error(f"LLM call failed: {e}")
            return None


@bot.event
async def on_ready():
    log.info(f"YF bot logged in as {bot.user}")
    log.info(f"Bot is in {len(bot.guilds)} guilds:")
    for g in bot.guilds:
        log.info(f"  - {g.name} (id: {g.id})")
    log.info(f"Intents: message_content={intents.message_content}")


@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    # Only respond to DMs or when mentioned, unless it's an allowed user
    is_dm = isinstance(message.channel, discord.DMChannel)
    is_mentioned = bot.user in message.mentions
    is_allowed = str(message.author.id) in ALLOWED_IDS

    if not is_dm and not is_mentioned:
        await bot.process_commands(message)
        return

    if not is_allowed and not is_dm:
        await bot.process_commands(message)
        return

    content = message.content.strip()
    uid = bot.user.id if bot.user else ""
    for mention in [f"<@{uid}>", f"<@!{uid}>"]:
        content = content.replace(mention, "").strip()

    if not content:
        content = "你好 / Hello"

    log.info(f"Processing message from {message.author}: {content[:80]}")

    # Show typing indicator while LLM processes
    async with message.channel.typing():
        # Try LLM first
        llm_messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": content},
        ]
        response = await llm_chat(llm_messages)

        if response:
            await message.channel.send(response[:1900])
        else:
            fallback = get_fallback_response(content)
            await message.channel.send(fallback)


def get_fallback_response(content: str) -> str:
    """Offline fallback when LLM is unreachable."""
    c = content.lower()
    if any(w in c for w in ["hi", "hello", "halo", "嗨", "你好", "hello"]):
        return (
            "你好！我是 YF，元风跟单王 ERP 的产品经理 👋\n"
            "LLM brain is taking a nap. Try again later!"
        )
    if any(w in c for w in ["版本", "version", "release", "更新", "changelog"]):
        return (
            "最新的版本发布信息在 https://github.com/Harwav/YF_ERP_Releases/releases\n"
            "CHANGELOG 也在那个 repo 里。"
        )
    if any(w in c for w in ["部署", "install", "安装"]):
        return (
            "下载最新 ERP_Server_Tray_vX.X.X.X.exe → 双击运行 → "
            "浏览器打开 http://localhost:8080\n"
            "就是这么简单。"
        )
    return (
        "YF here 🤙 Bot brain offline. "
        "Check releases at https://github.com/Harwav/YF_ERP_Releases\n"
        "有问题直接找 Markus。"
    )


@bot.command(name="about")
async def cmd_about(ctx: commands.Context):
    await ctx.send(
        "**YF** — 元风跟单王 ERP 产品经理 🤖\n"
        "Windows 订单跟踪系统 | Django/Python | yf.harwav.com\n"
        "Repo: https://github.com/Harwav/YF_ERP_Releases"
    )


@bot.command(name="help")
async def cmd_help(ctx: commands.Context):
    await ctx.send(
        "**YF Bot** — DM or @ me in channel.\n"
        "`yf!about` — What's YF?\n"
        "`yf!help` — This\n"
        "`yf!version` — Latest release\n\n"
        "Ask me anything about YF ERP! 有什么问题随便问！"
    )


@bot.command(name="version")
async def cmd_version(ctx: commands.Context):
    await ctx.send(
        "📦 Latest release: https://github.com/Harwav/YF_ERP_Releases/releases\n"
        "Check CHANGELOG for details."
    )


if __name__ == "__main__":
    bot.run(TOKEN, log_handler=None)
