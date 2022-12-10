from tools.lark_bot.lark import LarkReport


def main():
    lark = LarkReport()
    msg = {"msg_type": "text", "content": {"text": "TODO"}}
    lark.pack(msg=msg)
    lark.report()


if __name__ == "__main__":
    main()