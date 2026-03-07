#!/bin/bash
# 命运塔监控脚本 - 每30分钟执行一次（使用浏览器截图方式）
# 创建时间: 2026-03-06
# 监控目标: https://griffithjin.github.io/toweroffate-v1/playable.html

LOG_FILE="/Users/moutai/.openclaw/workspace/toweroffate_monitor.log"
SCREENSHOT_DIR="/Users/moutai/.openclaw/workspace/toweroffate_screenshots"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

echo "[$TIMESTAMP] 开始监控任务..." >> $LOG_FILE

# 确保目录存在
mkdir -p "$SCREENSHOT_DIR"

# 使用OpenClaw browser工具截图（通过API调用）
SCREENSHOT_FILE="$SCREENSHOT_DIR/toweroffate_${TIMESTAMP}.png"
LOG_JSON="/tmp/toweroffate_browser_${TIMESTAMP}.json"

echo "[$TIMESTAMP] 正在使用浏览器截图..." >> $LOG_FILE

# 调用OpenClaw browser截图
# 注意：这个脚本应该由OpenClaw Agent执行，或者通过agent-browser CLI
# 这里记录请求，实际截图由Agent处理

cat > "$LOG_JSON" << EOF
{
  "timestamp": "$TIMESTAMP",
  "action": "screenshot",
  "url": "https://griffithjin.github.io/toweroffate-v1/playable.html",
  "target_file": "$SCREENSHOT_FILE",
  "status": "pending"
}
EOF

echo "[$TIMESTAMP] ✅ 截图请求已记录: $SCREENSHOT_FILE" >> $LOG_FILE

# 如果agent-browser CLI可用，直接执行
if command -v agent-browser &> /dev/null; then
    agent-browser screenshot "https://griffithjin.github.io/toweroffate-v1/playable.html" "$SCREENSHOT_FILE" 2>/dev/null
    if [ $? -eq 0 ]; then
        echo "[$TIMESTAMP] ✅ 浏览器截图成功" >> $LOG_FILE
    else
        echo "[$TIMESTAMP] ⚠️ 浏览器截图失败，将由Agent异步处理" >> $LOG_FILE
    fi
else
    echo "[$TIMESTAMP] ℹ️ agent-browser CLI未安装，截图将由OpenClaw Agent异步执行" >> $LOG_FILE
fi

# 检查页面是否有更新（通过之前的截图哈希比对）
PREV_HASH_FILE="/tmp/toweroffate_prev_hash.txt"
if [ -f "$SCREENSHOT_FILE" ]; then
    CURRENT_HASH=$(md5 -q "$SCREENSHOT_FILE" 2>/dev/null || echo "")
    if [ -f "$PREV_HASH_FILE" ]; then
        PREV_HASH=$(cat "$PREV_HASH_FILE")
        if [ "$CURRENT_HASH" != "$PREV_HASH" ] && [ -n "$CURRENT_HASH" ]; then
            echo "[$TIMESTAMP] ⚠️ 检测到页面视觉变化!" >> $LOG_FILE
            # TODO: 发送通知（集成飞书）
        fi
    fi
    echo "$CURRENT_HASH" > "$PREV_HASH_FILE"
fi

echo "[$TIMESTAMP] ✅ 监控完成" >> $LOG_FILE
echo "---" >> $LOG_FILE
