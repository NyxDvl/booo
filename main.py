# ============================================================
#         iMLKq Community Bot - Full Professional Build
#         Powered By [ Xiy_y ]
# ============================================================

import discord
from discord.ext import commands, tasks
import asyncio
import json
import os
import random
import datetime
import re
import io
import aiohttp
from datetime import timezone, timedelta

# ============================================================
#                      الإعدادات العامة
# ============================================================
TOKEN = os.getenv("DISCORD_TOKEN") or "ضع_التوكن_هنا"

WELCOME_CHANNEL_ID = 808764166802374716
APP_PANEL_CHANNEL_ID = 1337804280836391016
APP_CONTROL_CHANNEL_ID = 1553162059292876892
GIVEAWAY_CHANNEL_ID = 1374379670652452884
BOOST_CHANNEL_ID = 1337462631191150663
TICKET_PANEL_CHANNEL_ID = 808382081843462145
TICKET_LOG_CHANNEL_ID = 1553150267661492234
JAIL_PANEL_CHANNEL_ID = 1529521201586770101
JAIL_LOG_CHANNEL_ID = 1529521204501942524
TICKET_ACTION_LOG_CHANNEL_ID = 1207040657483374642

REPOSTER_CHANNELS = [
    1362590778492321934,
    1529306986188116038,
    1296937483077943296,
    1374380125314879529,
    1374377922609283206,
    1374382361084432415,
]

APP_TARGET_CHANNELS = {
    "event": 1503053543215464558,
    "staff": 1474171233586380881,
    "lady":  1501924691173048360,
    "dev":   1503053396679069757,
}
ACCEPT_ROLES = {
    "event": [1529341838706872430, 1374342163332071444],
    "staff": [1358225686313173072, 1374335775122128976],
    "lady":  [1501930942988685403],
    "dev":   [1374340587578327050],
}
WINNER_ROLE_ID = 1529299390089527460
SECTION_NAMES = {
    "event": "Event Team",
    "staff": "Staff Team",
    "lady":  "Lady Submit",
    "dev":   "Developer Team",
}

TICKET_TYPES = {
    "high_staff":   {"label": "الإدارة العليا", "role_id": 1337456055952736329, "prefix": "high-staff"},
    "event_support":{"label": "دعم الإيفنت",   "role_id": 1374342163332071444, "prefix": "event"},
    "tech_support": {"label": "الدعم الفني",   "role_id": 1358225686313173072, "prefix": "tech"},
    "kick_support": {"label": "الدعم بالكيك",  "role_id": 1337740933290004520, "prefix": "kick"},
}

GENERAL_STAFF_ROLE_ID = 1358225686313173072
TICKET_CATEGORY_ID = 808382030051934238
JAIL_ROLE_ID = 1529521195115090020
REACTION_EMOJI_ID = 1512917096336588851

# ===== الصور =====
WELCOME_BANNER = "https://i.postimg.cc/2SrwstDz/i-MLKq.png"
THUMBNAIL = "https://i.postimg.cc/j2B0jbRQ/S-(1).png"
DIVIDER_IMAGE = "https://i.postimg.cc/nrmZBzRQ/5e91e5033ad6bd61.png"
BOOST_BANNER = "https://i.postimg.cc/3whyRMRH/image.png"
APP_PANEL_IMAGE = "https://i.postimg.cc/0Nkgjrd7/dhdh.png"
CONTROL_PANEL_IMAGE = "https://i.postimg.cc/fWBVR0c2/knknknk.png"
TICKET_PANEL_IMAGE = "https://i.postimg.cc/ZqPkGzmS/image.png"
TICKET_INSIDE_IMAGE = "https://i.postimg.cc/4dKw8TQn/tytyt.png"
TICKET_ADMIN_OPTIONS_IMAGE = "https://i.postimg.cc/c1wPZQfB/sfsh.png"
TICKET_SUCCESS_IMAGE = "https://i.postimg.cc/WhwkPIM/copyright-success.png"
POWERED_BY_IMAGE = "https://i.postimg.cc/G3XG4fFP/ʿbdalsmd-alqrshy.jpg"
JAIL_PANEL_IMAGE = "https://i.postimg.cc/jqzTSVyg/kkkk.png"
GIVEAWAY_PANEL_IMAGE = "https://i.postimg.cc/T1MJ27Zj/zzz.png"
BOOST_EMBED_COLOR = 0x16c7f0

SOCIAL_LINKS = [
    ("SnapChat",    "https://www.snapchat.com/@iimlkq",  1538760503566803036),
    ("Instagram",   "https://www.instagram.com/imlkq1",   1538773157849075812),
    ("TikTok",      "https://www.tiktok.com/@imlkq",      1538773286022815744),
    ("X (Twitter)", "https://x.com/imlkq1",               1538760262759354458),
    ("Kick",        "https://kick.com/imlkq",             1538772365784260660),
    ("WhatsApp",    "https://www.whatsapp.com/channel/0029VaeFkY9FXUuV971StZ0W", 1538774156387155978),
    ("YouTube",     "https://www.youtube.com/@imlkq1",    1538774156387155978),
]

RULES_TEXT = """**1.** يرجى من الجميع احترام جميع أعضاء السيرفر.

**2.** يمنع إرسال أي روابط أو طلب أي دعم.

**3.** يمنع طلب أي رتبة غير مستحقة.

**4.** يمنع الترويج أو نشر السيرفرات الأخرى سواءً في الخاص أو داخل السيرفر.

**5.** يمنع التدخل في خصوصيات الآخرين.

**6.** يمنع السب أو القذف أو الشتم.

**7.** يمنع التحدث في المواضيع السياسية أو الدينية أو العنصرية.

**8.** يمنع منعًا باتًا إرسال أي محتوى أو صور مخلة بالآداب.

**9.** يمنع إثارة المشاكل داخل السيرفر.

**10.** يمنع السبام أو تكبير الحروف في جميع الشاتات.

**11.** مخالفة القوانين قد تعرضك للباند النهائي.

**12.** أخيرًا، احترم تُحترم، واستمتع بوقتك."""

LEVELS_TEXT = """**رتب المستويات والمميزات:**

<@&1551629950337945740> (LVL 1) - استخدام إيموجيات وستيكرات خارجية + مشاركة الشاشة في الرومات الصوتية.
<@&1551630083611951104> (LVL 10) - إمكانية تغيير اللقب داخل السيرفر.
<@&1551630153359294574> (LVL 20) - إمكانية إرسال الصور والمقاطع في الشات العام.
<@&1551630206459052103> (LVL 30) - إضافة إيموجي خاص للسيرفر.

**رتب المستويات المتقدمة:**

LVL 40: <@&1551630294614802482>
LVL 50: <@&1551630458884980856>
LVL 60: <@&1551630612084849>
LVL 70: <@&1551630752653779098>
LVL 80: <@&1551630378890961028>
LVL 90: <@&1551651214872027136>
LVL 100: <@&1551630752653779098>

**رتب إضافية:**

<@&1551646588877803611> ┆ <@&1551646691059302490> ┆ <@&1551646804221759530> ┆ <@&1551646926217150525> ┆ <@&1551647061357625384>"""

# ============================================================
#                       البوت
# ============================================================
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

app_status = {"event": True, "staff": True, "lady": True, "dev": True}
pending_apps = {}
giveaway_entries = {}
tickets_data = {}
jail_data = {}
DATA_FILE = "bot_data.json"


def save_data():
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump({
                "app_status": app_status,
                "tickets_data": tickets_data,
                "jail_data": jail_data,
            }, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"[save_data] {e}")


def load_data():
    global app_status, tickets_data, jail_data
    if not os.path.exists(DATA_FILE):
        return
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            d = json.load(f)
            app_status.update(d.get("app_status", {}))
            tickets_data.update(d.get("tickets_data", {}))
            jail_data.update(d.get("jail_data", {}))
    except Exception as e:
        print(f"[load_data] {e}")


async def fetch_image_bytes(url: str):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    return await resp.read()
    except Exception as e:
        print(f"[fetch_image] {e}")
    return None


async def send_image_with_view(channel, image_url, view, filename="panel.png"):
    img = await fetch_image_bytes(image_url)
    if img is None:
        await channel.send(image_url, view=view)
        return
    file = discord.File(fp=io.BytesIO(img), filename=filename)
    await channel.send(file=file, view=view)


# ============================================================
#                    Views: الترحيب
# ============================================================
class WelcomeView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Server Rules", style=discord.ButtonStyle.secondary,
                       custom_id="imlkq:welcome:rules")
    async def rules_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(title="📜 قوانين سيرفر iMLKq Community",
                              description=RULES_TEXT, color=0x2b2d31)
        embed.set_thumbnail(url=THUMBNAIL)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label="Social Media", style=discord.ButtonStyle.secondary,
                       custom_id="imlkq:welcome:social")
    async def social_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(title="🌐 حسابات iMLKq الرسمية",
                              description="تابعنا على جميع منصاتنا الرسمية 👇",
                              color=0x2b2d31)
        embed.set_thumbnail(url=THUMBNAIL)
        await interaction.response.send_message(embed=embed, view=SocialView(), ephemeral=True)

    @discord.ui.button(label="Level System", style=discord.ButtonStyle.secondary,
                       custom_id="imlkq:welcome:levels")
    async def levels_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(title="📈 نظام المستويات",
                              description=LEVELS_TEXT, color=0x2b2d31)
        embed.set_thumbnail(url=THUMBNAIL)
        await interaction.response.send_message(embed=embed, ephemeral=True)


class SocialView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        for name, url, emoji_id in SOCIAL_LINKS:
            emoji = bot.get_emoji(emoji_id)
            self.add_item(discord.ui.Button(label=name, url=url,
                                            style=discord.ButtonStyle.link,
                                            emoji=emoji if emoji else None))


# ============================================================
#                    Views: التقديمات
# ============================================================
class ApplicationSelect(discord.ui.Select):
    def __init__(self):
        options = []
        for key, name in SECTION_NAMES.items():
            if app_status.get(key, True):
                options.append(discord.SelectOption(label=name, value=key))
        if not options:
            options.append(discord.SelectOption(label="لا توجد أقسام متاحة حالياً",
                                                value="none", default=True))
        super().__init__(placeholder="اختر القسم الذي تريد التقديم عليه...",
                         min_values=1, max_values=1, options=options,
                         custom_id="imlkq:app:select")

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "none":
            await interaction.response.send_message("🔒 جميع الأقسام مغلقة حالياً.", ephemeral=True)
            return
        section = self.values[0]
        if not app_status.get(section, False):
            await interaction.response.send_message("🔒 هذا القسم مغلق حالياً.", ephemeral=True)
            return
        await interaction.response.send_modal(ApplicationModal(section))


class ApplicationPanelView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(ApplicationSelect())


class ApplicationModal(discord.ui.Modal):
    def __init__(self, section):
        self.section = section
        super().__init__(title=f"تقديم - {SECTION_NAMES[section]}")

        if section == "event":
            self.q1 = discord.ui.TextInput(label="1) عرفنا بنفسك، وكم لك في السيرفر؟",
                                           style=discord.TextStyle.paragraph, required=True, max_length=500)
            self.q2 = discord.ui.TextInput(label="2) هل عندك خبرة سابقة في تنظيم فعاليات؟",
                                           style=discord.TextStyle.paragraph, required=True, max_length=500)
            self.q3 = discord.ui.TextInput(label="3) لو طلبنا فكرة فعالية جديدة، إيش بتكون؟",
                                           style=discord.TextStyle.paragraph, required=True, max_length=800)
            self.q4 = discord.ui.TextInput(label="4) لو صار خلاف، كيف تتصرف؟",
                                           style=discord.TextStyle.paragraph, required=True, max_length=500)
            self.q5 = discord.ui.TextInput(label="5) كم ساعة أسبوعيًا، وليش نقبلك؟",
                                           style=discord.TextStyle.paragraph, required=True, max_length=500)
            for q in (self.q1, self.q2, self.q3, self.q4, self.q5):
                self.add_item(q)

        elif section == "staff":
            self.q1 = discord.ui.TextInput(label="1) عرفنا بنفسك: اسمك، عمرك، ومن وين؟",
                                           style=discord.TextStyle.paragraph, required=True, max_length=500)
            self.q2 = discord.ui.TextInput(label="2) ليش تريد السابورت، ووش يميزك؟",
                                           style=discord.TextStyle.paragraph, required=True, max_length=500)
            self.q3 = discord.ui.TextInput(label="3) هل لديك خبرة سابقة في الدعم؟ اذكر مثالًا",
                                           style=discord.TextStyle.paragraph, required=True, max_length=500)
            self.q4 = discord.ui.TextInput(label="4) لو جاءك عضو بمشكلة ما تعرف حلها؟",
                                           style=discord.TextStyle.paragraph, required=True, max_length=500)
            self.q5 = discord.ui.TextInput(label="5) كيف تتعامل مع عضو عصبي؟",
                                           style=discord.TextStyle.paragraph, required=True, max_length=500)
            self.q6 = discord.ui.TextInput(label="6) كم ساعة أسبوعيًا للرد على التكتات؟",
                                           style=discord.TextStyle.paragraph, required=True, max_length=500)
            for q in (self.q1, self.q2, self.q3, self.q4, self.q5, self.q6):
                self.add_item(q)

        elif section == "lady":
            self.q1 = discord.ui.TextInput(label="1) اسمك", required=True, max_length=100)
            self.q2 = discord.ui.TextInput(label="2) عمرك", required=True, max_length=10)
            self.q3 = discord.ui.TextInput(label="3) من وين", required=True, max_length=100)
            self.q4 = discord.ui.TextInput(label="4) هل تستطيعين فتح المايك؟ (Yes/No)",
                                           placeholder="Yes أو No",
                                           required=True, max_length=5)
            for q in (self.q1, self.q2, self.q3, self.q4):
                self.add_item(q)

        elif section == "dev":
            self.q1 = discord.ui.TextInput(label="الاسم والعمر",
                                           placeholder="رهف - 20", required=True, max_length=100)
            self.q2 = discord.ui.TextInput(label="ساعات التواجد اليومية", required=True, max_length=50)
            self.q3 = discord.ui.TextInput(label="لغات البرمجة والمكتبات",
                                           style=discord.TextStyle.paragraph, required=True, max_length=500)
            self.q4 = discord.ui.TextInput(label="خبرتك في صناعة بوتات الديسكورد",
                                           style=discord.TextStyle.paragraph, required=True, max_length=800)
            self.q5 = discord.ui.TextInput(label="كيف تتصرف عند مواجهة ثغرة؟",
                                           style=discord.TextStyle.paragraph, required=True, max_length=800)
            for q in (self.q1, self.q2, self.q3, self.q4, self.q5):
                self.add_item(q)

    async def on_submit(self, interaction: discord.Interaction):
        if self.section == "lady":
            ans = self.q4.value.strip().lower()
            if ans not in ("yes", "no"):
                await interaction.response.send_message(
                    "❌ السؤال الرابع: اكتبي Yes أو No فقط.", ephemeral=True)
                return

        target = bot.get_channel(APP_TARGET_CHANNELS[self.section])
        if target is None:
            await interaction.response.send_message("❌ لم أجد روم القسم.", ephemeral=True)
            return

        embed = discord.Embed(title=f"📥 تقديم جديد - {SECTION_NAMES[self.section]}",
                              color=0x5865F2,
                              timestamp=datetime.datetime.now(timezone.utc))
        embed.set_thumbnail(url=interaction.user.display_avatar.url)
        embed.add_field(name="👤 المتقدم",
                        value=f"{interaction.user.mention}\n`{interaction.user.id}`",
                        inline=False)

        if self.section == "event":
            embed.add_field(name="1) عرفنا بنفسك", value=self.q1.value, inline=False)
            embed.add_field(name="2) خبرة في تنظيم الفعاليات", value=self.q2.value, inline=False)
            embed.add_field(name="3) فكرة فعالية جديدة", value=self.q3.value, inline=False)
            embed.add_field(name="4) عند الخلاف كيف تتصرف", value=self.q4.value, inline=False)
            embed.add_field(name="5) كم ساعة أسبوعيًا وليش نقبلك", value=self.q5.value, inline=False)
        elif self.section == "staff":
            embed.add_field(name="1) عرفنا بنفسك", value=self.q1.value, inline=False)
            embed.add_field(name="2) ليش السابورت ووش يميزك", value=self.q2.value, inline=False)
            embed.add_field(name="3) خبرة سابقة في الدعم", value=self.q3.value, inline=False)
            embed.add_field(name="4) لو ما تعرف تحل مشكلة", value=self.q4.value, inline=False)
            embed.add_field(name="5) التعامل مع عضو عصبي", value=self.q5.value, inline=False)
            embed.add_field(name="6) كم ساعة أسبوعيًا", value=self.q6.value, inline=False)
        elif self.section == "lady":
            embed.add_field(name="1) اسمك", value=self.q1.value, inline=False)
            embed.add_field(name="2) عمرك", value=self.q2.value, inline=False)
            embed.add_field(name="3) من وين", value=self.q3.value, inline=False)
            embed.add_field(name="4) فتح المايك؟", value=self.q4.value, inline=False)
        elif self.section == "dev":
            embed.add_field(name="1) الاسم والعمر", value=self.q1.value, inline=False)
            embed.add_field(name="2) ساعات التواجد", value=self.q2.value, inline=False)
            embed.add_field(name="3) لغات البرمجة", value=self.q3.value, inline=False)
            embed.add_field(name="4) خبرة البوتات", value=self.q4.value, inline=False)
            embed.add_field(name="5) معالجة الأخطاء", value=self.q5.value, inline=False)

        view = ApplicationReviewView()
        msg = await target.send(embed=embed, view=view)
        pending_apps[msg.id] = {"user_id": interaction.user.id, "section": self.section}

        await interaction.response.send_message(
            "✅ تم إرسال تقديمك، انتظر رد الإدارة.", ephemeral=True)


class ApplicationReviewView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Accept", style=discord.ButtonStyle.success,
                       custom_id="imlkq:app:accept")
    async def accept(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not interaction.user.guild_permissions.manage_roles:
            await interaction.response.send_message("❌ لا تملك الصلاحية.", ephemeral=True)
            return
        data = pending_apps.get(interaction.message.id)
        if not data:
            await interaction.response.send_message("⚠️ تمت معالجته مسبقاً.", ephemeral=True)
            return

        member = interaction.guild.get_member(data["user_id"])
        section = data["section"]
        if member is None:
            await interaction.response.send_message("❌ العضو غادر.", ephemeral=True)
            return

        roles = [interaction.guild.get_role(r) for r in ACCEPT_ROLES[section]]
        roles = [r for r in roles if r]
        try:
            if roles:
                await member.add_roles(*roles, reason=f"Accepted by {interaction.user}")
        except discord.Forbidden:
            await interaction.response.send_message("❌ لا أملك صلاحية إعطاء الرتب.", ephemeral=True)
            return

        embed = interaction.message.embeds[0]
        embed.color = 0x57F287
        ts = int(datetime.datetime.now(timezone.utc).timestamp())
        embed.add_field(name="✅ تم القبول",
                        value=f"بواسطة: {interaction.user.mention}\n<t:{ts}:R>",
                        inline=False)
        embed.set_footer(text=f"Accepted by {interaction.user}")

        for child in self.children:
            child.disabled = True
        await interaction.message.edit(embed=embed, view=self)

        try:
            dm = discord.Embed(title="🎉 مبروك! تم قبولك",
                               description=f"تم قبولك في **{SECTION_NAMES[section]}** في سيرفر iMLKq Community.\nمرحباً بك في الفريق!",
                               color=0x57F287)
            dm.set_thumbnail(url=THUMBNAIL)
            await member.send(embed=dm)
        except discord.Forbidden:
            pass

        pending_apps.pop(interaction.message.id, None)
        await interaction.response.send_message("✅ تم القبول.", ephemeral=True)

    @discord.ui.button(label="Deny", style=discord.ButtonStyle.danger,
                       custom_id="imlkq:app:deny")
    async def deny(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not interaction.user.guild_permissions.manage_roles:
            await interaction.response.send_message("❌ لا تملك الصلاحية.", ephemeral=True)
            return
        data = pending_apps.get(interaction.message.id)
        if not data:
            await interaction.response.send_message("⚠️ تمت معالجته مسبقاً.", ephemeral=True)
            return
        await interaction.response.send_modal(DenyReasonModal(
            interaction.message.id, data["user_id"], data["section"]))


class DenyReasonModal(discord.ui.Modal, title="سبب الرفض"):
    reason = discord.ui.TextInput(label="سبب الرفض",
                                  style=discord.TextStyle.paragraph,
                                  required=True, max_length=500)

    def __init__(self, message_id, user_id, section):
        super().__init__()
        self.message_id = message_id
        self.user_id = user_id
        self.section = section

    async def on_submit(self, interaction: discord.Interaction):
        member = interaction.guild.get_member(self.user_id)
        try:
            msg = await interaction.channel.fetch_message(self.message_id)
        except discord.NotFound:
            await interaction.response.send_message("❌ الرسالة غير موجودة.", ephemeral=True)
            return

        embed = msg.embeds[0]
        embed.color = 0xED4245
        embed.add_field(name="❌ تم الرفض",
                        value=f"بواسطة: {interaction.user.mention}\nالسبب: {self.reason.value}",
                        inline=False)
        embed.set_footer(text=f"Denied by {interaction.user}")

        await msg.edit(embed=embed, view=None)

        if member:
            try:
                dm = discord.Embed(title="❌ تم رفض تقديمك",
                                   description=f"تم رفض تقديمك في **{SECTION_NAMES[self.section]}**.\n**السبب:** {self.reason.value}",
                                   color=0xED4245)
                dm.set_thumbnail(url=THUMBNAIL)
                await member.send(embed=dm)
            except discord.Forbidden:
                pass

        pending_apps.pop(self.message_id, None)
        await interaction.response.send_message("✅ تم الرفض.", ephemeral=True)


# ============================================================
#              Views: لوحة التحكم
# ============================================================
class AppControlView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Toggle All", style=discord.ButtonStyle.secondary,
                       custom_id="imlkq:ctrl:toggle_all", row=0)
    async def toggle_all(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not interaction.user.guild_permissions.manage_guild:
            await interaction.response.send_message("❌ لا تملك الصلاحية.", ephemeral=True)
            return
        new_state = not all(app_status.values())
        for k in app_status:
            app_status[k] = new_state
        save_data()
        await interaction.response.send_message(
            "✅ تم فتح الكل" if new_state else "🔒 تم إغلاق الكل", ephemeral=True)
        await refresh_app_panel()
        if not any(app_status.values()):
            await send_app_closed_message()

    @discord.ui.button(label="Event", style=discord.ButtonStyle.secondary,
                       custom_id="imlkq:ctrl:event", row=1)
    async def t_event(self, interaction, button):
        await self._toggle(interaction, "event")

    @discord.ui.button(label="Staff", style=discord.ButtonStyle.secondary,
                       custom_id="imlkq:ctrl:staff", row=1)
    async def t_staff(self, interaction, button):
        await self._toggle(interaction, "staff")

    @discord.ui.button(label="Lady", style=discord.ButtonStyle.secondary,
                       custom_id="imlkq:ctrl:lady", row=1)
    async def t_lady(self, interaction, button):
        await self._toggle(interaction, "lady")

    @discord.ui.button(label="Developer", style=discord.ButtonStyle.secondary,
                       custom_id="imlkq:ctrl:dev", row=1)
    async def t_dev(self, interaction, button):
        await self._toggle(interaction, "dev")

    async def _toggle(self, interaction, section):
        if not interaction.user.guild_permissions.manage_guild:
            await interaction.response.send_message("❌ لا تملك الصلاحية.", ephemeral=True)
            return
        app_status[section] = not app_status[section]
        save_data()
        state = "🟢 مفتوح" if app_status[section] else "🔴 مغلق"
        await interaction.response.send_message(
            f"{SECTION_NAMES[section]}: {state}", ephemeral=True)
        await refresh_app_panel()
        if not app_status[section]:
            await send_app_closed_message(section=section)


async def refresh_app_panel():
    channel = bot.get_channel(APP_PANEL_CHANNEL_ID)
    if channel is None:
        return
    async for msg in channel.history(limit=30):
        if msg.author.id == bot.user.id and msg.components:
            try:
                await msg.edit(view=ApplicationPanelView())
            except Exception:
                pass
            return


async def send_app_closed_message(section: str = None):
    content = "# التقديم مقفل"
    channels_to_notify = [APP_PANEL_CHANNEL_ID]
    if section and section in APP_TARGET_CHANNELS:
        channels_to_notify.append(APP_TARGET_CHANNELS[section])
    for cid in channels_to_notify:
        ch = bot.get_channel(cid)
        if ch is None:
            continue
        try:
            await ch.send(content)
        except Exception:
            pass
        # ============================================================
#              Views: السحوبات
# ============================================================
class GiveawaySelect(discord.ui.Select):
    def __init__(self):
        super().__init__(
            placeholder="اختر إجراء...",
            options=[
                discord.SelectOption(label="إنشاء سحب جديد", value="create"),
                discord.SelectOption(label="إعطاء رتبة فائز يدوي", value="give_role"),
            ],
            custom_id="imlkq:giveaway:select",
        )

    async def callback(self, interaction: discord.Interaction):
        if not interaction.user.guild_permissions.manage_guild:
            await interaction.response.send_message("❌ لا تملك الصلاحية.", ephemeral=True)
            return
        if self.values[0] == "create":
            await interaction.response.send_modal(CreateGiveawayModal())
        else:
            await interaction.response.send_modal(GiveWinnerRoleModal())


class GiveawayPanelView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(GiveawaySelect())


class CreateGiveawayModal(discord.ui.Modal, title="إنشاء سحب جديد"):
    ch_id = discord.ui.TextInput(label="آيدي روم السحب", required=True, max_length=25)
    prize = discord.ui.TextInput(label="عنوان الجائزة", required=True, max_length=200)
    conds = discord.ui.TextInput(label="شروط السحب",
                                 style=discord.TextStyle.paragraph,
                                 required=False, max_length=500)
    duration = discord.ui.TextInput(label="المدة (بالدقائق)", required=True, max_length=10)
    winners = discord.ui.TextInput(label="عدد الفائزين", required=True, max_length=3)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            ch_id = int(self.ch_id.value.strip())
            dur = int(self.duration.value.strip())
            wc = int(self.winners.value.strip())
        except ValueError:
            await interaction.response.send_message("❌ تأكد من الأرقام.", ephemeral=True)
            return
        channel = bot.get_channel(ch_id)
        if channel is None:
            await interaction.response.send_message("❌ لم أجد الروم.", ephemeral=True)
            return

        end_ts = int((datetime.datetime.now(timezone.utc) +
                      timedelta(minutes=dur)).timestamp())
        embed = discord.Embed(
            title=f"🎉 {self.prize.value}",
            description=f"**الشروط:**\n{self.conds.value or 'لا يوجد'}\n\n**الفائزون:** {wc}\n**ينتهي:** <t:{end_ts}:R>",
            color=0xF1C40F,
        )
        embed.set_thumbnail(url=THUMBNAIL)
        embed.set_footer(text=f"Hosted by {interaction.user}")

        view = EnterGiveawayView()
        msg = await channel.send(embed=embed, view=view)
        giveaway_entries[msg.id] = set()

        bot.loop.create_task(_finish_giveaway(msg.id, channel.id, end_ts, wc))
        await interaction.response.send_message(f"✅ تم إنشاء السحب في {channel.mention}",
                                                ephemeral=True)


class EnterGiveawayView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Enter", style=discord.ButtonStyle.success,
                       emoji="🎉", custom_id="imlkq:giveaway:enter")
    async def enter(self, interaction: discord.Interaction, button: discord.ui.Button):
        giveaway_entries.setdefault(interaction.message.id, set()).add(interaction.user.id)
        await interaction.response.send_message("✅ تم تسجيلك في السحب.", ephemeral=True)


class GiveWinnerRoleModal(discord.ui.Modal, title="إعطاء رتبة فائز يدوي"):
    member_id = discord.ui.TextInput(label="آيدي العضو", required=True, max_length=25)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            mid = int(self.member_id.value.strip())
        except ValueError:
            await interaction.response.send_message("❌ آيدي غير صالح.", ephemeral=True)
            return
        member = interaction.guild.get_member(mid)
        role = interaction.guild.get_role(WINNER_ROLE_ID)
        if member is None or role is None:
            await interaction.response.send_message("❌ لم أجد العضو أو الرتبة.", ephemeral=True)
            return
        try:
            await member.add_roles(role, reason=f"Manual by {interaction.user}")
        except discord.Forbidden:
            await interaction.response.send_message("❌ لا أملك صلاحية.", ephemeral=True)
            return
        await interaction.response.send_message(f"✅ تم إعطاء الرتبة لـ {member.mention}",
                                                ephemeral=True)


async def _finish_giveaway(message_id, channel_id, end_ts, winners_count):
    delay = end_ts - int(datetime.datetime.now(timezone.utc).timestamp())
    if delay > 0:
        await asyncio.sleep(delay)

    channel = bot.get_channel(channel_id)
    if channel is None:
        return
    try:
        msg = await channel.fetch_message(message_id)
    except discord.NotFound:
        return

    entries = list(giveaway_entries.get(message_id, set()))
    if not entries:
        await channel.send("⚠️ لم يشارك أحد في السحب.")
        return

    winners = random.sample(entries, min(winners_count, len(entries)))
    winner_mentions = []
    role = channel.guild.get_role(WINNER_ROLE_ID)

    for wid in winners:
        member = channel.guild.get_member(wid)
        if member:
            winner_mentions.append(member.mention)
            if role:
                try:
                    await member.add_roles(role, reason="Giveaway winner")
                except discord.Forbidden:
                    pass
            try:
                dm = discord.Embed(title="🏆 مبروك! فزت بالسحب",
                                   description="لقد فزت بسحب في سيرفر iMLKq Community!",
                                   color=0xF1C40F)
                dm.set_thumbnail(url=THUMBNAIL)
                await member.send(embed=dm)
            except discord.Forbidden:
                pass

    embed = msg.embeds[0]
    embed.color = 0x57F287
    embed.add_field(name="🏆 الفائزون",
                    value="\n".join(winner_mentions) or "لا يوجد", inline=False)
    await msg.edit(embed=embed, view=None)
    await channel.send(f"🎉 مبروك للفائزين: {', '.join(winner_mentions)}")


# ============================================================
#         Views: التكتات
# ============================================================
class TicketTypeSelect(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="الإدارة العليا", value="high_staff"),
            discord.SelectOption(label="دعم الإيفنت",   value="event_support"),
            discord.SelectOption(label="الدعم الفني",   value="tech_support"),
            discord.SelectOption(label="الدعم بالكيك",  value="kick_support"),
        ]
        super().__init__(
            placeholder="اختر نوع التذكرة...",
            min_values=1, max_values=1,
            options=options,
            custom_id="imlkq:ticket:type_select",
        )

    async def callback(self, interaction: discord.Interaction):
        await open_ticket(interaction, self.values[0])


class TicketPanelView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(TicketTypeSelect())


# ============ داخل التكت ============
class TicketInsideView(discord.ui.View):
    """زر واحد فقط داخل التكت (إيموجي فقط)"""
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(emoji="⚙️",
                       style=discord.ButtonStyle.secondary,
                       custom_id="imlkq:ticket:admin_options")
    async def admin_options(self, interaction: discord.Interaction, button: discord.ui.Button):
        ch = interaction.channel
        data = tickets_data.get(str(ch.id))
        if not data:
            await interaction.response.send_message("❌ هذا ليس تكت.", ephemeral=True)
            return

        has_perm = interaction.user.guild_permissions.manage_roles
        has_role = any(r.id == GENERAL_STAFF_ROLE_ID for r in interaction.user.roles)

        if not (has_perm or has_role):
            await interaction.response.send_message("❌ لا تملك الصلاحية.", ephemeral=True)
            return

        img = await fetch_image_bytes(TICKET_ADMIN_OPTIONS_IMAGE)
        if img:
            file = discord.File(fp=io.BytesIO(img), filename="admin.png")
            await interaction.response.send_message(
                file=file, view=TicketAdminActionsView(), ephemeral=True)
        else:
            await interaction.response.send_message(
                TICKET_ADMIN_OPTIONS_IMAGE, view=TicketAdminActionsView(), ephemeral=True)


class TicketAdminActionsView(discord.ui.View):
    """أزرار الإدارة - تظهر فقط في الـ ephemeral"""
    def __init__(self):
        super().__init__(timeout=600)

    @staticmethod
    def has_access(user):
        if user.guild_permissions.manage_roles:
            return True
        return any(r.id == GENERAL_STAFF_ROLE_ID for r in user.roles)

    @staticmethod
    def get_owner(guild, data):
        return guild.get_member(data["owner"])

    @discord.ui.button(emoji="🔒", style=discord.ButtonStyle.secondary,
                       custom_id="imlkq:ticket:lock_btn")
    async def lock(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not self.has_access(interaction.user):
            await interaction.response.send_message("❌ لا تملك الصلاحية.", ephemeral=True)
            return
        ch = interaction.channel
        data = tickets_data.get(str(ch.id))
        if not data:
            await interaction.response.send_message("❌ ليس تكت.", ephemeral=True)
            return
        if data.get("locked"):
            await interaction.response.send_message("🔒 مقفل بالفعل.", ephemeral=True)
            return
        owner = self.get_owner(interaction.guild, data)
        try:
            await ch.set_permissions(interaction.guild.default_role, send_messages=False)
            if owner:
                await ch.set_permissions(owner, send_messages=False)
            data["locked"] = True
            save_data()
            if owner:
                await ch.edit(name=f"🔒〡{owner.name}〡t-{data['number']}")
        except Exception as e:
            await interaction.response.send_message(f"❌ {e}", ephemeral=True)
            return
        await interaction.response.send_message("🔒 تم القفل.", ephemeral=True)
        await send_ticket_log(interaction.guild, "Closed", data, interaction.user)

    @discord.ui.button(emoji="🔓", style=discord.ButtonStyle.secondary,
                       custom_id="imlkq:ticket:reopen_btn")
    async def reopen(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not self.has_access(interaction.user):
            await interaction.response.send_message("❌ لا تملك الصلاحية.", ephemeral=True)
            return
        ch = interaction.channel
        data = tickets_data.get(str(ch.id))
        if not data:
            await interaction.response.send_message("❌ ليس تكت.", ephemeral=True)
            return
        if not data.get("locked"):
            await interaction.response.send_message("🔓 التكت مفتوح بالفعل.", ephemeral=True)
            return
        owner = self.get_owner(interaction.guild, data)
        try:
            if owner:
                await ch.set_permissions(owner, send_messages=True)
            data["locked"] = False
            save_data()
            if owner:
                await ch.edit(name=f"🟢〡{owner.name}〡t-{data['number']}")
        except Exception as e:
            await interaction.response.send_message(f"❌ {e}", ephemeral=True)
            return
        await interaction.response.send_message("🔓 تم إعادة فتح التكت.", ephemeral=True)
        await send_ticket_log(interaction.guild, "Re-Open", data, interaction.user)

    @discord.ui.button(emoji="🗑️", style=discord.ButtonStyle.danger,
                       custom_id="imlkq:ticket:delete_btn")
    async def delete(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not self.has_access(interaction.user):
            await interaction.response.send_message("❌ لا تملك الصلاحية.", ephemeral=True)
            return
        ch = interaction.channel
        data = tickets_data.get(str(ch.id))
        if not data:
            await interaction.response.send_message("❌ ليس تكت.", ephemeral=True)
            return
        await send_ticket_log(interaction.guild, "Deleted", data, interaction.user)
        await interaction.response.send_message("🗑️ سيتم الحذف خلال 3 ثواني...", ephemeral=True)
        await asyncio.sleep(3)
        tickets_data.pop(str(ch.id), None)
        save_data()
        try:
            await ch.delete()
        except Exception:
            pass

    @discord.ui.button(emoji="➕", style=discord.ButtonStyle.secondary,
                       custom_id="imlkq:ticket:add_btn")
    async def add_member(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not self.has_access(interaction.user):
            await interaction.response.send_message("❌ لا تملك الصلاحية.", ephemeral=True)
            return
        await interaction.response.send_modal(AddMemberModal())

    @discord.ui.button(emoji="🔔", style=discord.ButtonStyle.secondary,
                       custom_id="imlkq:ticket:ping_btn")
    async def ping(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not self.has_access(interaction.user):
            await interaction.response.send_message("❌ لا تملك الصلاحية.", ephemeral=True)
            return
        ch = interaction.channel
        data = tickets_data.get(str(ch.id))
        if not data:
            await interaction.response.send_message("❌ ليس تكت.", ephemeral=True)
            return
        owner = self.get_owner(interaction.guild, data)
        role = interaction.guild.get_role(TICKET_TYPES[data["type"]]["role_id"])
        msg = "🔔 **تنبيه**"
        if owner:
            msg += f" {owner.mention}"
        if role:
            msg += f" {role.mention}"
        await ch.send(msg)
        await interaction.response.send_message("✅ تم التنبيه.", ephemeral=True)

    @discord.ui.button(emoji="✅", style=discord.ButtonStyle.success,
                       custom_id="imlkq:ticket:claim_btn")
    async def claim(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not self.has_access(interaction.user):
            await interaction.response.send_message("❌ لا تملك الصلاحية.", ephemeral=True)
            return
        ch = interaction.channel
        data = tickets_data.get(str(ch.id))
        if not data:
            await interaction.response.send_message("❌ ليس تكت.", ephemeral=True)
            return
        if data.get("claimed_by"):
            await interaction.response.send_message(
                f"⚠️ مستلمة من <@{data['claimed_by']}>.", ephemeral=True)
            return
        data["claimed_by"] = interaction.user.id
        save_data()

        owner = self.get_owner(interaction.guild, data)
        try:
            if owner:
                await ch.edit(name=f"🟢〡{owner.name}〡t-{data['number']}")
        except Exception as e:
            print(f"[rename claim] {e}")

        embed = discord.Embed(
            title="✅ تم استلام التكت",
            description=f"استلم التكت: {interaction.user.mention}",
            color=0x57F287,
        )
        embed.set_image(url=TICKET_SUCCESS_IMAGE)
        await ch.send(embed=embed)
        await interaction.response.send_message("✅ تم الاستلام.", ephemeral=True)
        await send_ticket_log(interaction.guild, "Claimed", data, interaction.user)


class AddMemberModal(discord.ui.Modal, title="إضافة عضو للتكت"):
    member_id = discord.ui.TextInput(label="آيدي العضو", required=True, max_length=25)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            mid = int(self.member_id.value.strip())
        except ValueError:
            await interaction.response.send_message("❌ آيدي غير صالح.", ephemeral=True)
            return
        member = interaction.guild.get_member(mid)
        if member is None:
            await interaction.response.send_message("❌ لم أجد العضو.", ephemeral=True)
            return
        try:
            await interaction.channel.set_permissions(member, view_channel=True,
                                                     send_messages=True,
                                                     read_message_history=True)
        except Exception as e:
            await interaction.response.send_message(f"❌ {e}", ephemeral=True)
            return
        await interaction.response.send_message(f"✅ تم إضافة {member.mention}.",
                                                ephemeral=True)


# ============================================================
#   نظام الأوامر النصية (🔒 🔓 hide unhide) — لكل الرومات
# ============================================================
async def handle_ticket_text_commands(message: discord.Message):
    """يتفاعل مع الأوامر النصية في أي روم - الشرط: رتبة GENERAL_STAFF_ROLE_ID"""
    if message.author.bot:
        return False
    if not message.guild:
        return False

    content = message.content.strip()
    content_lower = content.lower()

    actions = {
        "🔒":   ("lock",    "🔒"),
        "🔓":   ("unlock",  "🔓"),
        "hide": ("hide",    "🙈"),
        "unhide": ("unhide", "👁️"),
    }

    key = content if content in ("🔒", "🔓") else content_lower
    if key not in actions:
        return False

    # ✅ الشرط الوحيد: يمتلك رتبة GENERAL_STAFF_ROLE_ID
    has_role = any(r.id == GENERAL_STAFF_ROLE_ID for r in message.author.roles)
    if not has_role:
        return False

    action, _ = actions[key]
    ch = message.channel

    try:
        if action == "lock":
            await ch.set_permissions(message.guild.default_role, send_messages=False)

        elif action == "unlock":
            await ch.set_permissions(message.guild.default_role, send_messages=None)

        elif action == "hide":
            await ch.set_permissions(message.guild.default_role, view_channel=False)

        elif action == "unhide":
            await ch.set_permissions(message.guild.default_role, view_channel=None)

        # إذا الروم تكت → نعدل بياناته
        data = tickets_data.get(str(ch.id))
        if data:
            if action == "lock":
                data["locked"] = True
                owner = message.guild.get_member(data["owner"])
                if owner:
                    try:
                        await ch.set_permissions(owner, send_messages=False)
                        await ch.edit(name=f"🔒〡{owner.name}〡t-{data['number']}")
                    except Exception:
                        pass
            elif action == "unlock":
                data["locked"] = False
                owner = message.guild.get_member(data["owner"])
                if owner:
                    try:
                        await ch.set_permissions(owner, send_messages=True)
                        await ch.edit(name=f"🟢〡{owner.name}〡t-{data['number']}")
                    except Exception:
                        pass
            save_data()

        # حط الريأكشن على الرسالة
        try:
            emoji = bot.get_emoji(REACTION_EMOJI_ID)
            if emoji:
                await message.add_reaction(emoji)
        except Exception as e:
            print(f"[reaction] {e}")

        # أرسل إشعار في روم اللوق
        await send_ticket_action_log(message.guild, action, ch, message.author)

    except Exception as e:
        print(f"[text_cmd] {e}")

    return True


async def send_ticket_action_log(guild: discord.Guild, action: str, channel, actor: discord.Member):
    """إرسال إمبد مخصص في روم لوق الأوامر"""
    log_ch = guild.get_channel(TICKET_ACTION_LOG_CHANNEL_ID)
    if log_ch is None:
        return

    # نجيب بيانات التكت إذا كان تكت
    data = tickets_data.get(str(channel.id))
    owner = None
    ticket_type_label = "—"
    ticket_number = "—"

    if data:
        owner = guild.get_member(data["owner"])
        ticket_type_label = TICKET_TYPES[data["type"]]["label"]
        ticket_number = data["number"]

    titles = {
        "lock":   "🔒 | Channel Locked",
        "unlock": "🔓 | Channel Unlocked",
        "hide":   "🙈 | Channel Hidden",
        "unhide": "👁️ | Channel Unhidden",
    }
    colors = {
        "lock":   0xED4245,
        "unlock": 0x57F287,
        "hide":   0x95A5A6,
        "unhide": 0x57F287,
    }
    status_ar = {
        "lock":   "مقفل",
        "unlock": "مفتوح",
        "hide":   "مخفي",
        "unhide": "ظاهر",
    }

    embed = discord.Embed(
        title=titles.get(action, action),
        description=f"**📍 الروم:** {channel.mention}",
        color=colors.get(action, 0x16c7f0),
        timestamp=datetime.datetime.now(timezone.utc),
    )
    embed.add_field(name="🛠️ | By:", value=actor.mention, inline=True)
    embed.add_field(name="🚦 | Status:", value=f"`{status_ar.get(action, action)}`", inline=True)

    if data:
        embed.add_field(name="👤 | Owner:",
                        value=owner.mention if owner else f"`{data['owner']}`", inline=True)
        embed.add_field(name="📁 | Type:", value=ticket_type_label, inline=True)
        embed.add_field(name="🔢 | Ticket:", value=f"`{ticket_number}`", inline=True)

    embed.set_footer(text="Powered By [ Xiy_y ]", icon_url=POWERED_BY_IMAGE)
    try:
        await log_ch.send(embed=embed)
    except Exception as e:
        print(f"[action_log] {e}")


async def open_ticket(interaction: discord.Interaction, ttype: str):
    guild = interaction.guild
    info = TICKET_TYPES[ttype]

    for ch_id, data in tickets_data.items():
        if data.get("owner") == interaction.user.id and data.get("type") == ttype:
            ch = guild.get_channel(int(ch_id))
            if ch:
                await interaction.response.send_message(
                    f"⚠️ عندك تكت مفتوح: {ch.mention}", ephemeral=True)
                return

    # ✅ الصلاحيات: الرتبة المسؤولة فقط + صاحب التكت + البوت
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(view_channel=False),
        interaction.user: discord.PermissionOverwrite(view_channel=True,
                                                     send_messages=True,
                                                     read_message_history=True,
                                                     attach_files=True),
        guild.me: discord.PermissionOverwrite(view_channel=True,
                                              send_messages=True,
                                              manage_channels=True),
    }

    support_role = guild.get_role(info["role_id"])
    if support_role:
        overwrites[support_role] = discord.PermissionOverwrite(
            view_channel=True, send_messages=True, read_message_history=True,
            manage_messages=True, manage_channels=True)

    category = guild.get_channel(TICKET_CATEGORY_ID) if TICKET_CATEGORY_ID else None

    ticket_number = len(tickets_data) + 1
    new_name = f"🟠〡{interaction.user.name}〡t-{ticket_number}"

    try:
        channel = await guild.create_text_channel(
            name=new_name,
            overwrites=overwrites,
            category=category,
            topic=f"Owner: {interaction.user.id} | Type: {ttype}",
        )
    except Exception as e:
        await interaction.response.send_message(f"❌ {e}", ephemeral=True)
        return

    tickets_data[str(channel.id)] = {
        "owner": interaction.user.id,
        "type": ttype,
        "number": ticket_number,
        "claimed_by": None,
        "locked": False,
        "channel_id": channel.id,
        "created_at": int(datetime.datetime.now(timezone.utc).timestamp()),
    }
    save_data()

    await interaction.response.send_message(f"✅ تم إنشاء تكتك: {channel.mention}",
                                            ephemeral=True)

    await send_image_with_view(channel, TICKET_INSIDE_IMAGE,
                               TicketInsideView(), filename="ticket.png")
    await send_ticket_log(guild, "Open", tickets_data[str(channel.id)], interaction.user)


async def send_ticket_log(guild: discord.Guild, action: str, data: dict, actor: discord.Member):
    log_ch = guild.get_channel(TICKET_LOG_CHANNEL_ID)
    if log_ch is None:
        return
    owner = guild.get_member(data["owner"])
    claimed = guild.get_member(data["claimed_by"]) if data.get("claimed_by") else None

    colors = {"Open": 0x57F287, "Claimed": 0xF1C40F, "Closed": 0xED4245,
              "Re-Open": 0x57F287, "Deleted": 0xED4245}
    titles = {"Open": "🔓 | Open Ticket", "Claimed": "👋 | Claimed Ticket",
              "Closed": "🔒 | Closed Ticket", "Re-Open": "🔓 | Re-Open Ticket",
              "Deleted": "🗑️ | Deleted Ticket"}

    embed = discord.Embed(
        title=titles.get(action, action),
        color=colors.get(action, 0x16c7f0),
        timestamp=datetime.datetime.now(timezone.utc),
    )
    embed.add_field(name="👤 Owner:",
                    value=owner.mention if owner else f"`{data['owner']}`", inline=True)
    embed.add_field(name="🛠️ By:", value=actor.mention, inline=True)
    embed.add_field(name="📁 Type:",
                    value=TICKET_TYPES[data["type"]]["label"], inline=True)
    embed.add_field(name="🔢 Number:", value=f"`{data['number']}`", inline=True)
    embed.add_field(name="👋 Claimed:",
                    value=claimed.mention if claimed else "Not Claimed", inline=True)
    embed.add_field(name="🚦 Status:", value=f"`{action}`", inline=True)
    embed.set_footer(text="Powered By [ Xiy_y ]", icon_url=POWERED_BY_IMAGE)
    try:
        await log_ch.send(embed=embed)
    except Exception:
        pass
    # ============================================================
#              Views: السجن
# ============================================================
class JailPanelView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="سجن", style=discord.ButtonStyle.danger,
                       custom_id="imlkq:jail:jail", row=0)
    async def jail(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not interaction.user.guild_permissions.manage_roles:
            await interaction.response.send_message("❌ لا تملك الصلاحية.", ephemeral=True)
            return
        await interaction.response.send_modal(JailModal())

    @discord.ui.button(label="إفراج", style=discord.ButtonStyle.secondary,
                       custom_id="imlkq:jail:release", row=0)
    async def release(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not interaction.user.guild_permissions.manage_roles:
            await interaction.response.send_message("❌ لا تملك الصلاحية.", ephemeral=True)
            return
        await interaction.response.send_modal(ReleaseModal())


def parse_duration(text: str):
    """يرجع عدد الثواني. الصيغ: 1m (دقيقة) / 1h / 1d / 1w / 1mo (شهر) / 1y"""
    text = text.strip().lower()
    m = re.match(r"^(\d+)\s*(mo|m|h|d|w|y)$", text)
    if not m:
        return None
    n = int(m.group(1))
    unit = m.group(2)
    mult = {
        "m": 60, "h": 3600, "d": 86400, "w": 604800,
        "mo": 2592000, "y": 31536000,
    }.get(unit)
    if mult is None:
        return None
    return n * mult


class JailModal(discord.ui.Modal, title="سجن عضو"):
    member_id = discord.ui.TextInput(label="Member ID", required=True, max_length=25)
    reason = discord.ui.TextInput(label="Reason for imprisonment",
                                  style=discord.TextStyle.paragraph,
                                  required=True, max_length=500)
    term = discord.ui.TextInput(label="Prison term (1h / 1d / 1mo)",
                                required=True, max_length=10)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            mid = int(self.member_id.value.strip())
        except ValueError:
            await interaction.response.send_message("❌ آيدي غير صالح.", ephemeral=True)
            return

        seconds = parse_duration(self.term.value)
        if seconds is None:
            await interaction.response.send_message(
                "❌ صيغة المدة غير صحيحة. استخدم: 1m / 1h / 1d / 1w / 1mo / 1y",
                ephemeral=True)
            return

        member = interaction.guild.get_member(mid)
        if member is None:
            await interaction.response.send_message("❌ لم أجد العضو.", ephemeral=True)
            return

        jail_role = interaction.guild.get_role(JAIL_ROLE_ID)
        if jail_role is None:
            await interaction.response.send_message("❌ رتبة السجن غير موجودة.", ephemeral=True)
            return

        original_roles = [r.id for r in member.roles
                          if r != interaction.guild.default_role
                          and r != jail_role and r.is_assignable() and not r.managed]

        jail_data[str(member.id)] = {
            "roles": original_roles,
            "release_at": int(datetime.datetime.now(timezone.utc).timestamp()) + seconds,
            "reason": self.reason.value,
            "guild_id": interaction.guild.id,
        }
        save_data()

        try:
            roles_to_remove = [r for r in member.roles
                              if r != interaction.guild.default_role and r != jail_role]
            if roles_to_remove:
                await member.remove_roles(*roles_to_remove,
                                          reason=f"Jailed by {interaction.user}")
            await member.add_roles(jail_role, reason=f"Jailed by {interaction.user}")
        except discord.Forbidden:
            await interaction.response.send_message("❌ لا أملك صلاحية إدارة الرتب.", ephemeral=True)
            return

        await interaction.response.send_message(
            f"🔒 تم سجن {member.mention} لمدة `{self.term.value}`.\n**السبب:** {self.reason.value}",
            ephemeral=True)

        log_ch = interaction.guild.get_channel(JAIL_LOG_CHANNEL_ID)
        if log_ch:
            embed = discord.Embed(title="🔒 سجن عضو", color=0xED4245,
                                  timestamp=datetime.datetime.now(timezone.utc))
            embed.add_field(name="العضو", value=member.mention, inline=True)
            embed.add_field(name="بواسطة", value=interaction.user.mention, inline=True)
            embed.add_field(name="المدة", value=f"`{self.term.value}`", inline=True)
            embed.add_field(name="السبب", value=self.reason.value, inline=False)
            embed.set_thumbnail(url=member.display_avatar.url)
            embed.set_footer(text="Powered By [ Xiy_y ]")
            try:
                await log_ch.send(embed=embed)
            except Exception:
                pass


class ReleaseModal(discord.ui.Modal, title="إفراج عن عضو"):
    member_id = discord.ui.TextInput(label="Member ID", required=True, max_length=25)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            mid = int(self.member_id.value.strip())
        except ValueError:
            await interaction.response.send_message("❌ آيدي غير صالح.", ephemeral=True)
            return

        member = interaction.guild.get_member(mid)
        if member is None:
            await interaction.response.send_message("❌ لم أجد العضو.", ephemeral=True)
            return

        data = jail_data.pop(str(member.id), None)
        if data is None:
            await interaction.response.send_message("⚠️ هذا العضو ليس مسجوناً.", ephemeral=True)
            return
        save_data()

        jail_role = interaction.guild.get_role(JAIL_ROLE_ID)
        try:
            if jail_role:
                await member.remove_roles(jail_role, reason=f"Released by {interaction.user}")
            roles_to_add = [interaction.guild.get_role(rid) for rid in data["roles"]]
            roles_to_add = [r for r in roles_to_add if r]
            if roles_to_add:
                await member.add_roles(*roles_to_add, reason=f"Released by {interaction.user}")
        except discord.Forbidden:
            await interaction.response.send_message("❌ لا أملك صلاحية إدارة الرتب.", ephemeral=True)
            return

        await interaction.response.send_message(f"✅ تم الإفراج عن {member.mention}.",
                                                ephemeral=True)

        log_ch = interaction.guild.get_channel(JAIL_LOG_CHANNEL_ID)
        if log_ch:
            embed = discord.Embed(title="✅ إفراج عن عضو", color=0x57F287,
                                  timestamp=datetime.datetime.now(timezone.utc))
            embed.add_field(name="العضو", value=member.mention, inline=True)
            embed.add_field(name="بواسطة", value=interaction.user.mention, inline=True)
            embed.set_thumbnail(url=member.display_avatar.url)
            embed.set_footer(text="Powered By [ Xiy_y ]")
            try:
                await log_ch.send(embed=embed)
            except Exception:
                pass


@tasks.loop(seconds=30)
async def check_jail_expiry():
    now = int(datetime.datetime.now(timezone.utc).timestamp())
    expired = [uid for uid, d in jail_data.items() if d.get("release_at", 0) <= now]
    for uid in expired:
        data = jail_data.pop(uid, None)
        if not data:
            continue
        save_data()
        guild = bot.get_guild(data["guild_id"])
        if guild is None:
            continue
        member = guild.get_member(int(uid))
        if member is None:
            continue
        jail_role = guild.get_role(JAIL_ROLE_ID)
        try:
            if jail_role:
                await member.remove_roles(jail_role, reason="Jail term expired")
            roles_to_add = [guild.get_role(rid) for rid in data["roles"]]
            roles_to_add = [r for r in roles_to_add if r]
            if roles_to_add:
                await member.add_roles(*roles_to_add, reason="Jail term expired")
        except Exception as e:
            print(f"[jail expiry] {e}")


# ============================================================
#                    الأحداث
# ============================================================
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} ({bot.user.id})")
    load_data()
    bot.add_view(WelcomeView())
    bot.add_view(SocialView())
    bot.add_view(ApplicationPanelView())
    bot.add_view(ApplicationReviewView())
    bot.add_view(AppControlView())
    bot.add_view(GiveawayPanelView())
    bot.add_view(EnterGiveawayView())
    bot.add_view(TicketPanelView())
    bot.add_view(TicketInsideView())
    bot.add_view(JailPanelView())
    if not check_jail_expiry.is_running():
        check_jail_expiry.start()
    print("✅ Persistent views registered")


@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    # ✅ نظام الأوامر النصية في كل الرومات
    handled = await handle_ticket_text_commands(message)
    if handled:
        return

    # نظام الريپوستر
    if message.channel.id in REPOSTER_CHANNELS:
        try:
            await message.delete()
        except discord.Forbidden:
            pass
        files = [await a.to_file() for a in message.attachments]
        try:
            await message.channel.send(content=message.content or "", files=files)
            await message.channel.send(DIVIDER_IMAGE)
        except Exception as e:
            print(f"Repost error: {e}")

    await bot.process_commands(message)


@bot.event
async def on_member_update(before: discord.Member, after: discord.Member):
    if before.premium_since is None and after.premium_since is not None:
        channel = bot.get_channel(BOOST_CHANNEL_ID)
        if channel is None:
            return
        embed = discord.Embed(
            title="🚀 iMLKq Community - Thanks For The Boost",
            description=(
                f"شكراً لك {after.mention} على دعم سيرفر iMLKq Community!\n\n"
                f"نُقدر دعمك المستمر لمجتمعنا 💙"
            ),
            color=BOOST_EMBED_COLOR,
        )
        embed.set_thumbnail(url=THUMBNAIL)
        embed.set_image(url=BOOST_BANNER)
        embed.set_footer(text="Powered By [ Xiy_y ]")
        try:
            await channel.send(
                content=f"{after.mention} just boosted ** iMLKq Community **!",
                embed=embed,
            )
        except Exception as e:
            print(f"Boost error: {e}")


# ============================================================
#                    الأوامر
# ============================================================
@bot.command(name="setup_welcome")
@commands.has_permissions(manage_guild=True)
async def setup_welcome(ctx):
    description = (
        "مرحبا بك في سيرفر **iMLKq Community** يرجى قراءة القوانين أدناة بعناية لإنشاء بيئة خالية من المخربين واؤلئك الذين لا يلتمزون بالقوانين "
        "يرجى ملاحظة اي شخص يخالف القوانين سيتم معاقبته إداريا للحفاظ على مجتمع خاليا من المشاكل\n\n"
        "> Welcome to the **iMLKq Community** server. Please read the rules below carefully to help create a safe environment free from troublemakers. "
        "Kindly note that anyone who violates the rules will be subject to administrative action in order to maintain a community free of issues\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    )
    embed = discord.Embed(description=description, color=0x2b2d31)
    embed.set_image(url=WELCOME_BANNER)
    await ctx.send(embed=embed, view=WelcomeView())


@bot.command(name="setup_app")
@commands.has_permissions(manage_guild=True)
async def setup_app(ctx):
    await send_image_with_view(ctx.channel, APP_PANEL_IMAGE,
                               ApplicationPanelView(), "app_panel.png")


@bot.command(name="setup_control")
@commands.has_permissions(manage_guild=True)
async def setup_control(ctx):
    await send_image_with_view(ctx.channel, CONTROL_PANEL_IMAGE,
                               AppControlView(), "control_panel.png")


@bot.command(name="setup_giveaways")
@commands.has_permissions(manage_guild=True)
async def setup_giveaways(ctx):
    await send_image_with_view(ctx.channel, GIVEAWAY_PANEL_IMAGE,
                               GiveawayPanelView(), "giveaway_panel.png")


@bot.command(name="setup_tickets")
@commands.has_permissions(manage_guild=True)
async def setup_tickets(ctx):
    await send_image_with_view(ctx.channel, TICKET_PANEL_IMAGE,
                               TicketPanelView(), "ticket_panel.png")


@bot.command(name="setup_jail")
@commands.has_permissions(manage_guild=True)
async def setup_jail(ctx):
    await send_image_with_view(ctx.channel, JAIL_PANEL_IMAGE,
                               JailPanelView(), "jail_panel.png")


@bot.command(name="setup_all")
@commands.has_permissions(manage_guild=True)
async def setup_all(ctx: commands.Context):
    """يرسل كل البانلات دفعة واحدة في روماتها المخصصة"""
    guild = ctx.guild
    report = []

    # 1) الترحيب
    welcome_ch = guild.get_channel(WELCOME_CHANNEL_ID)
    if welcome_ch:
        try:
            description = (
                "مرحبا بك في سيرفر **iMLKq Community** يرجى قراءة القوانين أدناة بعناية لإنشاء بيئة خالية من المخربين واؤلئك الذين لا يلتمزون بالقوانين "
                "يرجى ملاحظة اي شخص يخالف القوانين سيتم معاقبته إداريا للحفاظ على مجتمع خاليا من المشاكل\n\n"
                "> Welcome to the **iMLKq Community** server. Please read the rules below carefully to help create a safe environment free from troublemakers. "
                "Kindly note that anyone who violates the rules will be subject to administrative action in order to maintain a community free of issues\n\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
            )
            embed = discord.Embed(description=description, color=0x2b2d31)
            embed.set_image(url=WELCOME_BANNER)
            await welcome_ch.send(embed=embed, view=WelcomeView())
            report.append(f"✅ الترحيب → {welcome_ch.mention}")
        except Exception as e:
            report.append(f"❌ الترحيب: {e}")
    else:
        report.append("❌ لم أجد روم الترحيب")

    # 2) التقديمات
    app_ch = guild.get_channel(APP_PANEL_CHANNEL_ID)
    if app_ch:
        try:
            await send_image_with_view(app_ch, APP_PANEL_IMAGE,
                                       ApplicationPanelView(), "app_panel.png")
            report.append(f"✅ التقديمات → {app_ch.mention}")
        except Exception as e:
            report.append(f"❌ التقديمات: {e}")
    else:
        report.append("❌ لم أجد روم التقديمات")

    # 3) لوحة التحكم
    ctrl_ch = guild.get_channel(APP_CONTROL_CHANNEL_ID)
    if ctrl_ch:
        try:
            await send_image_with_view(ctrl_ch, CONTROL_PANEL_IMAGE,
                                       AppControlView(), "control_panel.png")
            report.append(f"✅ لوحة التحكم → {ctrl_ch.mention}")
        except Exception as e:
            report.append(f"❌ لوحة التحكم: {e}")
    else:
        report.append("❌ لم أجد روم لوحة التحكم")

    # 4) السحوبات
    gv_ch = guild.get_channel(GIVEAWAY_CHANNEL_ID)
    if gv_ch:
        try:
            await send_image_with_view(gv_ch, GIVEAWAY_PANEL_IMAGE,
                                       GiveawayPanelView(), "giveaway_panel.png")
            report.append(f"✅ السحوبات → {gv_ch.mention}")
        except Exception as e:
            report.append(f"❌ السحوبات: {e}")
    else:
        report.append("❌ لم أجد روم السحوبات")

    # 5) التكتات
    tk_ch = guild.get_channel(TICKET_PANEL_CHANNEL_ID)
    if tk_ch:
        try:
            await send_image_with_view(tk_ch, TICKET_PANEL_IMAGE,
                                       TicketPanelView(), "ticket_panel.png")
            report.append(f"✅ التكتات → {tk_ch.mention}")
        except Exception as e:
            report.append(f"❌ التكتات: {e}")
    else:
        report.append("❌ لم أجد روم التكتات")

    # 6) السجن
    jail_ch = guild.get_channel(JAIL_PANEL_CHANNEL_ID)
    if jail_ch:
        try:
            await send_image_with_view(jail_ch, JAIL_PANEL_IMAGE,
                                       JailPanelView(), "jail_panel.png")
            report.append(f"✅ السجن → {jail_ch.mention}")
        except Exception as e:
            report.append(f"❌ السجن: {e}")
    else:
        report.append("❌ لم أجد روم السجن")

    # التقرير
    embed = discord.Embed(
        title="📋 تقرير إرسال البانلات",
        description="\n".join(report),
        color=0x16c7f0,
        timestamp=datetime.datetime.now(timezone.utc),
    )
    embed.set_footer(text="Powered By [ Xiy_y ]")
    try:
        await ctx.send(embed=embed)
    except Exception:
        pass


# ============================================================
#                    تشغيل البوت
# ============================================================
bot.run(TOKEN)