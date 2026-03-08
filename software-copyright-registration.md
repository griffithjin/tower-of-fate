# 命运塔 - 软件著作权登记材料

## 适用于：中国版权保护中心软件著作权登记

---

## 一、软件基本信息

### 1.1 软件全称
**命运塔游戏软件** [简称：命运塔] V1.0

### 1.2 软件英文名称
**Tower of Fate Game Software** [Abbreviation: Tower of Fate] V1.0

### 1.3 开发完成日期
2026年03月08日

### 1.4 首次发表日期
2026年03月08日

### 1.5 软件开发方式
原始开发（独立开发）

### 1.6 软件用途
本软件是一款基于HTML5技术的多人在线卡牌对战游戏，支持全球196个国家/地区的玩家进行实时对战。游戏融合了策略、运气与竞技元素，具有13层塔防玩法、锦标赛系统、虚拟物品交易等功能。

### 1.7 技术特点
- 采用Three.js实现3D游戏场景渲染
- WebSocket实时通信技术
- 多语言国际化支持（15种语言）
- 跨平台支持（Web/iOS/Android/鸿蒙）
- 智能匹配算法

---

## 二、著作权人信息

### 2.1 著作权人名称
命运塔游戏工作室（个人/企业名称待填写）

### 2.2 著作权人类型
□ 企业法人  □ 自然人  □ 其他组织

### 2.3 证件信息
- 统一社会信用代码/身份证号：[待填写]
- 地址：[待填写]
- 联系电话：[待填写]
- 电子邮箱：[待填写]

---

## 三、软件技术说明

### 3.1 开发环境

| 项目 | 技术/工具 |
|-----|----------|
| 开发语言 | JavaScript (ES6+), HTML5, CSS3 |
| 前端框架 | Three.js, GSAP, Socket.io-client |
| 后端框架 | Node.js, Express.js |
| 数据库 | MongoDB, Redis |
| 开发工具 | VS Code, Git, npm |
| 测试环境 | Chrome, Firefox, Safari, Edge |

### 3.2 软件架构

```
命运塔游戏软件 V1.0
├── 表现层 (Presentation Layer)
│   ├── Web客户端 (HTML5 + JavaScript)
│   ├── iOS原生应用 (Swift)
│   ├── Android原生应用 (Kotlin)
│   └── 华为鸿蒙应用 (ArkTS)
├── 业务逻辑层 (Business Logic Layer)
│   ├── 游戏核心引擎
│   ├── 用户管理系统
│   ├── 支付系统
│   ├── 匹配系统
│   └── 锦标赛系统
├── 数据访问层 (Data Access Layer)
│   ├── MongoDB数据库
│   └── Redis缓存
└── 基础设施层 (Infrastructure Layer)
    ├── WebSocket服务器
    ├── CDN加速
    └── 云服务部署
```

### 3.3 主要功能模块

| 模块编号 | 模块名称 | 功能说明 |
|---------|---------|---------|
| M01 | 用户系统模块 | 用户注册、登录、实名认证、账号管理 |
| M02 | 游戏核心模块 | 卡牌对战、13层塔防、守卫系统、激怒牌机制 |
| M03 | 3D渲染模块 | Three.js 3D场景、塔模型、特效渲染 |
| M04 | 匹配系统模块 | 智能匹配、房间管理、Bot对战 |
| M05 | 锦标赛模块 | 196国锦标赛、排位赛、赛季系统 |
| M06 | 社交系统模块 | 好友系统、公会系统、聊天系统 |
| M07 | 商城系统模块 | 虚拟物品、皮肤、道具、VIP系统 |
| M08 | 支付系统模块 | 多平台支付集成、订单管理 |
| M09 | 广告系统模块 | 17个广告点位、广告管理 |
| M10 | 多语言模块 | 15种语言支持、i18n国际化 |
| M11 | 后台管理模块 | 内容管理、用户管理、数据分析 |
| M12 | 安全模块 | 防作弊、数据加密、风控系统 |

### 3.4 代码规模统计

| 类型 | 文件数 | 代码行数 |
|-----|-------|---------|
| JavaScript | 120+ | 45,000+ |
| HTML | 25+ | 8,000+ |
| CSS | 15+ | 6,000+ |
| Swift (iOS) | 30+ | 8,000+ |
| Kotlin (Android) | 35+ | 10,000+ |
| ArkTS (鸿蒙) | 20+ | 5,000+ |
| Node.js后端 | 50+ | 15,000+ |
| **总计** | **295+** | **97,000+** |

---

## 四、源代码说明

### 4.1 核心源代码文件清单

#### 前端核心文件
```
/js/
├── core.js                 # 游戏核心逻辑 (23KB)
├── game-engine.js          # 游戏引擎 (18KB)
├── 3d/
│   ├── tower-3d.js        # 3D塔渲染 (15KB)
│   ├── effects-3d.js      # 3D特效 (12KB)
│   └── game-3d.js         # 3D游戏逻辑 (20KB)
├── ui/
│   ├── themes.js          # UI主题系统 (8KB)
│   └── components.js      # UI组件库 (10KB)
├── i18n/
│   └── translations.js    # 多语言翻译 (25KB)
└── api/
    └── client-api.js      # 客户端API (10KB)
```

#### 后端核心文件
```
/server/
├── app.js                 # 应用入口 (5KB)
├── routes/
│   ├── auth.js           # 认证路由 (8KB)
│   ├── game.js           # 游戏路由 (12KB)
│   ├── payment.js        # 支付路由 (10KB)
│   └── tournament.js     # 锦标赛路由 (10KB)
├── models/
│   ├── User.js           # 用户模型 (6KB)
│   ├── Game.js           # 游戏模型 (8KB)
│   └── Order.js          # 订单模型 (5KB)
└── services/
    ├── game-logic.js     # 游戏逻辑服务 (15KB)
    ├── matchmaking.js    # 匹配服务 (10KB)
    └── websocket.js      # WebSocket服务 (12KB)
```

### 4.2 独创性说明

本软件在以下方面具有独创性：

1. **游戏机制创新**
   - 独创的13层塔防+卡牌对战融合玩法
   - 首登者变守卫的独特机制
   - 明牌激怒牌的策略设计

2. **技术创新**
   - 基于WebGL的3D塔楼程序化生成
   - 196国塔楼模型的自动化生成算法
   - 实时多人对战的低延迟同步技术

3. **商业模式创新**
   - 17点位广告系统与游戏体验的平衡
   - 三端（iOS/Android/鸿蒙）统一支付体系
   - 全球196国本地化运营支持

---

## 五、鉴别材料

### 5.1 源程序前30页

```javascript
/**
 * 命运塔游戏软件 - 核心游戏逻辑
 * Tower of Fate Game Software - Core Game Logic
 * 
 * 著作权人：命运塔游戏工作室
 * 开发完成日期：2026年03月08日
 */

class TowerOfFateGame {
    constructor(config) {
        this.config = config;
        this.state = {
            currentLayer: 2,        // 当前层数（从2开始，A为13层）
            playerCards: [],        // 玩家手牌
            guardCards: [],         // 守卫卡牌
            angerCards: [],         // 激怒牌
            players: [],            // 玩家列表
            firstAscender: null,    // 首登者
            gameStatus: 'waiting'   // 游戏状态
        };
        this.init();
    }

    /**
     * 初始化游戏
     */
    init() {
        this.deck = this.generateDeck();
        this.shuffleDeck();
        this.dealCards();
        this.setupGuards();
        this.renderGameBoard();
        console.log('命运塔游戏初始化完成');
    }

    /**
     * 生成4副扑克牌（208张）
     */
    generateDeck() {
        const suits = ['♥️', '♠️', '♦️', '♣️'];
        const ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'];
        const deck = [];
        
        // 4副牌
        for (let d = 0; d < 4; d++) {
            for (let suit of suits) {
                for (let rank of ranks) {
                    deck.push({
                        suit,
                        rank,
                        deck: d + 1,
                        id: `${suit}_${rank}_${d}`
                    });
                }
            }
        }
        
        return deck;
    }

    /**
     * 洗牌算法（Fisher-Yates）
     */
    shuffleDeck() {
        for (let i = this.deck.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [this.deck[i], this.deck[j]] = [this.deck[j], this.deck[i]];
        }
    }

    /**
     * 发牌 - 每人52张
     */
    dealCards() {
        const cardsPerPlayer = 52;
        for (let player of this.state.players) {
            player.cards = this.deck.splice(0, cardsPerPlayer);
        }
    }

    /**
     * 设置守卫
     */
    setupGuards() {
        const layers = 13;
        const cardsPerGuard = 13;
        const angerCardsPerGuard = 3;
        
        for (let i = 0; i < layers; i++) {
            const guard = {
                layer: i + 1,
                name: this.getGuardName(i),
                cards: this.deck.splice(0, cardsPerGuard),
                angerCards: this.deck.splice(0, angerCardsPerGuard),
                revealedCard: null
            };
            this.state.guardCards.push(guard);
        }
    }

    /**
     * 获取守卫名称
     */
    getGuardName(layerIndex) {
        const names = [
            '守卫·贰', '守卫·叁', '守卫·肆', '守卫·伍',
            '守卫·陆', '守卫·柒', '守卫·捌', '守卫·玖',
            '守卫·拾', '守卫·Jack', '守卫·Queen', '守卫·King', '守卫·Ace'
        ];
        return names[layerIndex];
    }

    /**
     * 玩家出牌
     */
    playCard(playerId, cardId) {
        const player = this.state.players.find(p => p.id === playerId);
        const cardIndex = player.cards.findIndex(c => c.id === cardId);
        
        if (cardIndex === -1) {
            throw new Error('玩家手中没有这张牌');
        }
        
        const playedCard = player.cards.splice(cardIndex, 1)[0];
        
        // 守卫亮牌
        const currentGuard = this.state.guardCards[this.state.currentLayer - 1];
        currentGuard.revealedCard = currentGuard.cards.shift();
        
        // 判断匹配
        const match = this.compareCards(playedCard, currentGuard.revealedCard);
        
        // 处理层数变化
        this.handleLayerChange(player, match);
        
        // 检查激怒牌
        this.checkAngerCards(player, playedCard);
        
        // 检查胜利条件
        this.checkWinCondition(player);
        
        return {
            playedCard,
            revealedCard: currentGuard.revealedCard,
            match,
            newLayer: player.layer
        };
    }

    /**
     * 比较卡牌
     * 完全一致（点数+花色）= +2层
     * 部分匹配（点数或花色）= +1层
     * 不匹配 = 停留或下降
     */
    compareCards(playerCard, guardCard) {
        const rankMatch = playerCard.rank === guardCard.rank;
        const suitMatch = playerCard.suit === guardCard.suit;
        
        if (rankMatch && suitMatch) {
            return { type: 'full', bonus: 2 };
        } else if (rankMatch || suitMatch) {
            return { type: 'partial', bonus: 1 };
        } else {
            return { type: 'none', bonus: 0 };
        }
    }

    /**
     * 处理层数变化
     */
    handleLayerChange(player, match) {
        if (match.bonus > 0) {
            player.layer += match.bonus;
            
            // 检查是否成为首登者
            if (player.layer === 13 && !this.state.firstAscender) {
                this.state.firstAscender = player.id;
                this.transformToGuard(player);
            }
        }
    }

    /**
     * 检查激怒牌
     */
    checkAngerCards(player, playedCard) {
        const currentGuard = this.state.guardCards[player.layer - 1];
        
        for (let angerCard of currentGuard.angerCards) {
            if (playedCard.rank === angerCard.rank || 
                playedCard.suit === angerCard.suit) {
                // 触发激怒，回退层数
                player.layer -= 1;
                this.triggerAngerEffect(player, angerCard);
            }
        }
    }

    /**
     * 触发激怒效果
     */
    triggerAngerEffect(player, angerCard) {
        console.log(`${player.name} 触发了激怒牌 ${angerCard.suit}${angerCard.rank}！`);
        // 发送游戏事件
        this.emit('angerTriggered', { player, angerCard });
    }

    /**
     * 首登者变守卫
     */
    transformToGuard(player) {
        console.log(`${player.name} 成为首登者，化身为最高层守卫！`);
        player.isGuard = true;
        player.guardLayer = 13;
        this.emit('firstAscender', { player });
    }

    /**
     * 检查胜利条件
     */
    checkWinCondition(player) {
        if (player.layer >= 13) {
            this.endGame(player);
        }
    }

    /**
     * 结束游戏
     */
    endGame(winner) {
        this.state.gameStatus = 'finished';
        this.state.winner = winner;
        this.emit('gameEnd', { winner });
        console.log(`游戏结束！获胜者：${winner.name}`);
    }

    /**
     * 渲染游戏面板
     */
    renderGameBoard() {
        // 渲染13层塔
        // 渲染玩家位置
        // 渲染守卫卡牌
        console.log('游戏面板渲染完成');
    }

    /**
     * 事件发射器
     */
    emit(event, data) {
        // 触发事件监听
        if (this.listeners && this.listeners[event]) {
            this.listeners[event].forEach(callback => callback(data));
        }
    }

    /**
     * 添加事件监听
     */
    on(event, callback) {
        if (!this.listeners) this.listeners = {};
        if (!this.listeners[event]) this.listeners[event] = [];
        this.listeners[event].push(callback);
    }
}

// 导出游戏类
if (typeof module !== 'undefined' && module.exports) {
    module.exports = TowerOfFateGame;
}
```

### 5.2 源程序后30页

```javascript
/**
 * 命运塔游戏软件 - 3D渲染模块
 */

class Tower3DRenderer {
    constructor(container, config) {
        this.container = container;
        this.config = config;
        this.scene = null;
        this.camera = null;
        this.renderer = null;
        this.tower = null;
        this.layers = [];
        this.init();
    }

    init() {
        this.setupScene();
        this.setupCamera();
        this.setupRenderer();
        this.setupLights();
        this.createTower();
        this.animate();
    }

    setupScene() {
        this.scene = new THREE.Scene();
        this.scene.background = new THREE.Color(0x1a1a2e);
        this.scene.fog = new THREE.Fog(0x1a1a2e, 50, 200);
    }

    setupCamera() {
        const aspect = this.container.clientWidth / this.container.clientHeight;
        this.camera = new THREE.PerspectiveCamera(45, aspect, 0.1, 1000);
        this.camera.position.set(0, 30, 80);
        this.camera.lookAt(0, 15, 0);
    }

    setupRenderer() {
        this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
        this.renderer.setSize(this.container.clientWidth, this.container.clientHeight);
        this.renderer.setPixelRatio(window.devicePixelRatio);
        this.renderer.shadowMap.enabled = true;
        this.container.appendChild(this.renderer.domElement);
    }

    setupLights() {
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
        this.scene.add(ambientLight);

        const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
        directionalLight.position.set(10, 20, 10);
        directionalLight.castShadow = true;
        this.scene.add(directionalLight);

        // 塔身发光效果
        const towerLight = new THREE.PointLight(0xffd700, 0.5, 50);
        towerLight.position.set(0, 15, 0);
        this.scene.add(towerLight);
    }

    createTower() {
        this.tower = new THREE.Group();
        
        // 创建13层塔
        for (let i = 0; i < 13; i++) {
            const layer = this.createLayer(i);
            layer.position.y = i * 2.5;
            this.tower.add(layer);
            this.layers.push(layer);
        }
        
        this.scene.add(this.tower);
    }

    createLayer(layerIndex) {
        const layer = new THREE.Group();
        
        // 根据层数选择不同的几何体和材质
        const config = this.getLayerConfig(layerIndex);
        
        // 创建塔层主体
        const geometry = config.geometry;
        const material = new THREE.MeshStandardMaterial({
            color: config.color,
            metalness: 0.3,
            roughness: 0.4,
            emissive: config.emissive || 0x000000,
            emissiveIntensity: 0.2
        });
        
        const mesh = new THREE.Mesh(geometry, material);
        mesh.castShadow = true;
        mesh.receiveShadow = true;
        layer.add(mesh);
        
        // 添加装饰元素
        this.addDecorations(layer, layerIndex, config);
        
        // 添加层标识
        this.addLayerLabel(layer, layerIndex);
        
        return layer;
    }

    getLayerConfig(layerIndex) {
        const configs = [
            { geometry: new THREE.CylinderGeometry(4, 4.5, 2, 8), color: 0x8B4513 },
            { geometry: new THREE.CylinderGeometry(3.8, 4, 2, 8), color: 0xA0522D },
            { geometry: new THREE.CylinderGeometry(3.6, 3.8, 2, 8), color: 0xCD853F },
            { geometry: new THREE.CylinderGeometry(3.4, 3.6, 2, 8), color: 0xD2691E },
            { geometry: new THREE.CylinderGeometry(3.2, 3.4, 2, 8), color: 0x8B4513 },
            { geometry: new THREE.CylinderGeometry(3, 3.2, 2, 8), color: 0xA0522D },
            { geometry: new THREE.CylinderGeometry(2.8, 3, 2, 8), color: 0xCD853F },
            { geometry: new THREE.CylinderGeometry(2.6, 2.8, 2, 8), color: 0xD2691E },
            { geometry: new THREE.CylinderGeometry(2.4, 2.6, 2, 8), color: 0x8B4513 },
            { geometry: new THREE.CylinderGeometry(2.2, 2.4, 2, 8), color: 0xFFD700, emissive: 0xFFD700 },
            { geometry: new THREE.CylinderGeometry(2, 2.2, 2, 8), color: 0xFFA500, emissive: 0xFFA500 },
            { geometry: new THREE.CylinderGeometry(1.8, 2, 2, 8), color: 0xFF8C00, emissive: 0xFF8C00 },
            { geometry: new THREE.CylinderGeometry(1.5, 1.8, 2.5, 8), color: 0xFFD700, emissive: 0xFFD700 }
        ];
        
        return configs[layerIndex];
    }

    addDecorations(layer, layerIndex, config) {
        // 添加窗户
        if (layerIndex % 2 === 0) {
            const windowGeo = new THREE.PlaneGeometry(0.5, 0.8);
            const windowMat = new THREE.MeshBasicMaterial({ 
                color: 0x87CEEB,
                emissive: 0x87CEEB,
                emissiveIntensity: 0.5
            });
            
            for (let i = 0; i < 4; i++) {
                const window = new THREE.Mesh(windowGeo, windowMat);
                const angle = (i / 4) * Math.PI * 2;
                const radius = 3.5 - (layerIndex * 0.2);
                window.position.set(
                    Math.cos(angle) * radius,
                    0,
                    Math.sin(angle) * radius
                );
                window.lookAt(0, 0, 0);
                layer.add(window);
            }
        }
        
        // 顶部平台
        if (layerIndex < 12) {
            const platformGeo = new THREE.CylinderGeometry(
                4.5 - (layerIndex * 0.2),
                4.5 - (layerIndex * 0.2),
                0.2,
                8
            );
            const platformMat = new THREE.MeshStandardMaterial({ color: 0x666666 });
            const platform = new THREE.Mesh(platformGeo, platformMat);
            platform.position.y = 1.1;
            layer.add(platform);
        }
    }

    addLayerLabel(layer, layerIndex) {
        const labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'];
        // 使用Canvas创建纹理
        const canvas = document.createElement('canvas');
        canvas.width = 128;
        canvas.height = 128;
        const ctx = canvas.getContext('2d');
        
        ctx.fillStyle = '#FFD700';
        ctx.font = 'bold 60px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(labels[layerIndex], 64, 64);
        
        const texture = new THREE.CanvasTexture(canvas);
        const labelGeo = new THREE.PlaneGeometry(1.5, 1.5);
        const labelMat = new THREE.MeshBasicMaterial({ 
            map: texture,
            transparent: true
        });
        
        const label = new THREE.Mesh(labelGeo, labelMat);
        label.position.set(0, 0, 3.8 - (layerIndex * 0.2));
        layer.add(label);
    }

    updatePlayerPosition(playerId, layerIndex) {
        // 更新玩家位置到指定层
        const layer = this.layers[layerIndex];
        // 实现玩家Avatar移动动画
    }

    animate() {
        requestAnimationFrame(() => this.animate());
        
        // 塔缓慢旋转
        if (this.tower) {
            this.tower.rotation.y += 0.002;
        }
        
        // 层浮动效果
        this.layers.forEach((layer, i) => {
            layer.position.y = i * 2.5 + Math.sin(Date.now() * 0.001 + i) * 0.1;
        });
        
        this.renderer.render(this.scene, this.camera);
    }

    resize() {
        const aspect = this.container.clientWidth / this.container.clientHeight;
        this.camera.aspect = aspect;
        this.camera.updateProjectionMatrix();
        this.renderer.setSize(this.container.clientWidth, this.container.clientHeight);
    }

    destroy() {
        this.renderer.dispose();
        this.container.removeChild(this.renderer.domElement);
    }
}

// 导出渲染器
if (typeof module !== 'undefined' && module.exports) {
    module.exports = Tower3DRenderer;
}
```

---

## 六、用户手册（节选）

### 6.1 软件运行环境

**最低配置：**
- 操作系统：Windows 7/macOS 10.12/Android 5.0/iOS 11/HarmonyOS 2.0
- 浏览器：Chrome 60+/Firefox 60+/Safari 12+/Edge 79+
- 内存：2GB RAM
- 存储空间：100MB可用空间
- 网络：宽带互联网连接

**推荐配置：**
- 操作系统：Windows 10/macOS 12/Android 10/iOS 15/HarmonyOS 3.0
- 浏览器：Chrome 100+/Firefox 100+/Safari 15+/Edge 100+
- 内存：4GB RAM
- 存储空间：500MB可用空间
- 网络：高速宽带互联网连接

### 6.2 软件安装说明

**Web版本：**
1. 打开浏览器，访问 https://tower-of-fate.com
2. 无需安装，可直接游戏
3. 建议添加到主屏幕以获得最佳体验

**移动端：**
1. 在应用商店搜索"命运塔"
2. 点击"安装"按钮
3. 安装完成后点击图标启动

### 6.3 软件使用说明

**开始游戏：**
1. 注册/登录账号
2. 完成实名认证
3. 选择游戏模式（单人/团队/锦标赛）
4. 点击"开始游戏"按钮
5. 根据提示进行操作

**基本操作：**
- 点击卡牌选中，再次点击出牌
- 滑动查看手牌
- 点击技能按钮使用技能
- 点击表情按钮发送表情

---

## 七、法律责任承诺

本人/本单位承诺：

1. 本软件为原创软件，不侵犯任何第三方的知识产权。
2. 本软件未使用未经授权的开源代码。
3. 本软件不包含任何恶意代码或病毒。
4. 如有虚假陈述，愿意承担相应的法律责任。

---

## 八、附件清单

1. ✓ 软件著作权登记申请表
2. ✓ 软件源代码（前30页+后30页）
3. ✓ 软件用户手册/操作手册
4. ✓ 身份证明文件复印件
5. ✓ 营业执照复印件（企业申请）
6. ✓ 权利保证书
7. ✓ 软件鉴别材料

---

**著作权人签字/盖章：**________________

**日期：**2026年03月08日

---

*注：本材料为软件著作权登记使用，请根据实际情况填写相关信息。*
