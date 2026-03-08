# 命运塔用户协议集成指南

## 概述

本文档说明如何将多语言用户协议系统集成到命运塔游戏中。

## 文件结构

```
├── js/
│   └── i18n/
│       └── user-agreement-i18n.js    # 多语言用户协议核心代码
├── css/
│   └── user-agreement.css            # 用户协议样式
├── docs/
│   ├── user-agreement-zh-CN.html     # 中文完整版
│   ├── user-agreement-zh-CN.pdf      # 中文PDF版
│   ├── user-agreement-en-US.html     # 英文完整版
│   ├── user-agreement-en-US.pdf      # 英文PDF版
│   └── ...                           # 其他13种语言版本
└── integration-example.html          # 集成示例
```

## 快速集成

### 1. 引入必要文件

在游戏的HTML文件中添加：

```html
<!-- 在 <head> 中引入样式 -->
<link rel="stylesheet" href="css/user-agreement.css">

<!-- 在 </body> 前引入脚本 -->
<script src="js/i18n/user-agreement-i18n.js"></script>
```

### 2. 初始化用户协议

```javascript
// 页面加载完成后自动初始化
document.addEventListener('DOMContentLoaded', function() {
    // 自动检测是否需要显示协议弹窗
    userAgreementManager.init();
});
```

### 3. 监听用户同意事件

```javascript
window.addEventListener('userAgreementAccepted', function(e) {
    console.log('用户已同意协议，语言：', e.detail.lang);
    // 在这里执行游戏初始化逻辑
    startGame();
});
```

## 支持的15种语言

| 语言代码 | 语言 | 适用地区 |
|---------|------|---------|
| zh-CN | 简体中文 | 中国、新加坡 |
| en-US | 英语 | 全球 |
| ja-JP | 日语 | 日本 |
| ko-KR | 韩语 | 韩国 |
| de-DE | 德语 | 德国、奥地利、瑞士 |
| fr-FR | 法语 | 法国、加拿大、比利时 |
| es-ES | 西班牙语 | 西班牙、拉美 |
| pt-BR | 葡萄牙语 | 巴西、葡萄牙 |
| ru-RU | 俄语 | 俄罗斯、CIS |
| ar-SA | 阿拉伯语 | 中东、北非 |
| hi-IN | 印地语 | 印度 |
| th-TH | 泰语 | 泰国 |
| vi-VN | 越南语 | 越南 |
| id-ID | 印尼语 | 印尼 |
| tr-TR | 土耳其语 | 土耳其 |

## API参考

### UserAgreementManager 类

#### 方法

| 方法 | 说明 | 参数 |
|-----|------|------|
| `init()` | 初始化并显示协议弹窗（如需要） | 无 |
| `getAgreement(lang)` | 获取指定语言的协议内容 | `lang`: 语言代码 |
| `setLanguage(lang)` | 设置当前语言 | `lang`: 语言代码 |
| `needShowAgreement()` | 检查是否需要显示协议 | 返回布尔值 |
| `agree(version)` | 记录用户同意 | `version`: 协议版本 |
| `renderAgreementModal()` | 渲染协议弹窗HTML | 返回HTML字符串 |
| `changeLanguage(lang)` | 切换语言并重新渲染 | `lang`: 语言代码 |
| `accept()` | 用户点击同意 | 无 |
| `decline()` | 用户点击拒绝 | 无 |

#### 属性

| 属性 | 说明 |
|-----|------|
| `currentLang` | 当前语言代码 |
| `agreedVersions` | 已同意的协议版本记录 |

### 事件

| 事件名 | 触发时机 | 参数 |
|-------|---------|------|
| `userAgreementAccepted` | 用户同意协议时 | `{ lang: 语言代码 }` |

## 本地化存储

用户协议系统使用 `localStorage` 存储以下数据：

| Key | 说明 |
|-----|------|
| `user-agreement-lang` | 用户选择的语言 |
| `agreed-versions` | 各语言版本的同意记录 |
| `agreed-at-{lang}` | 同意时间戳 |

## 版本控制

协议版本管理：

```javascript
// 检查当前版本是否需要重新同意
needShowAgreement() {
    const currentVersion = '1.0'; // 更新协议时修改版本号
    const lastAgreed = this.agreedVersions[this.currentLang];
    return !lastAgreed || lastAgreed !== currentVersion;
}
```

**重要**: 当协议内容更新时，务必修改版本号，以提示用户重新同意。

## 自定义配置

### 修改默认语言

```javascript
// 在初始化前设置默认语言
userAgreementManager.setLanguage('en-US');
userAgreementManager.init();
```

### 强制显示协议

```javascript
// 清除同意记录，强制用户重新同意
localStorage.removeItem('agreed-versions');
userAgreementManager.init();
```

### 自定义样式

可以通过覆盖CSS变量来自定义外观：

```css
.agreement-content {
    --primary-color: #your-color;
    --secondary-color: #your-color;
}
```

## 完整协议页面

除了弹窗形式的协议，还需要提供完整的协议页面供用户随时查看：

```
docs/
├── user-agreement-zh-CN.html    # 中文HTML版
├── user-agreement-zh-CN.pdf     # 中文PDF版
├── user-agreement-en-US.html    # 英文HTML版
├── user-agreement-en-US.pdf     # 英文PDF版
└── ...                          # 其他语言版本
```

## 测试清单

- [ ] 首次访问时自动显示协议弹窗
- [ ] 未勾选年龄确认时，同意按钮禁用
- [ ] 点击同意后，弹窗关闭，触发事件
- [ ] 刷新页面后不再显示（已同意）
- [ ] 语言切换功能正常
- [ ] 各语言版本内容正确
- [ ] 移动端显示正常
- [ ] RTL语言（阿拉伯语）显示正确
- [ ] 点击"阅读完整协议"打开详细页面
- [ ] 点击"下载PDF"下载PDF版本

## 法律合规检查

确保用户协议包含以下必要条款：

- [ ] 账号管理和实名认证
- [ ] 虚拟物品所有权声明
- [ ] 禁止行为列表
- [ ] 未成年人保护（防沉迷、消费限制）
- [ ] 隐私政策链接
- [ ] 免责声明
- [ ] 争议解决条款
- [ ] 联系方式

## 注意事项

1. **版本更新**: 修改协议内容时，必须更新版本号
2. **法律审查**: 发布前建议请法律专业人士审查
3. **地区差异**: 不同地区可能有不同的法律要求
4. **年龄验证**: 确保未成年人保护措施生效
5. **记录保存**: 保留用户的同意记录

## 联系支持

如有问题，请联系：
- 技术支持：tech@tower-of-fate.com
- 法务咨询：legal@tower-of-fate.com

---

*最后更新：2026年03月08日*
