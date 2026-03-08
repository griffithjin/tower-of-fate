# 命运塔 - 全要素后台配置系统

## 系统架构

```
前端游戏界面 ←→ 后台配置中心
    ↓                    ↓
  用户可见            管理员配置
  实时生效            即时同步
```

---

## 1. 按钮配置系统

### 1.1 游戏主界面按钮

```javascript
// config/buttons/main-menu.js

const MAIN_MENU_BUTTONS = {
    // 开始游戏按钮
    'btn-start-game': {
        id: 'btn-start-game',
        enabled: true,
        texts: {
            'zh-CN': '开始游戏',
            'en-US': 'Start Game',
            'ja-JP': 'ゲーム開始',
            'ko-KR': '게임 시작',
            'de-DE': 'Spiel Starten',
            'fr-FR': 'Commencer',
            'es-ES': 'Iniciar Juego',
            'pt-BR': 'Iniciar Jogo',
            'ru-RU': 'Начать Игру',
            'ar-SA': 'بدء اللعبة',
            'hi-IN': 'खेल शुरू करें',
            'th-TH': 'เริ่มเกม',
            'vi-VN': 'Bắt đầu',
            'id-ID': 'Mulai Game',
            'tr-TR': 'Oyuna Başla'
        },
        style: {
            backgroundColor: '#FFD700',
            textColor: '#1A1A2E',
            fontSize: '18px',
            borderRadius: '25px',
            padding: '15px 40px'
        },
        icon: '▶️',
        redirect: null, // 无跳转，执行游戏逻辑
        action: 'startGame',
        visibility: { guest: true, user: true, vip: true },
        position: { x: 'center', y: '60%' }
    },
    
    // 商城按钮
    'btn-shop': {
        id: 'btn-shop',
        enabled: true,
        texts: {
            'zh-CN': '商城',
            'en-US': 'Shop',
            'ja-JP': 'ショップ',
            'ko-KR': '상점',
            'de-DE': 'Shop',
            'fr-FR': 'Boutique',
            'es-ES': 'Tienda',
            'pt-BR': 'Loja',
            'ru-RU': 'Магазин',
            'ar-SA': 'المتجر',
            'hi-IN': 'दुकान',
            'th-TH': 'ร้านค้า',
            'vi-VN': 'Cửa hàng',
            'id-ID': 'Toko',
            'tr-TR': 'Mağaza'
        },
        style: {
            backgroundColor: 'transparent',
            textColor: '#FFD700',
            fontSize: '14px',
            border: '2px solid #FFD700',
            borderRadius: '20px',
            padding: '10px 25px'
        },
        icon: '🛒',
        redirect: '/shop',
        action: 'navigate',
        visibility: { guest: true, user: true, vip: true },
        badge: { type: 'new', count: null }
    },
    
    // 锦标赛按钮
    'btn-tournament': {
        id: 'btn-tournament',
        enabled: true,
        texts: {
            'zh-CN': '锦标赛',
            'en-US': 'Tournament',
            'ja-JP': 'トーナメント',
            'ko-KR': '토너먼트',
            'de-DE': 'Turnier',
            'fr-FR': 'Tournoi',
            'es-ES': 'Torneo',
            'pt-BR': 'Torneio',
            'ru-RU': 'Турнир',
            'ar-SA': 'البطولة',
            'hi-IN': 'टूर्नामेंट',
            'th-TH': 'ทัวร์นาเมนต์',
            'vi-VN': 'Giải đấu',
            'id-ID': 'Turnamen',
            'tr-TR': 'Turnuva'
        },
        style: {
            backgroundColor: '#FF6B6B',
            textColor: '#FFFFFF',
            fontSize: '14px',
            borderRadius: '20px',
            padding: '10px 25px'
        },
        icon: '🏆',
        redirect: '/tournament',
        action: 'navigate',
        visibility: { guest: false, user: true, vip: true }, // 需登录
        badge: { type: 'hot', text: 'HOT' }
    },
    
    // 连胜模式按钮
    'btn-streak': {
        id: 'btn-streak',
        enabled: true,
        texts: {
            'zh-CN': '连胜模式',
            'en-US': 'Streak Mode',
            'ja-JP': '連勝モード',
            'ko-KR': '연승 모드',
            'de-DE': 'Serie-Modus',
            'fr-FR': 'Mode Série',
            'es-ES': 'Modo Racha',
            'pt-BR': 'Modo Sequência',
            'ru-RU': 'Режим Серии',
            'ar-SA': 'وضع الانتصارات',
            'hi-IN': 'स्ट्रीक मोड',
            'th-TH': 'โหมดสตรีค',
            'vi-VN': 'Chế độ Thắng liên tiếp',
            'id-ID': 'Mode Streak',
            'tr-TR': 'Seri Modu'
        },
        style: {
            backgroundColor: '#FF4757',
            textColor: '#FFFFFF',
            fontSize: '14px',
            borderRadius: '20px',
            padding: '10px 25px',
            animation: 'pulse 2s infinite'
        },
        icon: '🔥',
        redirect: '/streak',
        action: 'navigate',
        visibility: { guest: false, user: true, vip: true },
        badge: { type: 'new', text: 'NEW' }
    },
    
    // VIP按钮
    'btn-vip': {
        id: 'btn-vip',
        enabled: true,
        texts: {
            'zh-CN': 'VIP',
            'en-US': 'VIP',
            'ja-JP': 'VIP',
            'ko-KR': 'VIP',
            'de-DE': 'VIP',
            'fr-FR': 'VIP',
            'es-ES': 'VIP',
            'pt-BR': 'VIP',
            'ru-RU': 'VIP',
            'ar-SA': 'VIP',
            'hi-IN': 'VIP',
            'th-TH': 'VIP',
            'vi-VN': 'VIP',
            'id-ID': 'VIP',
            'tr-TR': 'VIP'
        },
        style: {
            backgroundColor: 'linear-gradient(135deg, #FFD700, #FFA500)',
            textColor: '#1A1A2E',
            fontSize: '14px',
            borderRadius: '20px',
            padding: '10px 25px',
            fontWeight: 'bold'
        },
        icon: '👑',
        redirect: '/vip',
        action: 'navigate',
        visibility: { guest: true, user: true, vip: true },
        badge: { type: 'sale', text: '-50%' }
    },
    
    // 个人中心按钮
    'btn-profile': {
        id: 'btn-profile',
        enabled: true,
        texts: {
            'zh-CN': '个人中心',
            'en-US': 'Profile',
            'ja-JP': 'プロフィール',
            'ko-KR': '프로필',
            'de-DE': 'Profil',
            'fr-FR': 'Profil',
            'es-ES': 'Perfil',
            'pt-BR': 'Perfil',
            'ru-RU': 'Профиль',
            'ar-SA': 'الملف الشخصي',
            'hi-IN': 'प्रोफाइल',
            'th-TH': 'โปรไฟล์',
            'vi-VN': 'Hồ sơ',
            'id-ID': 'Profil',
            'tr-TR': 'Profil'
        },
        style: {
            backgroundColor: 'transparent',
            textColor: '#FFFFFF',
            fontSize: '14px',
            borderRadius: '20px',
            padding: '10px 25px'
        },
        icon: '👤',
        redirect: '/profile',
        action: 'navigate',
        visibility: { guest: false, user: true, vip: true }
    },
    
    // 设置按钮
    'btn-settings': {
        id: 'btn-settings',
        enabled: true,
        texts: {
            'zh-CN': '设置',
            'en-US': 'Settings',
            'ja-JP': '設定',
            'ko-KR': '설정',
            'de-DE': 'Einstellungen',
            'fr-FR': 'Paramètres',
            'es-ES': 'Configuración',
            'pt-BR': 'Configurações',
            'ru-RU': 'Настройки',
            'ar-SA': 'الإعدادات',
            'hi-IN': 'सेटिंग्स',
            'th-TH': 'การตั้งค่า',
            'vi-VN': 'Cài đặt',
            'id-ID': 'Pengaturan',
            'tr-TR': 'Ayarlar'
        },
        style: {
            backgroundColor: 'transparent',
            textColor: '#888888',
            fontSize: '14px',
            borderRadius: '20px',
            padding: '8px 20px'
        },
        icon: '⚙️',
        redirect: '/settings',
        action: 'navigate',
        visibility: { guest: true, user: true, vip: true }
    }
};
```

### 1.2 游戏内按钮

```javascript
// config/buttons/game-controls.js

const GAME_CONTROL_BUTTONS = {
    // 出牌按钮
    'btn-play-card': {
        id: 'btn-play-card',
        enabled: true,
        texts: {
            'zh-CN': '出牌',
            'en-US': 'Play',
            'ja-JP': '出す',
            'ko-KR': '카드 내기',
            'de-DE': 'Ausspielen',
            'fr-FR': 'Jouer',
            'es-ES': 'Jugar',
            'pt-BR': 'Jogar',
            'ru-RU': 'Сыграть',
            'ar-SA': 'اللعب',
            'hi-IN': 'कार्ड खेलें',
            'th-TH': 'เล่นไพ่',
            'vi-VN': 'Đánh bài',
            'id-ID': 'Main Kartu',
            'tr-TR': 'Kart Oyna'
        },
        style: {
            backgroundColor: '#4CAF50',
            textColor: '#FFFFFF',
            fontSize: '16px',
            borderRadius: '25px',
            padding: '12px 35px'
        },
        icon: '▶️',
        action: 'playSelectedCard',
        visibility: { inGame: true, myTurn: true },
        disabledWhen: 'noCardSelected'
    },
    
    // 托管按钮
    'btn-auto-play': {
        id: 'btn-auto-play',
        enabled: true,
        texts: {
            'zh-CN': '托管',
            'en-US': 'Auto',
            'ja-JP': '自動',
            'ko-KR': '자동',
            'de-DE': 'Auto',
            'fr-FR': 'Auto',
            'es-ES': 'Auto',
            'pt-BR': 'Auto',
            'ru-RU': 'Авто',
            'ar-SA': 'تلقائي',
            'hi-IN': 'ऑटो',
            'th-TH': 'อัตโนมัติ',
            'vi-VN': 'Tự động',
            'id-ID': 'Otomatis',
            'tr-TR': 'Oto'
        },
        style: {
            backgroundColor: '#9C27B0',
            textColor: '#FFFFFF',
            fontSize: '14px',
            borderRadius: '20px',
            padding: '8px 20px'
        },
        icon: '🤖',
        action: 'toggleAutoPlay',
        visibility: { inGame: true },
        toggleStates: {
            on: { text: '取消托管', color: '#666' },
            off: { text: '托管', color: '#9C27B0' }
        }
    },
    
    // 退出游戏按钮
    'btn-quit-game': {
        id: 'btn-quit-game',
        enabled: true,
        texts: {
            'zh-CN': '退出',
            'en-US': 'Quit',
            'ja-JP': '退出',
            'ko-KR': '나가기',
            'de-DE': 'Beenden',
            'fr-FR': 'Quitter',
            'es-ES': 'Salir',
            'pt-BR': 'Sair',
            'ru-RU': 'Выйти',
            'ar-SA': 'خروج',
            'hi-IN': 'बाहर निकलें',
            'th-TH': 'ออก',
            'vi-VN': 'Thoát',
            'id-ID': 'Keluar',
            'tr-TR': 'Çık'
        },
        style: {
            backgroundColor: '#F44336',
            textColor: '#FFFFFF',
            fontSize: '14px',
            borderRadius: '20px',
            padding: '8px 20px'
        },
        icon: '🚪',
        action: 'confirmQuitGame',
        visibility: { inGame: true },
        confirmDialog: {
            title: '确认退出',
            message: '退出游戏将视为认输，确定要退出吗？',
            confirmText: '确定退出',
            cancelText: '继续游戏'
        }
    },
    
    // 表情按钮
    'btn-emoji': {
        id: 'btn-emoji',
        enabled: true,
        texts: { all: '' }, // 纯图标按钮
        style: {
            backgroundColor: 'rgba(255,255,255,0.2)',
            borderRadius: '50%',
            width: '40px',
            height: '40px',
            fontSize: '20px'
        },
        icon: '😀',
        action: 'openEmojiPanel',
        visibility: { inGame: true }
    },
    
    // 快捷语按钮
    'btn-quick-chat': {
        id: 'btn-quick-chat',
        enabled: true,
        texts: { all: '' },
        style: {
            backgroundColor: 'rgba(255,255,255,0.2)',
            borderRadius: '50%',
            width: '40px',
            height: '40px',
            fontSize: '20px'
        },
        icon: '💬',
        action: 'openQuickChatPanel',
        visibility: { inGame: true }
    }
};
```

---

## 2. 链接配置系统

### 2.1 导航链接

```javascript
// config/links/navigation.js

const NAVIGATION_LINKS = {
    // 官网链接
    'link-official-website': {
        id: 'link-official-website',
        enabled: true,
        urls: {
            default: 'https://tower-of-fate.com',
            'zh-CN': 'https://tower-of-fate.com/zh',
            'en-US': 'https://tower-of-fate.com/en',
            'ja-JP': 'https://tower-of-fate.com/ja',
            'ko-KR': 'https://tower-of-fate.com/ko'
        },
        openInNewTab: false,
        analytics: { category: 'navigation', action: 'click', label: 'official_website' }
    },
    
    // 帮助中心
    'link-help-center': {
        id: 'link-help-center',
        enabled: true,
        urls: {
            default: 'https://help.tower-of-fate.com',
            'zh-CN': 'https://help.tower-of-fate.com/zh',
            'en-US': 'https://help.tower-of-fate.com/en'
        },
        openInNewTab: true,
        analytics: { category: 'support', action: 'click', label: 'help_center' }
    },
    
    // 客服支持
    'link-customer-support': {
        id: 'link-customer-support',
        enabled: true,
        urls: {
            default: 'https://support.tower-of-fate.com',
            'zh-CN': 'https://support.tower-of-fate.com/zh/chat',
            'en-US': 'https://support.tower-of-fate.com/en/chat'
        },
        openInNewTab: true,
        analytics: { category: 'support', action: 'click', label: 'customer_support' }
    },
    
    // 隐私政策
    'link-privacy-policy': {
        id: 'link-privacy-policy',
        enabled: true,
        urls: {
            default: 'https://tower-of-fate.com/privacy',
            'zh-CN': 'https://tower-of-fate.com/zh/privacy',
            'en-US': 'https://tower-of-fate.com/en/privacy',
            'ja-JP': 'https://tower-of-fate.com/ja/privacy',
            'ko-KR': 'https://tower-of-fate.com/ko/privacy',
            'de-DE': 'https://tower-of-fate.com/de/privacy',
            'fr-FR': 'https://tower-of-fate.com/fr/privacy',
            'es-ES': 'https://tower-of-fate.com/es/privacy',
            'pt-BR': 'https://tower-of-fate.com/pt/privacy',
            'ru-RU': 'https://tower-of-fate.com/ru/privacy',
            'ar-SA': 'https://tower-of-fate.com/ar/privacy',
            'hi-IN': 'https://tower-of-fate.com/hi/privacy',
            'th-TH': 'https://tower-of-fate.com/th/privacy',
            'vi-VN': 'https://tower-of-fate.com/vi/privacy',
            'id-ID': 'https://tower-of-fate.com/id/privacy',
            'tr-TR': 'https://tower-of-fate.com/tr/privacy'
        },
        openInNewTab: true,
        analytics: { category: 'legal', action: 'click', label: 'privacy_policy' }
    },
    
    // 用户协议
    'link-user-agreement': {
        id: 'link-user-agreement',
        enabled: true,
        urls: {
            default: 'https://tower-of-fate.com/agreement',
            'zh-CN': 'https://tower-of-fate.com/zh/agreement',
            'en-US': 'https://tower-of-fate.com/en/agreement',
            'ja-JP': 'https://tower-of-fate.com/ja/agreement',
            'ko-KR': 'https://tower-of-fate.com/ko/agreement',
            'de-DE': 'https://tower-of-fate.com/de/agreement',
            'fr-FR': 'https://tower-of-fate.com/fr/agreement',
            'es-ES': 'https://tower-of-fate.com/es/agreement',
            'pt-BR': 'https://tower-of-fate.com/pt/agreement',
            'ru-RU': 'https://tower-of-fate.com/ru/agreement',
            'ar-SA': 'https://tower-of-fate.com/ar/agreement',
            'hi-IN': 'https://tower-of-fate.com/hi/agreement',
            'th-TH': 'https://tower-of-fate.com/th/agreement',
            'vi-VN': 'https://tower-of-fate.com/vi/agreement',
            'id-ID': 'https://tower-of-fate.com/id/agreement',
            'tr-TR': 'https://tower-of-fate.com/tr/agreement'
        },
        openInNewTab: true,
        analytics: { category: 'legal', action: 'click', label: 'user_agreement' }
    },
    
    // 社交媒体
    'link-facebook': {
        id: 'link-facebook',
        enabled: true,
        urls: {
            default: 'https://facebook.com/toweroffate'
        },
        openInNewTab: true,
        icon: 'facebook',
        analytics: { category: 'social', action: 'click', label: 'facebook' }
    },
    
    'link-twitter': {
        id: 'link-twitter',
        enabled: true,
        urls: {
            default: 'https://twitter.com/toweroffate'
        },
        openInNewTab: true,
        icon: 'twitter',
        analytics: { category: 'social', action: 'click', label: 'twitter' }
    },
    
    'link-discord': {
        id: 'link-discord',
        enabled: true,
        urls: {
            default: 'https://discord.gg/toweroffate'
        },
        openInNewTab: true,
        icon: 'discord',
        analytics: { category: 'social', action: 'click', label: 'discord' }
    },
    
    'link-youtube': {
        id: 'link-youtube',
        enabled: true,
        urls: {
            default: 'https://youtube.com/@toweroffate'
        },
        openInNewTab: true,
        icon: 'youtube',
        analytics: { category: 'social', action: 'click', label: 'youtube' }
    }
};
```

### 2.2 推广链接

```javascript
// config/links/promotions.js

const PROMOTION_LINKS = {
    // 应用商店
    'link-app-store': {
        id: 'link-app-store',
        enabled: true,
        urls: {
            ios: 'https://apps.apple.com/app/tower-of-fate/id123456789',
            android: 'https://play.google.com/store/apps/details?id=com.toweroffate.game'
        },
        redirectLogic: 'detectDevice',
        analytics: { category: 'download', action: 'click', label: 'app_store' }
    },
    
    // 邀请好友
    'link-invite-friends': {
        id: 'link-invite-friends',
        enabled: true,
        urlTemplate: 'https://tower-of-fate.com/invite?ref={{userId}}&code={{inviteCode}}',
        openInNewTab: false,
        analytics: { category: 'referral', action: 'click', label: 'invite' }
    },
    
    // 推广活动
    'link-promo-events': {
        id: 'link-promo-events',
        enabled: true,
        urls: {
            current: 'https://tower-of-fate.com/events/spring-festival-2026',
            scheduled: [
                { start: '2026-04-01', end: '2026-04-07', url: 'https://tower-of-fate.com/events/easter-2026' },
                { start: '2026-05-01', end: '2026-05-07', url: 'https://tower-of-fate.com/events/labor-day-2026' }
            ]
        },
        autoRedirect: true,
        analytics: { category: 'promotion', action: 'click', label: 'events' }
    }
};
```

---

## 3. 后台管理界面

### 3.1 按钮配置管理

```html
<!-- admin/button-config-manager.html -->
<div class="config-manager">
    <div class="config-sidebar">
        <h3>🎮 按钮配置</h3>
        <div class="config-categories">
            <div class="category active" data-category="main-menu">主界面按钮</div>
            <div class="category" data-category="game-controls">游戏内按钮</div>
            <div class="category" data-category="shop">商城按钮</div>
            <div class="category" data-category="profile">个人中心按钮</div>
            <div class="category" data-category="social">社交按钮</div>
        </div>
    </div>
    
    <div class="config-content">
        <div class="config-header">
            <h2>主界面按钮配置</h2>
            <button class="btn-add" onclick="addNewButton()">+ 添加按钮</button>
        </div>
        
        <div class="button-list">
            <!-- 按钮配置卡片 -->
            <div class="button-card" data-button-id="btn-start-game">
                <div class="button-preview">
                    <button style="background: #FFD700; color: #1A1A2E; padding: 15px 40px; border-radius: 25px;">
                        ▶️ 开始游戏
                    </button>
                </div>
                
                <div class="button-settings">
                    <div class="setting-group">
                        <label>按钮ID</label>
                        <input type="text" value="btn-start-game" readonly>
                    </div>
                    
                    <div class="setting-group">
                        <label>启用状态</label>
                        <label class="toggle">
                            <input type="checkbox" checked>
                            <span class="toggle-slider"></span>
                        </label>
                    </div>
                    
                    <div class="setting-group">
                        <label>多语言文本</label>
                        <div class="lang-inputs">
                            <div class="lang-input">
                                <span class="lang-flag">🇨🇳</span>
                                <input type="text" value="开始游戏" data-lang="zh-CN">
                            </div>
                            <div class="lang-input">
                                <span class="lang-flag">🇺🇸</span>
                                <input type="text" value="Start Game" data-lang="en-US">
                            </div>
                            <!-- 更多语言... -->
                        </div>
                    </div>
                    
                    <div class="setting-group">
                        <label>样式设置</label>
                        <div class="style-settings">
                            <div class="style-input">
                                <span>背景色</span>
                                <input type="color" value="#FFD700">
                            </div>
                            <div class="style-input">
                                <span>文字色</span>
                                <input type="color" value="#1A1A2E">
                            </div>
                            <div class="style-input">
                                <span>圆角</span>
                                <input type="range" min="0" max="50" value="25">
                            </div>
                        </div>
                    </div>
                    
                    <div class="setting-group">
                        <label>跳转链接</label>
                        <input type="text" value="" placeholder="留空执行游戏逻辑">
                        <label class="checkbox">
                            <input type="checkbox"> 新窗口打开
                        </label>
                    </div>
                    
                    <div class="setting-group">
                        <label>显示条件</label>
                        <div class="visibility-options">
                            <label><input type="checkbox" checked> 游客可见</label>
                            <label><input type="checkbox" checked> 注册用户可见</label>
                            <label><input type="checkbox" checked> VIP用户可见</label>
                        </div>
                    </div>
                    
                    <div class="button-actions">
                        <button class="btn-save" onclick="saveButtonConfig('btn-start-game')">💾 保存</button>
                        <button class="btn-preview" onclick="previewButton('btn-start-game')">👁️ 预览</button>
                        <button class="btn-delete" onclick="deleteButton('btn-start-game')">🗑️ 删除</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
```

### 3.2 链接配置管理

```html
<!-- admin/link-config-manager.html -->
<div class="config-manager">
    <div class="config-header">
        <h2>🔗 链接配置管理</h2>
        <div class="config-actions">
            <button class="btn-add" onclick="addNewLink()">+ 添加链接</button>
            <button class="btn-batch" onclick="batchEdit()">批量编辑</button>
        </div>
    </div>
    
    <div class="links-table-container">
        <table class="links-table">
            <thead>
                <tr>
                    <th>链接ID</th>
                    <th>类型</th>
                    <th>默认URL</th>
                    <th>多语言URL</th>
                    <th>打开方式</th>
                    <th>状态</th>
                    <th>操作</th>
                </tr>
            </thead>
            <tbody>
                <tr data-link-id="link-official-website">
                    <td>link-official-website</td>
                    <td><span class="tag tag-nav">导航</span></td>
                    <td>
                        <input type="text" value="https://tower-of-fate.com" class="url-input">
                    </td>
                    <td>
                        <button class="btn-lang-urls" onclick="editLangUrls('link-official-website')">
                            15个语言版本
                        </button>
                    </td>
                    <td>
                        <select>
                            <option value="self">当前窗口</option>
                            <option value="blank" selected>新窗口</option>
                        </select>
                    </td>
                    <td>
                        <label class="toggle">
                            <input type="checkbox" checked>
                            <span class="toggle-slider"></span>
                        </label>
                    </td>
                    <td>
                        <button class="btn-save" onclick="saveLink('link-official-website')">保存</button>
                        <button class="btn-test" onclick="testLink('https://tower-of-fate.com')">测试</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
```

---

## 4. 实时同步机制

```javascript
// services/config-sync.js

class ConfigSyncService {
    constructor() {
        this.ws = null;
        this.configCache = new Map();
        this.subscribers = new Map();
    }
    
    // 连接WebSocket
    connect() {
        this.ws = new WebSocket('wss://api.tower-of-fate.com/config-sync');
        
        this.ws.onopen = () => {
            console.log('配置同步服务已连接');
            this.subscribeToAllConfigs();
        };
        
        this.ws.onmessage = (event) => {
            const data = JSON.parse(event.data);
            this.handleConfigUpdate(data);
        };
        
        this.ws.onclose = () => {
            console.log('配置同步服务断开，尝试重连...');
            setTimeout(() => this.connect(), 3000);
        };
    }
    
    // 处理配置更新
    handleConfigUpdate(data) {
        const { configType, configId, changes, timestamp } = data;
        
        // 更新缓存
        const cacheKey = `${configType}:${configId}`;
        this.configCache.set(cacheKey, {
            ...changes,
            _lastUpdate: timestamp
        });
        
        // 通知订阅者
        const subscribers = this.subscribers.get(cacheKey) || [];
        subscribers.forEach(callback => callback(changes));
        
        // 广播到前端
        this.broadcastToFrontend(configType, configId, changes);
    }
    
    // 广播到前端
    broadcastToFrontend(configType, configId, changes) {
        // 通过WebSocket或SSE推送到游戏客户端
        window.dispatchEvent(new CustomEvent('configUpdated', {
            detail: { configType, configId, changes }
        }));
    }
    
    // 保存配置（后台调用）
    async saveConfig(configType, configId, configData) {
        const response = await fetch('/api/admin/config', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${getAdminToken()}`
            },
            body: JSON.stringify({
                configType,
                configId,
                configData,
                timestamp: Date.now()
            })
        });
        
        if (response.ok) {
            // 通过WebSocket广播给其他管理员和前端
            this.ws.send(JSON.stringify({
                type: 'configUpdate',
                configType,
                configId,
                changes: configData
            }));
            
            return { success: true };
        }
        
        return { success: false, error: await response.text() };
    }
    
    // 获取配置
    getConfig(configType, configId) {
        const cacheKey = `${configType}:${configId}`;
        return this.configCache.get(cacheKey);
    }
    
    // 订阅配置变更
    subscribe(configType, configId, callback) {
        const cacheKey = `${configType}:${configId}`;
        if (!this.subscribers.has(cacheKey)) {
            this.subscribers.set(cacheKey, []);
        }
        this.subscribers.get(cacheKey).push(callback);
        
        // 返回取消订阅函数
        return () => {
            const subs = this.subscribers.get(cacheKey);
            const index = subs.indexOf(callback);
            if (index > -1) subs.splice(index, 1);
        };
    }
}

// 导出单例
const configSyncService = new ConfigSyncService();
export default configSyncService;
```

---

## 5. 配置变更日志

```javascript
// models/config-change-log.js

const configChangeLogSchema = {
    id: String,           // 日志ID
    configType: String,   // 配置类型（button/link/text）
    configId: String,     // 配置ID
    action: String,       // 操作类型（create/update/delete）
    
    before: Object,       // 变更前数据
    after: Object,        // 变更后数据
    
    operator: {
        id: String,       // 操作人ID
        name: String,     // 操作人姓名
        role: String      // 操作人角色
    },
    
    timestamp: Date,      // 操作时间
    ip: String,          // 操作IP
    userAgent: String,   // 操作设备
    
    approvedBy: {        // 审批信息（重要变更）
        id: String,
        name: String,
        timestamp: Date
    },
    
    rollbackInfo: {      // 回滚信息
        canRollback: Boolean,
        rollbackTo: String  // 回滚到哪个版本
    }
};
```

---

## 6. API 接口规范

### 6.1 按钮配置接口

```javascript
// 获取按钮配置
GET /api/admin/config/buttons?category=main-menu

// 更新按钮配置
PUT /api/admin/config/buttons/:buttonId
{
    "texts": { "zh-CN": "新文本", "en-US": "New Text" },
    "style": { "backgroundColor": "#FF0000" },
    "enabled": true
}

// 批量更新
POST /api/admin/config/buttons/batch
{
    "buttons": [
        { "id": "btn-1", "texts": {...} },
        { "id": "btn-2", "texts": {...} }
    ]
}
```

### 6.2 链接配置接口

```javascript
// 获取链接配置
GET /api/admin/config/links

// 更新链接
PUT /api/admin/config/links/:linkId
{
    "urls": { "default": "https://new-url.com", "zh-CN": "https://new-url.com/zh" },
    "openInNewTab": true
}

// 测试链接可访问性
POST /api/admin/config/links/:linkId/test
// 返回：{ "accessible": true, "statusCode": 200, "responseTime": 150 }
```

---

## 7. 前端适配代码

```javascript
// hooks/useConfig.js - React Hook示例

import { useState, useEffect } from 'react';
import configSyncService from '../services/config-sync';

export function useButtonConfig(buttonId) {
    const [config, setConfig] = useState(null);
    const [loading, setLoading] = useState(true);
    
    useEffect(() => {
        // 获取初始配置
        fetch(`/api/config/buttons/${buttonId}`)
            .then(res => res.json())
            .then(data => {
                setConfig(data);
                setLoading(false);
            });
        
        // 订阅实时更新
        const unsubscribe = configSyncService.subscribe('button', buttonId, (changes) => {
            setConfig(prev => ({ ...prev, ...changes }));
        });
        
        return unsubscribe;
    }, [buttonId]);
    
    return { config, loading };
}

// 使用示例
function StartGameButton() {
    const { config, loading } = useButtonConfig('btn-start-game');
    const { language } = useLanguage(); // 获取当前语言
    
    if (loading) return <button>加载中...</button>;
    
    const text = config.texts[language] || config.texts['en-US'];
    
    return (
        <button
            style={{
                backgroundColor: config.style.backgroundColor,
                color: config.style.textColor,
                borderRadius: config.style.borderRadius,
                padding: config.style.padding,
                fontSize: config.style.fontSize
            }}
            onClick={() => {
                if (config.redirect) {
                    window.open(config.redirect, config.openInNewTab ? '_blank' : '_self');
                } else {
                    executeAction(config.action);
                }
            }}
        >
            {config.icon} {text}
        </button>
    );
}
```

---

## 8. 配置验证规则

```javascript
// validators/config-validator.js

const configValidationRules = {
    button: {
        id: { required: true, pattern: /^[a-z0-9-]+$/ },
        texts: {
            required: true,
            minLength: 1,
            languages: ['zh-CN', 'en-US'] // 至少这两种语言
        },
        style: {
            backgroundColor: { pattern: /^#[0-9A-F]{6}$/i },
            fontSize: { pattern: /^\d+px$/ }
        },
        redirect: {
            pattern: /^(https?:\/\/)?([\da-z.-]+)\.([a-z.]{2,6})([/\w .-]*)*\/?$/,
            allowEmpty: true
        }
    },
    
    link: {
        id: { required: true, pattern: /^[a-z0-9-]+$/ },
        urls: {
            required: true,
            validate: (urls) => {
                for (const [lang, url] of Object.entries(urls)) {
                    if (!isValidURL(url)) {
                        return { valid: false, error: `Invalid URL for ${lang}` };
                    }
                }
                return { valid: true };
            }
        }
    }
};

function validateConfig(configType, configData) {
    const rules = configValidationRules[configType];
    const errors = [];
    
    for (const [field, rule] of Object.entries(rules)) {
        const value = configData[field];
        
        if (rule.required && !value) {
            errors.push(`${field} is required`);
        }
        
        if (rule.pattern && value && !rule.pattern.test(value)) {
            errors.push(`${field} format is invalid`);
        }
        
        if (rule.validate && value) {
            const result = rule.validate(value);
            if (!result.valid) {
                errors.push(result.error);
            }
        }
    }
    
    return { valid: errors.length === 0, errors };
}
```

---

*文档版本: 1.0*  
*最后更新: 2026年03月08日*
