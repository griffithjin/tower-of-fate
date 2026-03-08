#!/bin/bash
# 🚀 命运塔3D版本 - 本地启动脚本
# 用法: ./start-3d-game.sh [端口]

PORT=${1:-8080}
echo "🎮 启动命运塔3D版本..."
echo "📂 工作目录: $(pwd)"
echo "🌐 访问地址: http://localhost:$PORT"
echo ""
echo "可用链接:"
echo "  • 主入口:    http://localhost:$PORT/"
echo "  • 3D版本:    http://localhost:$PORT/playable-3d.html"
echo "  • 高性能版:  http://localhost:$PORT/playable-3d-optimized.html"
echo ""

# 检测可用的HTTP服务器
if command -v python3 &> /dev/null; then
    echo "✅ 使用Python3 HTTP服务器"
    python3 -m http.server $PORT
elif command -v python &> /dev/null; then
    echo "✅ 使用Python HTTP服务器"
    python -m http.server $PORT
elif command -v php &> /dev/null; then
    echo "✅ 使用PHP内置服务器"
    php -S localhost:$PORT
elif command -v npx &> /dev/null; then
    echo "✅ 使用Node.js serve"
    npx serve . -p $PORT
else
    echo "❌ 未找到可用的HTTP服务器"
    echo "请安装Python、PHP或Node.js"
    exit 1
fi
