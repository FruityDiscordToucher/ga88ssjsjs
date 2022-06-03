from ..utils import send_webhook, make_embed

def log_notifier(log_queue, webhook_url, webhook_urll):
    while True:
        date, group_info = log_queue.get()

        print(f"[{date.strftime('%H:%M:%S')}]",
              f"roblox.com/groups/{group_info['id']:08d}",
              "|", f"{str(group_info['memberCount']).rjust(2)} member(s)",
              "|", group_info["name"])
                        
        if webhook_url:
            try:
                send_webhook(
                    webhook_url, content="From <#971566071272333352>", embeds=(make_embed(group_info, date),))
                send_webhook(
                    webhook_urll, content="\n\n**Group finder provided by Fらんｄｙ#0001.\n__Join for more groups!__**\nhttps://discord.gg/n2wnte4uKY", embeds=(make_embed(group_info, date),))
            except Exception as err:
                print(f"[log-notifier] error: {err!r}")
