#!/bin/bash
curl -X POST -H "Content-Type: application/json" \
	-d '{"msg_type":"text","content":{"text":"TODO"}}' \
    https://open.feishu.cn/open-apis/bot/v2/hook/
