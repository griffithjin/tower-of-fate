#!/bin/bash
# 命运塔监控触发器 - 每5分钟执行
# 此脚本由系统cron每5分钟调用，创建触发文件通知Agent执行

TRIGGER_FILE="/Users/moutai/.openclaw/workspace/.toweroffate_trigger_$(date +%Y%m%d_%H%M).flag"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# 创建带时间戳的触发文件
echo "$TIMESTAMP" > "$TRIGGER_FILE"

# 记录触发日志
echo "[$TIMESTAMP] 监控触发信号已发出 - 等待Agent执行" >> /Users/moutai/.openclaw/workspace/toweroffate_trigger.log

# 清理旧的触发文件(保留最近10个)
ls -t /Users/moutai/.openclaw/workspace/.toweroffate_trigger_*.flag 2>/dev/null | tail -n +11 | xargs rm -f 2>/dev/null
